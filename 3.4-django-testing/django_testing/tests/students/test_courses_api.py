import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient
from students.filters import CourseFilter
from students.models import Student, Course
from django.urls import reverse


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = client.get(url, headers={'Accept': 'application/json'})
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == course.pk


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    course = course_factory(_quantity=2)
    url = reverse('courses-list')
    response = client.get(url, headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert len(response.data) == 2


@pytest.mark.django_db
def test_filter_course_by_id(client, course_factory):
    course1 = course_factory()
    course2 = course_factory()
    course3 = course_factory()
    filtered_ids = [course1.pk, course3.pk]
    url = reverse('courses-list')
    data = {'id': filtered_ids}
    my_filter = CourseFilter(data=data, queryset=Course.objects.all())
    response = client.get(url, data, content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == len(filtered_ids)
    assert all(course['id'] in filtered_ids for course in response.json())


@pytest.mark.django_db
def test_filter_course_by_name(client, course_factory):
    course1 = course_factory(name='course1')
    course2 = course_factory(name='course2')
    course3 = course_factory(name='course3')
    url = reverse('courses-list')
    data = {'name': 'course1'}
    my_filter = CourseFilter(data=data, queryset=Course.objects.all())
    response = client.get(url, data, content_type='application/json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]['id'] == course1.pk
    assert response.json()[0]['name'] == course1.name
    assert all(course.id == course1.pk for course in my_filter.qs)


@pytest.mark.django_db
def test_create_course(client):
    data = {
        'name': 'Django',
    }
    url = reverse('courses-list')
    response = client.post(url, data)
    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert response.data['name'] == data['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    update_data = {
        'name': 'Updated Course',
    }
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = client.patch(url, update_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == update_data['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Course.objects.filter(id=course.pk).exists()
