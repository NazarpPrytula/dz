from django.shortcuts import render
from rest_framework import viewsets, permissions
from hw3.serializers import PostSerializer
from hw3.models import Post


# Create your views here.


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [
        permissions.IsAuthenticated   
    ]

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        self.queryset = Post.objects.filter(title__icontains=query)
        return self.queryset