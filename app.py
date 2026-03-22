import time

print("🚀 Entorno de aprendizaje iniciado con éxito.")
print("Conexión con la base de datos configurada (simulada).")

# Este bucle evita que el contenedor se apague
while True:
    print(time.ctime()) # Esto imprime el día, hora, minutos y segundos actual
    time.sleep(1)