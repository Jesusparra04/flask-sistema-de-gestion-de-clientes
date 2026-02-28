# 🚀 Sistema de Gestión Empresarial - Flask

Aplicación web desarrollada con Flask para la gestión de empleados con sistema de autenticación de usuarios y conexión a base de datos MySQL.

Este proyecto está diseñado como demostración de arquitectura modular en Flask con separación de rutas, controladores y conexión a base de datos.

---

## 📌 Funcionalidades

- 🔐 Registro e inicio de sesión de usuarios
- 👥 Gestión CRUD de empleados
- 📷 Subida de imágenes de empleados
- 💾 Conexión a base de datos MySQL
- 🧩 Arquitectura modular (routers, controllers, conexión)
- 🎨 Interfaz responsiva

---

## 🛠 Tecnologías utilizadas

- Python
- Flask
- MySQL
- HTML5
- CSS3
- Bootstrap
- mysql-connector-python

---

## 🗄 Base de Datos

El archivo `app_empresa_bd.sql` se encuentra incluido en el proyecto.

### Pasos para importar:

1. Crear una base de datos en MySQL llamada: app_empresa_bd

2. Importar el archivo `app_empresa_bd.sql`.
3. Configurar las credenciales en el archivo `conexionBD.py`.

---

## ⚙ Instalación y ejecución

```bash
git clone https://github.com/Jesusparra04/flask-client-management-system.git
cd my-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
abrir en el navegador: http://127.0.0.1:5600/



auto: Jesús Parra
Backend Developer | Flask & Django