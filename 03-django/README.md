# Django

## About

Django is made up of separate `apps`. The idea is that one project brings many apps together. Therefore, you can reuse apps you've already made in other projects, making Django development very scalable.

It follows an MTV (Model Template View) model that is opinionated! It's high-level and requires you to follow a certain structure and set of rules - the Django way. 

### Benefits

It is:
- highly scalable
- secure
- full featured (has user auth, site maps, etc.)
- created for rapid development

### Used by:
- Disqus
- Instagram
- Pinterest
- NASA


## Resources
https://www.youtube.com/watch?v=D6esTdOLXh4

https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/


## Installation 

https://www.anaconda.com/download/#macos


## Instructions 

### Starting Our First Server

1. `conda install virtualenv` (prepend with `sudo` if you get a permissions error)

- https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/


2. `mkdir app`

3. `conda create -n venv` (where we can choose another word instead of `venv`)

4. `source activate venv` (to deactivate: `source deactivate`. to delete: `conda remove -n venv -all`)
  - or just `activate venv`

5. `conda install -n venv <package>`

6. `conda install django`

7. `django-admin startproject app`

8. `conda install mysqlclient`

9. Django will come with a SQLite db by default.

10. From app (at the same level as venv) `python manage.py runserver`  

### Database Connection to MySQL

11. Open *settings.py* in our /app folder and comment out the existing entry for DATABASES. 

12. We want to use something more robust than SQLite, so we'll replace it with MySQL.

13. Create a new DATABASE entry dictionary in the following format, and then create a new database in your MySQL Workbench.

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': YOUR_APP_NAME,
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': ''
    }
}


```

14. Run this command in your Anaconda shell in your /app directory,

`python manage.py migrate`

15. Start the server again and head to the `/admin` route. 

### Establishing a Super User

16. To create a super user: `python manage.py createsuperuser --username=<username> --email=<name@email.com>`
- create a password that you will remember. 

17. checkout `http://127.0.0.1:8000/admin`. Log in.

### Creating an App

18. run `python manage.py startapp <name>`

19. add your app in apps in `settings.py`:

```python
INSTALLED_APPS = [
    "<name>",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```
