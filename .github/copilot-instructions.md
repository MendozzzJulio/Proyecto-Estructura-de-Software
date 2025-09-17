# Copilot Instructions for AI Agents

## Arquitectura general
- El proyecto es una agenda de contactos en Python, orientada a consola, con estructura modular.
- Los componentes principales son:
  - `contacto.py`: Define la clase `Contacto` con atributos y métodos para gestionar la información de cada contacto.
  - `agenda_contactos.py`: Implementa la clase `AgendaContactos`, que gestiona una colección de contactos y operaciones CRUD (agregar, buscar, actualizar, eliminar, guardar/cargar).
  - `interfaz_consola.py`: Proporciona la interfaz de usuario por consola, maneja el menú y la interacción con el usuario.
  - `main.py`: Punto de entrada, inicializa la interfaz y ejecuta la aplicación.

## Flujos y convenciones clave
- El flujo principal inicia en `main.py`, que crea una instancia de `InterfazConsola` y llama a `ejecutar()`.
- Los datos de contactos se almacenan en un archivo JSON (`contactos.json`), gestionado por `AgendaContactos`.
- Las búsquedas y actualizaciones se realizan por nombre, teléfono o email.
- Los métodos de cada clase están documentados con docstrings en español.
- Los nombres de variables y métodos siguen el estilo snake_case.
- Los mensajes y prompts al usuario están en español.
- El menú de la consola está definido en `InterfazConsola.mostrar_menu()`.

## Prácticas y patrones específicos
- No hay dependencias externas ni frameworks; todo es Python estándar.
- Los archivos de caché (`__pycache__`) pueden ignorarse.
- No existe un sistema de pruebas automatizadas ni scripts de build; la ejecución es directa desde `main.py`.
- Para depuración, agregar prints en los métodos relevantes.
- Los datos persistentes se guardan automáticamente al salir si el usuario lo confirma.

## Ejemplo de uso
```bash
python Agenda de contactos/proyectoEstructura/main.py
```

## Recomendaciones para agentes
- Mantener la modularidad: agregar nuevas funcionalidades en archivos/clases separados si es posible.
- Seguir el idioma español para mensajes y documentación.
- Si se agregan nuevas operaciones, actualizar el menú en `InterfazConsola` y la lógica en `AgendaContactos`.
- Documentar cualquier convención nueva en este archivo.

## Referencias
- Ver `README.md` para el propósito general.
- Revisar los archivos en `Agenda de contactos/proyectoEstructura/` para ejemplos de patrones y estructura.
