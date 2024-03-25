from django.shortcuts import render
from  .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BlogList(APIView):
    def get(self,request,format=None):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return  Response(serializer.data,status=status.HTTP_200_OK)
    

class AddPost(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Post Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk,format=None):
        post=Post.objects.get(id=pk)
        serializer=PostSerializer(post)
        return  Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        post=Post.objects.get(id=pk)
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_200_OK)
        return  Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,pk,format=None):
        post=Post.objects.get(id=pk)
        serializer=PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_200_OK)
        return  Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)  
    
    def delete(self,request,pk,format=None):
        post=Post.objects.get(id=pk)
        if post is not None:
            post.delete()
            return Response({'msg':'Post Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'msg':'Something went wrong'},status=status.HTTP_404_NOT_FOUND)


