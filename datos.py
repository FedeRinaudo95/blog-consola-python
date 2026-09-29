"""Carga y guarda objetos Post usando el archivo posts.json."""

import json
from pathlib import Path

from blog.modelos import Autor, Post

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
ARCHIVO_POSTS = RUTA_PROYECTO / "posts.json"

perfil_autor = Autor(
    nombre="Federico",
    bio="Comparto mis avances aprendiendo programación.",
    especialidad="Python",
    redes_sociales=["@federico_python", "@federico_dev"],
)


def posts_iniciales():
    """Devuelve datos de ejemplo si todavía no hay un JSON utilizable."""
    autor = Autor(
        nombre=perfil_autor.nombre,
        bio=perfil_autor.bio,
        especialidad=perfil_autor.especialidad,
        redes_sociales=list(perfil_autor.redes_sociales),
    )
    return [
        Post(
            id=1,
            titulo="Mis primeros pasos con Python",
            contenido="Una introducción a los primeros conceptos de Python.",
            autor=autor,
            tags=["Python", "Principiantes"],
            estado="publicado",
        ),
        Post(
            id=2,
            titulo="Qué es Django y para qué sirve",
            contenido="Django es un framework web desarrollado con Python.",
            autor=autor,
            tags=["Python", "Django", "Web"],
            estado="borrador",
        ),
        Post(
            id=3,
            titulo="Organizando datos con diccionarios",
            contenido="",
            autor=autor,
            tags=["Python", "Diccionarios"],
            estado="archivado",
        ),
    ]


def cargar_posts(ruta=ARCHIVO_POSTS):
    """Carga registros JSON y los reconstruye como objetos Post."""
    archivo = Path(ruta)
    if not archivo.exists():
        print("No se encontró posts.json. Se cargarán posts de ejemplo.")
        return posts_iniciales()

    try:
        contenido = archivo.read_text(encoding="utf-8")
        if not contenido.strip():
            print("posts.json está vacío. Se cargarán posts de ejemplo.")
            return posts_iniciales()

        datos = json.loads(contenido)
        if not isinstance(datos, list):
            print("posts.json debe contener una lista. Se cargarán posts de ejemplo.")
            return posts_iniciales()

        posts = []
        for numero, registro in enumerate(datos, start=1):
            try:
                posts.append(Post.from_dict(registro))
            except (TypeError, ValueError) as error:
                print(f"Se omitió el registro {numero}: {error}")

        return posts if posts else posts_iniciales()

    except (OSError, json.JSONDecodeError) as error:
        print(f"No se pudo leer posts.json ({error}). Se cargarán posts de ejemplo.")
        return posts_iniciales()


def guardar_posts(posts, ruta=ARCHIVO_POSTS):
    """Serializa los objetos Post a diccionarios y los guarda como JSON."""
    archivo = Path(ruta)
    try:
        archivo.parent.mkdir(parents=True, exist_ok=True)
        datos = [post.to_dict() for post in posts]
        archivo.write_text(
            json.dumps(datos, ensure_ascii=False, indent=4),
            encoding="utf-8",
        )
        return True
    except (OSError, TypeError, ValueError) as error:
        print(f"No se pudieron guardar los posts en JSON: {error}")
        return False
