"""Archivo principal: coordina el menú y las operaciones del blog."""

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import (
    buscar_por_titulo,
    filtrar_por_tag,
    listar_posts,
    mostrar_resultados,
)
from blog.validaciones import validar_post


def ejecutar_sistema():
    """Mantiene activo el programa hasta que se elige salir."""
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Buscar por titulo: ").strip()
            if not termino:
                print("La búsqueda no puede estar vacía.")
            else:
                resultados = buscar_por_titulo(posts, termino)
                mostrar_resultados(resultados)

        elif opcion == 3:
            tag = input("Ingresá el tag: ").strip()
            if not tag:
                print("El tag no puede estar vacío.")
            else:
                resultados = filtrar_por_tag(posts, tag)
                mostrar_resultados(resultados)

        elif opcion == 4:
            print("\nResultado de la validación:")
            for numero, post in enumerate(posts, start=1):
                resultado = validar_post(post)
                if resultado is True:
                    print(f"Post {numero}: válido")
                else:
                    print(f"Post {numero}: error - {resultado}")

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    ejecutar_sistema()
