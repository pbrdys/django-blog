from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def index(request):
#     return HttpResponse("Ello, ello, Blog og og og og")

class PostList(generic.ListView):
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1)
    # queryset = Post.objects.all().order_by("created_on")
    template_name = "post_list.html"