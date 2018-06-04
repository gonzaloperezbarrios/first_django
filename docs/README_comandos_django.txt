# Python 3.6.5 + Django 1.11

#Crear un proyecto base
django-admin startproject mysite

#Correr el servidor de desarrollo
python manage.py runserver

#Cambiar el puertodel servidor de desarrollo
python manage.py runserver 7070

#Revesar los modelos a la base de datos
python manage.py migrate

#Preparar la migración del modelo (polls)
python manage.py makemigrations polls

#Ver script sql antes de lanzar la migración
python manage.py sqlmigrate polls 001
	polls->polls/apps.py
	001-> polls/migrations/0001_initial.py

#Revisar posibles problemas en la emigración
python manage.py check

#Shell interactivo de Python + Django 
python manage.py shell

#Ejecutar pruebas
python manage.py test polls