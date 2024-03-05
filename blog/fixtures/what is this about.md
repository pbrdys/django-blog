# Adding data to database via json

1. Create directory named **fixtures**
2. Create file named **posts.json**
3. Fill json file with data
4. Now load the data to the database table using the fixture name of posts. 
Django knows where to look for the file, as it is stored in the fixtures directory by default, e.g. blog/fixtures/posts.json
    ```python
        python3 manage.py loaddata posts
    ```
5. Add blog/fixtures/ to the .gitignore file.
Note: You can keep the directory locally, as this technique will be helpful in the future if you run into database errors.