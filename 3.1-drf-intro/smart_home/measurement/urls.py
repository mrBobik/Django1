from django.urls import path
# from measurement.views import demo
from measurement.views import SensorCreateAPIView, SensorUpdateAPIView, MeasurementCreateAPIView, SensorListAPIView, SensorRetrieveAPIView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/create/', SensorCreateAPIView.as_view(), name='create-sensor'),
    path('sensors/<pk>/update/', SensorUpdateAPIView.as_view(), name='update-sensor'),
    path('measurements/<int:id>/create/', MeasurementCreateAPIView.as_view(), name='create-measurement'),
    path('sensors/',  SensorListAPIView.as_view(), name='sensors-list'),
    path('sensor/<pk>/', SensorRetrieveAPIView.as_view(), name='sensor'),
]
