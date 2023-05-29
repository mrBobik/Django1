from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):

    creator = UserSerializer(read_only=True)
    status = serializers.ChoiceField(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at')

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError('Only authenticated users can create advertisements.')
        if data.get('status', '') == AdvertisementStatusChoices.OPEN:
            open_ads_count = Advertisement.objects.filter(creator=self.context['request'].user, status=AdvertisementStatusChoices.OPEN).count()
            if open_ads_count >= 10:
                raise serializers.ValidationError('You cannot create more than 10 open advertisements.')
        return data
