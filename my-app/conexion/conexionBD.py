import mysql.connector
import os


def connectionBD():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=os.getenv("DB_USER", "tu_usuario"),
            passwd=os.getenv("DB_PASSWORD", "tu_password"),
            database="app_empresa_bd",
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True
        )

        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")