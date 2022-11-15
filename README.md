## INF601 - Advanced Programming in Python
James Kobell |
 Mini Project 4
 
 ### Project
 Mini Project 4 is a Django project with a default Admin app, and 1 added app named Charts which has an alias name of Financial Ticker. Users must first register, and then login before having access to data. After login, a user can view details about each Exchange, Currency or Timezone selected. A modal notifies user of a successful logout. Styles are Bootstrap 5.

### Interpreter
Python 3.10.6

### Framework
- Django 4.1.2
- sqlite local database [default]
- Bootstrap 5 styles - CDN

### Installation [Windows]
- Create a directory for the project.
- Download ZIP of project and extract into newly created project directory. 
- Install Python 3.10.6 if not already installed.
- Create and activate a virtual environment.
- Refer to requirements.txt and pip install the listed packages.
- Update each package.

### Project Creation
- In Terminal, run command: django-admin startproject fin_ticker
- In Terminal, run command: python manage.py migrate

### Create SQLite Database
- In Terminal, run command: CREATE DATABASE Charts
- In Terminal, run command: python manage.py migrate

### Create Charts App
- In Terminal, run command: python manage.py startapp charts
- In Terminal, run command: python manage.py makemigrations charts 
- In Terminal, run command: python manage.py migrate

### Create SuperUser
- In Terminal, run command: python manage.py createsuperuser
- Follow prompts to enter; username, email address, password

### Start Project
- In Terminal, run command: python manage.py

### Load Database
- In browser, navigate to URL, http://127.0.0.1:8000/admin [for admin app]
- Login with superuser credentials.
- Add desired records to each database table.

### Running Project
- In browser, navigate to URL, http://127.0.0.1:8000/charts [for Charts app] 
- At http://127.0.0.1:8000/charts, register as a user
- Login as registered user
- Select from links; Exchanges, Currencies, Tickers
- Select each item to view details for selected item.
- Logout 

### Help
- Refer to Django tutorial at https://docs.djangoproject.com/en/4.1/intro/
- Refer to Django documentation at https://docs.djangoproject.com/en/4.1/

### Contributing
- Please open an issue to initiate a change process.