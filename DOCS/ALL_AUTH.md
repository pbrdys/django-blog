
# ALLAUTH 
1. Install the Allauth package.
```python 
    pip3 install django-allauth~=0.57.0
```
2. Add to requirements.txt
```python
    pip3 freeze --local > requirements.txt
```

3. project/settings.py add:
```python
    INSTALLED_APPS = [
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
    ]
```

4. Add the following constants in **project/settings.py** directly below the **INSTALLED_APPS** list.
```python
    SITE_ID = 1
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/'
```
**NOTE**: We need to add a SITE_ID of 1 so that Django can handle multiple sites from one database. We need to give each project an ID value so that the database is aware of which project is contacting it. We only have one site here using our one database, but we'll still need to tell Django the site number of 1 explicitly.

The redirection URLs are also added so that after we've logged in or logged out, the site will automatically redirect us to the home page.

5. Append the following line to the list of MIDDLEWARE in codestar/settings.py.
```python
    MIDDLEWARE = [
    # …
    'allauth.account.middleware.AccountMiddleware',
]
```
**NOTE**: This is the middleware for the **allauth.account** app you added to INSTALLED_APPS. It adds additional functionality to the project's account user authentication.

6. Below the AUTH_PASSWORD_VALIDATORS, in codestar/settings.py, add:

```python
    ACCOUNT_EMAIL_VERIFICATION = 'none'
```

Note: We are not using email verification in this project, so this line informs Django not to expect it. Without this line, you would get Internal Server errors (code 500) during login and registration. 

7. Save all the files and migrate.

```python
    python3 manage.py migrate
```
**NOTE**: Just as with django_summernote previously, you do not need makemigrations as the migrations directory and files already exist in the account, site and socialaccount apps.

8.  Open the **codestar/urls.py** file and include the path of accounts in the urlpatterns below about.

```python
    urlpatterns = [
        # …
        path("accounts/", include("allauth.urls")),
        # …
    ]
```


## Adding and modifying templates

1. Open the base.html template and assign the new URLs to variables using the as keyword.

```python
    {% url 'account_login' as login_url %}
    {% url 'account_signup' as signup_url %}
    {% url 'account_logout' as logout_url %}
```

2. Also, in base.html, add Logout, Register and Login links, with their template tags directly below the About link.

```python
    {% if user.is_authenticated %}
    <li class="nav-item">
        <a class="nav-link {% if request.path == logout_url %}active{% endif %}" aria-current="page" href="{% url 'account_logout' %}">Logout</a>
    </li>
    {% else %}
    <li class="nav-item">
        <a class="nav-link {% if request.path == signup_url %}active{% endif %}" aria-current="page"
            href="{% url 'account_signup' %}">Register</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% if request.path == login_url %}active{% endif %}" aria-current="page" href="{% url 'account_login' %}">Login</a>
    </li>
    {% endif %}
```

Note: The URLs and views these link to are in the allauth.accounts app, so you don't have to create them.

3. From the terminal, check the location of your django-allauth package files on your computer. Copy the file path labelled Location:

You will need this in the next step.

```python
    pip3 show django-allauth
```

4. Copy the allauth template files to the projects templates directory using this terminal command where <Location> is the file path you copied in the previous step.

cp -r <Location>/allauth/templates/* ./templates/

Note: The route to your site package files may differ in your directory structure from the image. The path in the image is where the django-allauth files are located on the computer used when writing this topic.
