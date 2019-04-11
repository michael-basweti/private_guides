from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Review
        fields = '__all__'