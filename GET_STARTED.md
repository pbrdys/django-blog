
![Creating-Repo, Installing packages, Creating Django Project, Creating Django App, Creating Views, Creating Urls, settings.py](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/16383559f48c4ae4a69e9e9149914729/d5d0251c90ab4dc5b7fc81bb7ac368d2)

# Documentation on creating an Django Project:

## Install Django Package:
```python
    pip3 install Django~=4.2.1
```
### Check Installed Django Version:
```python
    django-admin version
```
### Show installed packages in general:
```python
    pip3 list
```

## Add Installed Packages to requirements.txt
```python
    pip3 freeze --local > requirements.txt
```

## Create Django Project:
```python
    django-admin startproject project_name .
```
The . at the end says that the project is being insalled in the current directory!!!

## CREATE DJANGO APP:
```python
    python3 manage.py startapp app_name
```

## APP/views.py - ADD:
```python
    from django.http import HttpResponse

    def index(request):
        return HttpResponse
```

## PROJECT/urls.py - Add the created VIEW. 
```python
    from app_name import views as alias_view_name
    urlpatterns = [path('', alias_view_name.index, name='index')]
```

## ADD APP to settings.py to connect the app to the project. 
Append 'app_name', to the end of the list of **INSTALLED_APPS** within settings.py

## RUN DJANGO SERVER:
```python
    python3 manage.py runserver
```

## IMPORTANT PROJECT FILES:
* settings.py 
    this file contains the project-wide settings, 
    such as installed apps and database connection information, among other things
* manage.py
     this file is in the root directory, above the project folder. 
     It is used to create apps, run our project and perform some database operations.


![Deployment-Process on Heroku](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/16383559f48c4ae4a69e9e9149914729/00d6fcc7568c48dea6eb2f89ee0d0a3a)

# DEPLOYMENT PROCESS:
* Create Heroku App (Dashboard)
* Settings -> Config Vars:
```python
    Add the KEY "DISABLE_COLLECTSTATIC" with the VALUE of "1"
```
* Install a production-ready webserver for Heroku.
```python
    pip3 install gunicorn~=20.1
```
* Add gunicorn==20.1.0 to the requirements.txt file
```python
    pip3 freeze --local > requirements.txt
```
5. Create a file named "Procfile" at the root directory of the project (same directory as requirements.txt).
6. In the Procfile, declare this is a web process followed by the command to execute your Django project.
    web: gunicorn my_project.wsgi
This assumes your project is named my_project.
Note: gunicorn my_project.wsgi is the command heroku will use to start the server. 
It works similarly to python3 manage.py runserver.
7. Open the my_project/settings.py file and replace DEBUG=True with DEBUG=False.
8. Also, in settings.py we need to append the Heroku hostname to the ALLOWED_HOSTS list, in addition to the local host we added in the last lesson.
    ,'.herokuapp.com'
9. You can now git add the files you have modified, git commit them and push them to GitHub. 


## Create User Stories:
[Create User Stories](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/4565659a34d648b8b8edd063c3182180/)