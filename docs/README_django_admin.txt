# Python 3.6.5 + Django 1.11
#Admin

#crear un usuario que pueda iniciar sesión en el sitio administrativo
python manage.py createsuperuser

#Matricular para que aparezcan en las operciones CRUD en el admin
polls/admin.py
from .models import Question
admin.site.register(Question)