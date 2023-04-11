from rest_framework import serializers
from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
# class SensorSerializer(serializers.Serializer):
#     id = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()

# class SensorSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Sensor
#         fields = ['id', 'title', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor']


class SensorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
