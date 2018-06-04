https://devcode.la/tutoriales/como-conectar-django-con-postgres-en-ubuntu/

# Instalar postgres en windows
https://www.openscg.com/bigsql/oscg_download/?file=packages/PostgreSQL-9.6.9-1-win64-bigsql.exe&user=${auth.authName} 

# Driver postgres
# Psycopg2
pip install psycopg2

#Configuración de Django
# mysite/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Ejemplo_DB',
        'USER': 'Ejemplo_Usuario',
        'PASSWORD': 'password_usuario',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

python manage.py migrate

