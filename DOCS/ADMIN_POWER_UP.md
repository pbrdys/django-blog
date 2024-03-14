we'll enhance the admin panel to simplify the process of adding and editing blog posts for the superuser. We'll introduce Summernote, a robust text editor, to achieve this.

1. Firstly, install the django-summernote package.
    ```python
        pip3 install django-summernote~=0.8.20.0
    ```

2. Add the django-summernote package to the requirements.txt file.

3. Append django_summernote to the **INSTALLED_APPS** within **codestar/settings.py**
    ```python
        'django_summernote',.
    ```
**NOTE**: The app might be called django-summernote when we install it through pip3. But in the INSTALLED_APPS we have to call it by the name django_summernote.
This is due to naming convention of python!

4. Include the summernote urlpattern within codestar/urls.py file:
    ```python
        path('summernote/', include('django_summernote.urls')),
    ```

5. go to **blog/admin.py** and ADD:
```python 
    from django_summernote.admin import SummernoteModelAdmin

    @admin.register()
    class PostAdmin(SummernoteModelAdmin):

        list_display = ('title', 'slug', 'status')
        search_fields = ['title']
        list_filter = ('status',)
        prepopulated_fields = {'slug': ('title',)}
        summernote_fields = ('content',)
```
**Note**: The decorator is how we register a class, compared to just registering the standard model as we did before. When we use a class, we register it with a decorator that is more Pythonic and allows us to customise how the models we are registering will appear on the admin site.

@admin.register(Post)

admin.site.register(Post) can be removed now!

6. python3 manage.py migrate

7. Run the Django server and open in a browser