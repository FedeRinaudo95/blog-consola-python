"""Funciones auxiliares de presentación de resultados."""


def mostrar_resultados(posts):
    """Muestra los posts devueltos por una búsqueda o filtro."""
    if not posts:
        print("No se encontraron resultados.")
        return

    print("\nResultados:")
    for post in posts:
        print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")
