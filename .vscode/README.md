# Automatización de Comandos al Abrir VS Code

Para ejecutar comandos automáticamente al abrir Visual Studio Code en este repositorio, puedes usar un archivo `tasks.json` o configurar un script en el archivo `settings.json` del espacio de trabajo. Aquí te explico cómo hacerlo:

## 1. Usar un archivo `tasks.json`

Puedes configurar tareas automáticas en VS Code utilizando el archivo `tasks.json`:

1. Crea una carpeta llamada `.vscode` en la raíz de tu proyecto (si no existe).
2. Dentro de esa carpeta, crea un archivo llamado `tasks.json`.
3. Configura el archivo para ejecutar el comando deseado. Por ejemplo, para iniciar el servidor FastAPI automáticamente:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run FastAPI Server",
            "type": "shell",
            "command": "uvicorn main:app --reload",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": [],
            "detail": "Tarea para iniciar el servidor FastAPI automáticamente."
        }
    ]
}
```

Cuando abras el proyecto, puedes ejecutar esta tarea presionando `Ctrl+Shift+B` (o configurarla para que se ejecute automáticamente con extensiones adicionales).

## 2. Usar un archivo `settings.json` del espacio de trabajo

Si quieres ejecutar comandos automáticamente al abrir el proyecto, puedes usar la extensión **Run on Folder Open** o configurar un script en el archivo `settings.json`:

1. Crea o edita el archivo `.vscode/settings.json` en tu proyecto.
2. Configura un script para ejecutarse al abrir el proyecto. Ejemplo:

```json
{
    "runOnOpen.commands": [
        {
            "command": "uvicorn main:app --reload",
            "cwd": "${workspaceFolder}",
            "name": "Start FastAPI Server"
        }
    ]
}
```

> **Nota:** Instala la extensión **Run on Folder Open** desde el marketplace de VS Code para que esta configuración funcione.

## 3. Usar un script de inicialización

Si prefieres un enfoque más general, puedes crear un script de inicialización en Python o Bash que se ejecute al abrir el proyecto:

- Crea un archivo `start.sh` (Linux/Mac) o `start.bat` (Windows) con el comando para iniciar el servidor.
- Ejecútalo manualmente o configúralo como parte de las tareas de VS Code.
