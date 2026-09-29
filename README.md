# Blog Project — Módulo 1

Proyecto base de Django para iniciar un blog. Incluye el proyecto `blog_project` y la aplicación `posts`, registrada en la configuración.

## Requisitos

- Python 3.10 o superior (compatible con Django 5.2 LTS).
- Git.

## Clonar el repositorio

Cuando hayas creado el repositorio público en GitHub, reemplaza la URL y el nombre de carpeta por los tuyos:

```bash
git clone URL_DE_TU_REPOSITORIO
cd NOMBRE_DE_LA_CARPETA
```

## Crear y activar el entorno virtual

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

## Preparar la base de datos y ejecutar

```bash
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en el navegador. Para detener el servidor, presiona `Ctrl+C` en la terminal.

## Configuración incluida

- Aplicación `posts` registrada como `posts.apps.PostsConfig`.
- Idioma: `es-ar`.
- Zona horaria: `America/Argentina/Buenos_Aires`.
- SQLite para desarrollo local.

La clave secreta incluida es solo para desarrollo local. Antes de publicar una aplicación real, configura una clave privada mediante una variable de entorno y desactiva `DEBUG`.
