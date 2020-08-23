from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class PostSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['author', 'title', 'body', 'created', 'updated']
