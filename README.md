# 🎓 Sistema de Gestión de Estudiantes

Este es un script interactivo en Python diseñado para administrar registros de estudiantes mediante operaciones **CRUD** (Crear, Leer, Actualizar, Borrar) y persistencia de datos en archivos **JSON**.

## 🚀 Funcionalidades

El sistema permite realizar las siguientes acciones a través de un menú interactivo:

1.  **Registro de Estudiantes**: Captura nombre, ID (10 dígitos), edad, clase y estado de actividad.
2.  **Visualización**: Muestra una lista numerada de todos los estudiantes registrados.
3.  **Búsqueda**: Permite localizar estudiantes por su **Nombre** o por su **ID**.
4.  **Actualización**: Modifica el estado de actividad (Activo/Inactivo) de un estudiante existente.
5.  **Eliminación**: Borra el registro de un estudiante mediante su ID, con confirmación de seguridad.
6.  **Persistencia (JSON)**:
    *   **Guardar**: Exporta los datos actuales a un archivo `.json`.
    *   **Cargar**: Importa datos desde un archivo `.json` existente.

## 🛠️ Estructura de Datos

Los datos se almacenan en un diccionario donde la **llave** es el ID del estudiante y el **valor** es un objeto con su información:

```json
{
    "1234567890": {
        "name": "juan perez",
        "age": "20",
        "class": "matemáticas",
        "is active?": true
    }
}
