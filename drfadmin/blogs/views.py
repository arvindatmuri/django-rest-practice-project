from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    print(PostSerializer.data)
