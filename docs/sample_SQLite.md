# Proyecto Django: Todos

Este proyecto es un ejemplo de cómo crear una aplicación Django llamada "todos". En esta aplicación, crearemos un modelo llamado `Person` en la base de datos SQLite y guardaremos algunos datos de ejemplo.

## Requisitos

- Python 3
- Django (version 3.x o superior)

## Instalación

Antes de proceder, debes haber seguido los pasos de instalación de la aplicación "todos" explicados en:
- [Guía de Instalación](../README.md)

## Definición del Modelo `Person`

1. **Edita el archivo `models.py` de la aplicación "todos" y añade el siguiente código:**

    ```python
    from django.db import models

    class Person(models.Model):
        id_card = models.CharField(primary_key=True, max_length=9, null=False)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        age = models.IntegerField(default=18)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"
    ```

2. **Crea y aplica las migraciones para el modelo `Person`:**

    ```bash
    python manage.py makemigrations todos
    python manage.py migrate
    ```

## Añadir Datos de Ejemplo

1. **Abre el archivo `admin.py` de la aplicación "todos" y registra el modelo `Person`:**

    ```python
    from django.contrib import admin
    from .models import Person

    admin.site.register(Person)
    ```

2. **Crea un superusuario para acceder al panel de administración:**

    ```bash
    python manage.py createsuperuser
    ```

    Sigue las indicaciones para crear el superusuario.

3. **Corre el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

4. **Accede al panel de administración:**

    Ve a `http://127.0.0.1:8000/admin` e inicia sesión con el superusuario que acabas de crear.

5. **Añade datos de ejemplo desde la shell de Django:**

    ```bash
    python manage.py shell
    ```

    Una vez en la shell, añade los datos de ejemplo:

    ```python
    from todos.models import Person

    Person.objects.create(
        id_card='123456A',
        first_name='Pedro',
        last_name='García',
        age=22
    )
    ```

6. **Verifica que los datos se han añadido correctamente:**

    Ve a `http://127.0.0.1:8000/admin/todos/person/` para ver los registros de `Person` en el panel de administración.

## Conclusión

Has creado exitosamente una aplicación Django llamada "todos", definido un modelo `Person` en la base de datos SQLite, y añadido datos de ejemplo. Este proyecto sirve como base para cualquier desarrollo futuro que desees realizar con Django.

