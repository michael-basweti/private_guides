from django.db.models import Avg
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile, Image, Video, Review
from authentication.models import User
import datetime
from authentication.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    
    age = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.id')

    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

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
        # response['reviews'] = UserSerializer(instance.reviews).data
        return response

    def get_average_rating(self, obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
        
        if average is None:
            return 0
        
        return round(average*2)/2


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

class ReviewSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Review
        fields = '__all__'
        
    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError(
            'Rating must be an integer between 1 and 5'
        )
