from django.shortcuts import render

# Create your views here.
from posts.models import Post
from django.views.generic import ListView  # new



# Create your views here.
class PostList(ListView):  # new
    model = Post
    template_name = "post_list.html"