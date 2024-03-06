# BASE TEMPLATE

## Prepare the project for multiple template directories
1. In **codestar/settings.py**, create a TEMPLATES_DIR constant to build a path for our subdirectory 'templates'.
    ```python
        TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    ```

2. Scroll down in the **codestar/settings.py** file to TEMPLATES and add your newly created TEMPLATES_DIR constant to the list of 'DIRS'.
    ```python
        'DIRS': [TEMPLATES_DIR],
    ```

3. Add a new top-level templates directory.
**/workspace/django-blog/templates**


* Open the codestar/settings.py file and build a path for our subdirectory static so we can link to files in the static directory from a template. 
**STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]**

* Open the base.html file and load the static directory from the first line of the file.
**{% load static %}**



## Template Inheritance:
The base.html file contains the header and footer, but the index.html file is where the code to display the list of blog posts appears.
In base.html, we have the following code:

    {% block content %}
        <!-- Content Goes here -->
    {% endblock content %}

Here, we define a block. Our base.html file is a skeleton HTML document. It's the job of the child templates to fill these blocks with content.
In index.html, we have two bits of code that link it back to base.html.

    {% extends "base.html" %}
    {% block content %}

    <!-- index.html content starts here -->
    …
    <!-- index.html content ends here -->
    {% endblock %}

First, we have an extends tag. This tells index.html that it is a child template of base.html. Then, everything we have inside our block fills the corresponding blocks in base.html, giving us a fully rendered web page.


### Fining our templates
Finding our templates

How does Django know where to find the templates?

1. That is controlled by the TEMPLATES setting in settings.py.
    * The DIRS key tells Django which directories to look in. This is a Python list, so we add the TEMPLATES_DIR variable, which was set at the top of settings.py.
    * The TEMPLATES setting also has APP_DIRS set to True, which means that Django will also look for a templates directory inside all our app directories.

2. Finally, in our project, we set TEMPLATES_DIR value to the templates directory in our base, or top-level directory.


### Bits about blocks

All the block and endblock tags do is tell Django's templating engine that a child template may fill them with content.

{% block content %}
    <!-- Content Goes here -->
{% endblock content %}

As you can see, blocks are also named. In this project, we named our block content because, not surprisingly, our page content goes into it. We can give blocks any name we like, and a template may contain several blocks that a child template may or may not fill. For example, we could have a block called sidebar that the child template could use to populate a side navigation bar, if one existed.

In our project, we will only have one block named content, but feel free to add more blocks with different names to your own projects.


### Loading more than one block

If you have more than one block in your base template, you don't need to create separate files for each of them. In the sidebar example above, we would put both the content and the sidebar in our index.html file. When index.html is loaded, Django will only populate the blocks that exist in the child template; otherwise, the block will be left empty.

If you wanted, you could also put some default content inside the block in your base template. If the child template chooses to populate that block, then the default content would then be overwritten.

For example, you could add this to base.html:

{% block content %}
    <p>This is my default paragraph</p>
{% endblock content %}

