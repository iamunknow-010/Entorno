import time

print("🚀 Entorno de aprendizaje iniciado con éxito.")
print("Conexión con la base de datos configurada (simulada).")

# Este bucle evita que el contenedor se apague
while True:
    time=time.sleep(3600)  # Duerme una hora y repite
    print(time)