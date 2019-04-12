from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Blog
        fields = '__all__'

