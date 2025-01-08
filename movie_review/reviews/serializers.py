from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(read_only = True)

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'content', 'rating', 'user', 'created_at', 'updated_at']
        read_only_fields = ['user']