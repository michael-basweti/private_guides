from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile
from authentication.models import User
import datetime


class ProfileSerializer(serializers.ModelSerializer):
    
    age = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        super().update(instance, validated_data)
        if user_data is not None and user_data.get('email') is not None:
            instance.user.email = user_data.get('email')
            instance.user.save()
        return instance

    class Meta:
        model = Profile
        fields = '__all__'

    def get_age(self, instance):
        return datetime.datetime.now().year - instance.dob.year
