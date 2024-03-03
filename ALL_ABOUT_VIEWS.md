1. Create **urls.py** in /blog
    * This file is where we'll list our blog app-specific URLs.
2. Remove blog-view-import in **codestar/urls.py**
    * We don't need it anymore, cause /blog has its own **urls.py** now
    * Instead we add **include** to **from django.urls import path, include**
    * Replace: 
        path("blog/", blog_views.blog, name='blog') with 
        path("", include("blog.urls"), name="blog-urls")
3. Create **templates** directory in /blog with another directory nested within, named blog. 
    * mkdir -p blog/templates/blog


# Create a class based view:
1. in blog/view.py add:
    ```python 
        from django.views import generic
        from .models import Post

        # Create your views here.
        class PostList(generic.ListView):
            model = Post
    ```

2. in blog/urls.py add:
    ```python
        from . import views
        from django.urls import path

        urlpatterns = [
            path('', views.PostList.as_view(), name='home'),
        ]
    ```

