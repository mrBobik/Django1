from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from measurement.serializers import SensorSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         sensserial = SensorSerializer(sensors, many=True)
#         return Response(sensserial.data)
#     if request.method == 'POST':
#         return Response({'Status': 'OK'})

# class DemoView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         sensserial = SensorSerializer(sensors, many=True)
#         return Response(sensserial.data)
#     def post(self, request):
#         return Response({'Status': 'OK'})

class SensorCreateAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def sensor_create(self, serializer):
        serializer.save()


class SensorUpdateAPIView(UpdateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()

    def sensor_update(self, serializer):
        serializer.save()


class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def measure_create(self, serializer):
        serializer.save()


class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
