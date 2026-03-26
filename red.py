import os
import psycopg2
from dotenv import load_dotenv
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def probar_conexion():
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                print("Conexion exitosa")

    except psycopg2.Error as e:
        print(f"Error: {e}")


def crear_tabla():
    comando_sql= """
    CREATE TABLE IF NOT EXISTS predicciones (
        id SERIAL PRIMARY KEY,
        entrada FLOAT NOT NULL,
        resultado FLOAT NOT NULL,
        creado_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    
    try:
        with psycopg2.connect(DATABASE_URL) as con:
            with con.cursor() as  cur:
                cur.execute(comando_sql)
                print("Tabla creada")
    except Exception as e:
        print(f"Error: {e}")


def guardar_prediccion(valor_entrada, valor_resultado):

    query = """
        INSERT INTO predicciones (entrada, resultado)
        VALUES (%s, %s)
        RETURNING id;
        """
    
    try:
        with psycopg2.connect(DATABASE_URL) as con:
            with con.cursor() as cur:
                cur.execute(query, (valor_entrada, valor_resultado))
                nuevo_id=cur.fetchone()[0]    
                print(f"Prediccion gurdada con id: {nuevo_id}")
                return nuevo_id
    except psycopg2.DatabaseError as e:
        print(f"Error: {e}")
        return None
    
def entrenar_ia():
    x = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    modelo = LinearRegression()
    modelo.fit(x, y)

    print("IA entrenada")

    return modelo
    
    
if __name__ == "__main__":
    probar_conexion()
    crear_tabla()

    nombre_archivo = "modelo_ia.pkl"

    if os.path.exists(nombre_archivo):
        modelo_ia = joblib.load(nombre_archivo)
        print("🧠 Modelo cargado desde el archivo (Inferencia rápida)")
    else:
        modelo_ia = entrenar_ia()
        joblib.dump(modelo_ia, nombre_archivo)
        print("🎓 Modelo entrenado y guardado por primera vez")


    numero_nuevo = np.array([[20]])
    prediccion = modelo_ia.predict(numero_nuevo)[0]

    print(f"La IA predijo para {numero_nuevo[0][0]}: {prediccion}")
    
    # 4. Guardar ese pensamiento en la nube (Render)
    guardar_prediccion(float(numero_nuevo[0][0]), float(prediccion))