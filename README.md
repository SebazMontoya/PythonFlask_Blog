# Flask Blog

Este es un proyecto de blog desarrollado con Flask, un microframework de Python. El objetivo de este proyecto es proporcionar una plataforma básica para publicar y gestionar entradas de blog.

## Características

- Sistema de autenticación de usuarios (registro e inicio de sesión).
- Creación, edición y eliminación de publicaciones.
- Diseño responsivo utilizando Bootstrap.
- Base de datos gestionada con SQLAlchemy.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/flask-blog.git
    cd flask-blog
    ```

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura la base de datos:

    ```bash
    flask db init
    flask db migrate -m "Inicialización de la base de datos"
    flask db upgrade
    ```

5. Ejecuta la aplicación:

    ```bash
    flask run
    ```

6. Abre tu navegador y visita `http://127.0.0.1:5000`.

## Estructura del Proyecto

```
Flask-Blog/
│
├── app/
│   ├── static/         # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/      # Plantillas HTML
│   ├── models.py       # Modelos de la base de datos
│   ├── routes.py       # Rutas de la aplicación
│   └── __init__.py     # Inicialización de la aplicación
│
├── migrations/         # Migraciones de la base de datos
├── venv/               # Entorno virtual (opcional)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto
```

