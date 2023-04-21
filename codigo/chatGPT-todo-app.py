'''
A continuación se muestra un ejemplo de código Python que implementa una aplicación to-do con interfaz de usuario Tkinter y base de datos SQLite:
'''
import sqlite3
from tkinter import *

# Establecer la conexión con la base de datos
db_conn = sqlite3.connect('mi_bd.db')
cursor = db_conn.cursor()

# Crear la tabla de tareas si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT,
        completada INTEGER
    )
''')
db_conn.commit()

# Función para añadir una tarea a la base de datos
def add_task():
    descripcion = task_input.get()
    if descripcion:
        cursor.execute('''
            INSERT INTO tareas (descripcion, completada) VALUES (?, 0)
        ''', (descripcion,))
        db_conn.commit()
        task_input.delete(0, END)
        show_tasks()

# Función para editar una tarea existente en la base de datos
def edit_task(task_id):
    descripcion = task_input.get()
    if descripcion:
        cursor.execute('''
            UPDATE tareas SET descripcion = ? WHERE id = ?
        ''', (descripcion, task_id))
        db_conn.commit()
        task_input.delete(0, END)
        show_tasks()

# Función para marcar una tarea como completada en la base de datos
def complete_task(task_id):
    cursor.execute('''
        UPDATE tareas SET completada = 1 WHERE id = ?
    ''', (task_id,))
    db_conn.commit()
    show_tasks()

# Función para borrar una tarea de la base de datos
def delete_task(task_id):
    cursor.execute('''
        DELETE FROM tareas WHERE id = ?
    ''', (task_id,))
    db_conn.commit()
    show_tasks()

# Función para mostrar las tareas existentes en la base de datos
def show_tasks():
    task_list.delete(0, END)
    cursor.execute('''
        SELECT id, descripcion, completada FROM tareas
    ''')
    for row in cursor.fetchall():
        task_list.insert(END, row)

# Crear la interfaz de usuario usando Tkinter
root = Tk()
root.title("Mi aplicación to-do")

# Crear una entrada de texto para ingresar la descripción de la tarea
task_input = Entry(root, width=30)
task_input.pack()

# Crear un botón para añadir una tarea
add_button = Button(root, text="Añadir", command=add_task)
add_button.pack()

# Crear una lista para mostrar las tareas existentes
task_list = Listbox(root)
task_list.pack()

# Mostrar las tareas existentes en la base de datos cuando se inicie la aplicación
show_tasks()

# Crear un botón para editar una tarea seleccionada
edit_button = Button(root, text="Editar", command=lambda: edit_task(task_list.get(ACTIVE)[0]))
edit_button.pack()

# Crear un botón para marcar una tarea como completada
complete_button = Button(root, text="Completar", command=lambda: complete_task(task_list.get(ACTIVE)[0]))
complete_button.pack()

# Crear un botón para borrar una tarea seleccionada
delete_button = Button(root, text="Borrar", command=lambda: delete_task(task_list.get(ACTIVE)[0]))
delete_button.pack()

# Asegurarse de cerrar la conexión a la base de datos cuando la aplicación se cierre
db_conn.close()

root.mainloop()

'''
En este código se crean una entrada de texto para ingresar la descripción de la tarea, un botón para añadir una tarea, una lista para mostrar las tareas existentes, un botón para editar una tarea seleccionada, un botón para marcar una tarea como completada, un botón para borrar una tarea seleccionada y se muestran las tareas existentes en la base de datos cuando se inicie la aplicación. Además, se cierra la conexión a la base de datos cuando la aplicación se cierre.
'''