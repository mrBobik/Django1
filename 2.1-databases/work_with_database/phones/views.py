from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_request = request.GET.get('sort', 'all')
    if sort_request == 'all':
        phone_objects = Phone.objects.all()
    else:
        sorted = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}
        phone_objects = Phone.objects.order_by(sorted[sort_request])
    phones_list =[]
    for phone in phone_objects:
        phones_list.append({'name': phone.name,
                'image': phone.image,
                'price': phone.price,
                'release_date': phone.release_date,
                'lte_exists': phone.lte_exists,
                'slug': phone.slug.replace(' ', '-')})
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(name=slug.replace('-', ' '))
    context = {'phone': phone}
    return render(request, template, context)
