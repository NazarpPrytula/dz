from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer

class PostListApiView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    
    def get(self, request, *args, **kwargs):
        Post = Post.objects.filter(user = request.user.id)
        serializer = PostSerializer(Post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

