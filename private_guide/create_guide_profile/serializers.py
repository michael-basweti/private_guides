from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile, Video, Image
from authentication.models import User


class ProfileSerializer(serializers.ModelSerializer):
    # """
    # Serializer to map the UserProfile instance into JSON format
    # """
    # username = serializers.RegexField(
    #     regex='^(?!.*\ )[A-Za-z\d\-\_]+$',
    #     min_length=4,
    #     required=True,
    #     source='user.username',
    #     validators=[
    #         UniqueValidator(
    #             queryset=Profile.objects.all(),
    #             message='Username must be unique',
    #         )
    #     ],
    #     error_messages={
    #         'invalid': 'Username cannot have a space',
    #         'required': 'Username is required',
    #         'min_length': 'Username must have at least 4 characters'
    #     }
    # )
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'