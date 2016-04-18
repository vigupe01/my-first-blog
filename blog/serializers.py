from django.contrib.auth.models import User
from .models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'image')
    author = serializers.CharField(read_only=True, required=False)
