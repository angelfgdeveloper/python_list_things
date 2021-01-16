# Paso 5
instructions = [
    "SET FOREIGN_KEY_CHECKS=0;",
    "DROP TABLE IF EXISTS todo;",
    "DROP TABLE IF EXISTS user;",
    "SET FOREIGN_KEY_CHECKS=1;",
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )
    """,
    """
        CREATE TABLE todo (
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        )
    """
]

# Paso 6
# AGREGARLOS A LA BASE DE DATOS
# set FLASK_APP=todo
# set FLASK_ENV=development
# set FLASK_DATABASE_HOST=localhost
# set FLASK_DATABASE_PASSWORD=
# set FLASK_DATABASE_USER=
# set FLASK_DATABASE=

# Paso 7.1
# flask init-db