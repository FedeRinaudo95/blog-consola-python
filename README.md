# Blog de consola con POO y persistencia JSON

Este proyecto permite listar publicaciones, buscarlas por título, filtrarlas por etiqueta, crear posts y validar su información. Los posts se cargan y guardan en `posts.json`.

## Cómo ejecutar

Desde la carpeta raíz del proyecto, ejecutá:

```bash
python main.py
```

Si tu sistema usa el comando `python3`, ejecutá `python3 main.py`.

## Opciones del menú

1. Ver todos los posts.
2. Buscar por título (no distingue mayúsculas y minúsculas).
3. Filtrar por tag (no distingue mayúsculas y minúsculas).
4. Crear un post; se asigna como autor el perfil de Federico.
5. Validar los posts.
6. Guardar los posts en JSON.
7. Salir; guarda automáticamente los cambios.

El tercer post de ejemplo tiene el contenido vacío intencionalmente para que la validación informe un error.

## Clases principales

- `Autor`: contiene el nombre, la bio, la especialidad y las redes sociales.
- `Post`: representa una publicación y contiene una instancia de `Autor`.
- `Blog`: mantiene una lista de objetos `Post` y ofrece métodos para listar, buscar, filtrar, crear y validar publicaciones.

## Organización de archivos

- `main.py`: punto de entrada; crea el objeto `Blog` y conecta el menú con las operaciones.
- `posts.json`: datos persistidos en formato JSON.
- `blog/__init__.py`: identifica `blog` como paquete.
- `blog/modelos.py`: clases `Autor`, `Post` y `Blog`.
- `blog/datos.py`: carga JSON y convierte diccionarios en objetos; guarda objetos convertidos en diccionarios.
- `blog/menu.py`: muestra opciones y procesa la entrada del menú.
- `blog/operaciones.py`: presenta los resultados de búsqueda y filtrado.
- `blog/validaciones.py`: verifica los campos y tipos de los posts.

## Persistencia

Al iniciar, `blog/datos.py` lee `posts.json` y reconstruye objetos `Post` y `Autor`. Al guardar, convierte cada objeto a un diccionario y usa el módulo estándar `json` para escribirlo.

Si el archivo no existe, está vacío o contiene JSON inválido, el programa muestra un mensaje y carga los posts de ejemplo. Podés crear posts desde el menú y guardarlos con la opción 6; la opción 7 también los guarda antes de salir.

## Cambios respecto al checkpoint anterior

El sistema ahora usa clases y objetos en lugar de manejar cada publicación como un diccionario durante su funcionamiento. También guarda y recupera publicaciones mediante JSON para conservar los cambios entre ejecuciones.
