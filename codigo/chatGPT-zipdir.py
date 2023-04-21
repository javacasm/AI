import zipfile
import time
import os
import datetime

directorio = "ruta/del/directorio"

while True:
    # Obtenemos la fecha y hora actual
    fecha_hora = datetime.datetime.now()

    # Generamos el nombre del archivo zip con la fecha y hora
    nombre_zip = fecha_hora.strftime("%Y-%m-%d_%H-%M-%S") + ".zip"

    # Creamos un archivo zip
    with zipfile.ZipFile(nombre_zip, "w") as zip:
        # Recorremos todos los archivos del directorio
        for archivo in os.listdir(directorio):
            # Añadimos cada archivo al archivo zip
            zip.write(os.path.join(directorio, archivo))

    # Esperamos una hora
    time.sleep(3600)




