"""Reglas de validación de los objetos Post."""

ESTADOS_POST = ("borrador", "publicado", "archivado")


def validar_post(post):
    """Retorna True si el post es válido o un mensaje que describe el error."""
    from blog.modelos import Autor, Post

    if not isinstance(post, Post):
        return "el post no es un objeto Post"

    if isinstance(post.id, bool) or not isinstance(post.id, int) or post.id <= 0:
        return "el id debe ser un entero positivo"

    if not isinstance(post.titulo, str) or not post.titulo.strip():
        return "el título está vacío o no es texto"

    if not isinstance(post.contenido, str) or not post.contenido.strip():
        return "el contenido está vacío o no es texto"

    if not isinstance(post.autor, Autor):
        return "el autor no es un objeto Autor"

    if not isinstance(post.autor.nombre, str) or not post.autor.nombre.strip():
        return "falta el nombre del autor o está vacío"

    if not isinstance(post.tags, list):
        return "tags no es una lista"

    if any(not isinstance(tag, str) or not tag.strip() for tag in post.tags):
        return "los tags deben ser textos no vacíos"

    if post.estado not in ESTADOS_POST:
        return "el estado no es válido"

    return True
