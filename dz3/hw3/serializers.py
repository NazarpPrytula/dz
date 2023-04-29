from hw3.models import review, PublishedTime, Post
from rest_framework import routers, serializers, viewsets


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'review', 'PublishedTime', 'like', 'dislike')
