# Sistema de blog por consola

Este programa permite consultar publicaciones de un blog desde un menú interactivo. Se pueden listar posts, buscar por título, filtrar por etiqueta y validar que cada publicación tenga la estructura requerida.

## Cómo ejecutarlo

Desde la carpeta raíz `blog_consola`, abrí una terminal y ejecutá:

```bash
python main.py
```

En algunos equipos también puede ser necesario usar `python3 main.py`.

## Opciones del menú

1. Ver todos los posts.
2. Buscar por título, sin distinguir mayúsculas y minúsculas.
3. Filtrar por tag, sin distinguir mayúsculas y minúsculas.
4. Validar los posts e informar errores de estructura.
5. Salir del sistema.

El tercer post está incompleto intencionalmente: le falta la clave `contenido`, para que la opción de validación permita comprobar que se detectan datos faltantes.

## Organización del proyecto

- `main.py`: inicia el sistema y coordina el menú con las funciones.
- `blog/__init__.py`: identifica `blog` como un paquete de Python.
- `blog/datos.py`: contiene el perfil del autor, los estados, las etiquetas y los posts.
- `blog/menu.py`: muestra el menú y captura la opción.
- `blog/operaciones.py`: lista, busca y filtra publicaciones.
- `blog/validaciones.py`: revisa la estructura de cada post.
