from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def index(request):
#     return HttpResponse("Ello, ello, Blog og og og og")
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"