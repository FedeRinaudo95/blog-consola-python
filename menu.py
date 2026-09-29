"""Menú e ingreso de opciones por consola."""


def mostrar_menu():
    """Muestra el menú y devuelve la opción como número entero."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    try:
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Ingresá un número del menú.")
        return None
