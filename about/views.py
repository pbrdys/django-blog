from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import About

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about},
    )