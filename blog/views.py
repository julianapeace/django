from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
@api_view(['GET']) #you can also include POST requests
def post_list (request, slug):
posts = Post.objects.filter(blog__slug=slug) #look up posts by the slug
serializer = PostSerializer(posts, many=True) #pass the data to the serializer
return Response(serializer.data) #send back the response
