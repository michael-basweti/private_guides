from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile, Image, Video
from authentication.models import User
import datetime
from authentication.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    
    age = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Profile
        fields = '__all__'

        def update(self, instance, validated_data):
            # retrieve the User
            user_data = validated_data.pop('user', None)
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)

            # retrieve Profile
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.user.save()
            instance.save()
            return instance

    def get_age(self, instance):
        try:
            return datetime.datetime.now().year - instance.dob.year
        except:
            return "Null"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response


class ImageSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Image
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Video
        fields = '__all__'