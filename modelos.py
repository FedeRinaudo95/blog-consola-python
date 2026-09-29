"""Clases que representan el autor, las publicaciones y el blog."""

from dataclasses import dataclass, field
from typing import Any

from blog.validaciones import validar_post


@dataclass
class Autor:
    """Representa a una persona autora del blog."""

    nombre: Any
    bio: Any = ""
    especialidad: Any = ""
    redes_sociales: Any = field(default_factory=list)

    def to_dict(self):
        """Convierte el autor en un diccionario serializable como JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
        }

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye un autor desde un diccionario."""
        if not isinstance(datos, dict):
            return None
        return cls(
            nombre=datos.get("nombre", ""),
            bio=datos.get("bio", ""),
            especialidad=datos.get("especialidad", ""),
            redes_sociales=datos.get("redes_sociales", []),
        )


@dataclass
class Post:
    """Representa una publicación; autor debe ser un objeto Autor."""

    id: Any
    titulo: Any
    contenido: Any
    autor: Any
    tags: Any = field(default_factory=list)
    estado: Any = "borrador"

    def to_dict(self):
        """Convierte el post y su autor anidado a diccionarios."""
        autor_dict = self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": autor_dict,
            "tags": self.tags,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye un post desde un diccionario leído de JSON."""
        if not isinstance(datos, dict):
            raise ValueError("el registro del post no es un diccionario")

        return cls(
            id=datos.get("id"),
            titulo=datos.get("titulo", ""),
            contenido=datos.get("contenido", ""),
            autor=Autor.from_dict(datos.get("autor")),
            tags=datos.get("tags", []),
            estado=datos.get("estado", ""),
        )


@dataclass
class Blog:
    """Centraliza la colección de posts y sus operaciones."""

    posts: list = field(default_factory=list)

    def listar_posts(self):
        """Devuelve la lista actual de objetos Post."""
        return list(self.posts)

    def buscar_por_titulo(self, termino):
        """Busca posts por fragmento de título, sin distinguir mayúsculas."""
        termino = termino.strip().lower()
        if not termino:
            return []
        return [
            post for post in self.posts
            if isinstance(post.titulo, str) and termino in post.titulo.lower()
        ]

    def filtrar_por_tag(self, tag):
        """Filtra posts por tag, sin distinguir mayúsculas."""
        tag = tag.strip().lower()
        if not tag:
            return []
        return [
            post for post in self.posts
            if isinstance(post.tags, list)
            and any(isinstance(item, str) and item.lower() == tag for item in post.tags)
        ]

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador"):
        """Crea y agrega un Post nuevo con un id consecutivo."""
        if not isinstance(autor, Autor):
            raise ValueError("el autor debe ser una instancia de Autor")
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("el título no puede estar vacío")
        if not isinstance(contenido, str) or not contenido.strip():
            raise ValueError("el contenido no puede estar vacío")
        if not isinstance(tags, list) or not tags:
            raise ValueError("se requiere al menos un tag")

        ids = [
            post.id for post in self.posts
            if isinstance(post.id, int) and not isinstance(post.id, bool)
        ]
        nuevo_id = max(ids, default=0) + 1
        post = Post(
            id=nuevo_id,
            titulo=titulo.strip(),
            contenido=contenido.strip(),
            autor=autor,
            tags=[tag.strip() for tag in tags if isinstance(tag, str) and tag.strip()],
            estado=estado,
        )
        resultado = validar_post(post)
        if resultado is not True:
            raise ValueError(resultado)
        self.posts.append(post)
        return post

    def validar_posts(self):
        """Devuelve pares de (post, resultado de validación)."""
        return [(post, validar_post(post)) for post in self.posts]
