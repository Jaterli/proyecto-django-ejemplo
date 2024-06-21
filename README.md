
# Primer proyecto django (ejemplo de creación)

El siguiente método te permite crear un proyecto Django desde cero en tu máquina local sin necesidad de clonarlo desde un repositorio remoto. 
Es útil especialmente si estás comenzando un proyecto nuevo y quieres configurarlo según tus propias necesidades desde el principio.
Cómo ejemplo, se ha creado una aplicación ejemplo llamada "todos" que dejaremos en su versión inicial.
También, como prueba, se ha creado una función y se ha configurado una URL a través de la que se ejecutará dicha función.

## Requisitos

- Python 3.10 o superior
- pip
- virtualenv

### Paso 1: Crear una nueva carpeta para el proyecto

1. **Abre tu terminal o línea de comandos:**

   Dependiendo de tu sistema operativo, abre una terminal o línea de comandos. Puedes usar Terminal en macOS/Linux o Command Prompt en Windows.

2. **Crea una nueva carpeta para el proyecto:**

   ```bash
   mkdir conquermanager
   cd conquermanager
   ```

### Paso 2: Inicializar un entorno virtual

1. **Crea un entorno virtual para el proyecto:**

   ```bash
   # Utilizando venv en Python 3
   python3 -m venv env

   # Activar el entorno virtual en macOS/Linux
   source env/bin/activate

   # Activar el entorno virtual en Windows
   env\Scripts\activate
   ```

   Esto creará un entorno virtual llamado `env` en la carpeta del proyecto y lo activará.

### Paso 3: Instalar Django y crear un proyecto

1. **Instala Django dentro del entorno virtual:**

   Asegúrate de que estás en el entorno virtual (`env` activado) y luego instala Django:

   ```bash
   pip install django
   ```

2. **Crea un nuevo proyecto Django llamado "conquermanager":**

   ```bash
   django-admin startproject conquermanager .
   ```

   Esto creará una estructura básica de proyecto Django en la carpeta actual (`.`) con el nombre `conquermanager`.

### Paso 4: Configuración inicial del proyecto

1. **Configura la base de datos (opcional):**

   Si necesitas configurar una base de datos diferente a SQLite o realizar ajustes en `settings.py`, puedes hacerlo ahora.

2. **Crea una nueva aplicación dentro del proyecto:**

   ```bash
   python manage.py startapp todos
   ```

   Esto creará una nueva aplicación llamada `todos` dentro del proyecto.

### Paso 5: Configuración de urls y vistas

1. **Define una vista de prueba en `views.py` dentro de la aplicación `todos`:**

   Abre el archivo `todos/views.py` y agrega una vista de prueba:

   ```python
   from django.http import HttpResponse

   def helloworld(request):
       return HttpResponse("Hola, esto es una prueba")
   ```
2. **Añade la aplicación `todos` al archivo `conquermanager/settings.py`:**

   Abre el archivo `conquermanager/settings.py` y agregalo al array  `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'todos',
   ]
   ```

3. **Configura la URL para la vista de prueba:**

   Abre el archivo `conquermanager/urls.py` y configura la URL para la vista `helloworld`:

   ```python
   from django.contrib import admin
   from django.urls import path
   from todos.views import helloworld

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('saludo/', helloworld),
   ]
   ```

### Paso 6: Ejecutar el servidor de desarrollo

1. **Ejecuta el servidor de desarrollo de Django:**

   Asegúrate de estar en la carpeta donde está gestionado tu proyecto Django (`manage.py` debe estar presente) y ejecuta:

   ```bash
   python manage.py runserver
   ```

2. **Abre tu navegador y prueba la vista de prueba:**

   Abre tu navegador web y visita `http://127.0.0.1:8000/saludo/`. Deberías ver el mensaje "Hola, esto es una prueba".

### Notas adicionales

- A medida que continúes desarrollando el proyecto, puedes agregar más aplicaciones, modelos, vistas y plantillas según sea necesario.
- No olvides desactivar el entorno virtual cuando hayas terminado de trabajar en tu proyecto:

  ```bash
  deactivate
  ```


