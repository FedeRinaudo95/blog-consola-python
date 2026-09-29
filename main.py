"""Punto de entrada: conecta el menú con el objeto Blog y la persistencia."""

from blog.datos import cargar_posts, guardar_posts, perfil_autor
from blog.menu import mostrar_menu
from blog.modelos import Blog
from blog.operaciones import mostrar_resultados
from blog.validaciones import validar_post


def ejecutar():
    """Carga los posts y ejecuta el menú hasta que el usuario sale."""
    blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            mostrar_resultados(blog.listar_posts())

        elif opcion == 2:
            termino = input("Buscar por titulo: ").strip()
            if not termino:
                print("La búsqueda no puede estar vacía.")
            else:
                mostrar_resultados(blog.buscar_por_titulo(termino))

        elif opcion == 3:
            tag = input("Ingresá el tag: ").strip()
            if not tag:
                print("El tag no puede estar vacío.")
            else:
                mostrar_resultados(blog.filtrar_por_tag(tag))

        elif opcion == 4:
            titulo = input("Título del post: ").strip()
            contenido = input("Contenido del post: ").strip()
            tags_texto = input("Tags separados por coma: ").strip()
            tags = [tag.strip() for tag in tags_texto.split(",") if tag.strip()]

            if not titulo or not contenido or not tags:
                print("No se creó el post: título, contenido y al menos un tag son obligatorios.")
                continue

            try:
                post = blog.crear_post(
                    titulo=titulo,
                    contenido=contenido,
                    autor=perfil_autor,
                    tags=tags,
                    estado="borrador",
                )
                print(f"Post creado: {post.titulo}")
            except ValueError as error:
                print(f"No se pudo crear el post: {error}")

        elif opcion == 5:
            print("\nResultado de la validación:")
            for numero, post in enumerate(blog.posts, start=1):
                resultado = validar_post(post)
                if resultado is True:
                    print(f"Post {numero}: válido")
                else:
                    print(f"Post {numero}: error - {resultado}")

        elif opcion == 6:
            if guardar_posts(blog.posts):
                print("Posts guardados en posts.json.")

        elif opcion == 7:
            # Guarda también los cambios al salir para conservar los posts nuevos.
            guardar_posts(blog.posts)
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    ejecutar()
