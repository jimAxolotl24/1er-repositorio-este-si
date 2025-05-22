import threading
import time

def tarea(nombre,segundos):
    print(f"I n i c i a n d o  * {nombre} * ...")    
    time.sleep(segundos) # Simula trabajo ¿?
    print(f"-> * {nombre} * c o m p l e t a d a  :3")

# CREACION DE LOS HILOS
hilo1 = threading.Thread(
    target = tarea,
    args = ("Tarea - 1",2)
)
hilo2 = threading.Thread(
    target = tarea,
    args = ("Tarea - 2",1)
)

# Inicio de ejecución de los hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()