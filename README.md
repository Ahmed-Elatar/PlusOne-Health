# PlusOne-Health

PlusOne-Health - Project Setup Guide<br/>

Pre-requisites<br/>

Before you begin, ensure you have met the following requirements:
- python_version = "3.10" or latest
- Django = "4.2" or latest
- psycopg2 = "*"
- django rest-framework = "*"
- PostgreSQL = '16 
  
1-Install Dependencies :<br/>
- $ pip install django==4.2
- $ pip install psycopg2
- $ pip install djangorestframework
- $ apt install postgresql


2-Configure Database Settings <br/>
Open settings.py in your Django project directory and update the DATABASES setting to configure your PostgreSQL database. <br/>
Here’s an example configuration:
<br/><br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'your_database_name',<br/>
        'USER': 'your_database_user',<br/>
        'PASSWORD': 'your_database_password',<br/>
        'HOST': 'your_database_host',<br/>
        'PORT': 'your_database_port',<br/>
    }<br/>
}<br/>

<br/>

3-Run commands:<br/>
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
- $ pytohn3 manage.py runserver
- Your project should now be running at http://127.0.0.1:8000/

URL Map:
 - path('', index ,name="index"),
 - path('login/',For Login),
 - path('logout/',For Logout),
 - path('signup/',For singup),
 - path('post/<int:id>/', To get Post details),
 - path('profile/<int:id>/', To get certain Profile),
 - path('add-post/',To Add a Post),
 - path('post-delete/<int:id>',For delete a Post),#only if you a SuperUser or post Publisher
 - path('comment-delete/<int:id>',For delete a comment),#only if you a SuperUser or post Publisher


