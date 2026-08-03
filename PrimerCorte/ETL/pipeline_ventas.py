"""
pipeline_ventas.py

Plantilla para el Ejercicio 4 (reto) del taller de ETL.

Objetivo: reescribir el pipeline del notebook como un script con funciones
separadas extract(), transform(), load() y una función main() que las orqueste.

Cómo usar esta plantilla:
1. Completa cada función con la lógica que ya construiste y probaste en el notebook
   (son literalmente los mismos pasos, solo organizados en funciones).
2. Ejecuta el script desde una terminal con:  python pipeline_ventas.py
3. Al final deberías obtener el mismo resultado que en el notebook: un archivo
   'data_warehouse.db' con las tablas 'ventas_limpias' y 'resumen_ventas_tienda'.
"""

import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta


def extract():
    """
    Genera/lee los datos de ventas "sucios" y el catálogo de tiendas.

    Retorna:
        df_ventas (pd.DataFrame): datos de ventas sin procesar.
        df_tiendas (pd.DataFrame): catálogo de tiendas.
    """
    np.random.seed(42)

    # TODO: copia aquí la lógica de generación de 'ventas_sucias' del notebook
    # (sección 1.1) y guárdala en 'ventas_raw.csv'.
    df_ventas = None  # <-- reemplaza

    # TODO: lee 'ventas_raw.csv' con pd.read_csv(..., parse_dates=["fecha"])
    df_ventas = None  # <-- reemplaza

    # TODO: crea el DataFrame df_tiendas igual que en la sección 1.3 del notebook
    df_tiendas = None  # <-- reemplaza

    return df_ventas, df_tiendas


def transform(df_ventas, df_tiendas):
    """
    Limpia, valida y enriquece los datos de ventas.

    Parámetros:
        df_ventas (pd.DataFrame): datos de ventas sin procesar (salida de extract()).
        df_tiendas (pd.DataFrame): catálogo de tiendas (salida de extract()).

    Retorna:
        df (pd.DataFrame): ventas limpias y enriquecidas.
        resumen_por_tienda (pd.DataFrame): agregado de ventas por tienda.
    """
    # TODO: aplica, en orden, los mismos pasos del notebook (sección 2):
    #   1. Quitar duplicados
    #   2. Descartar nulos críticos (id_tienda, producto) y convertir tipos
    #   3. Estandarizar texto en 'producto'
    #   4. Descartar cantidades inválidas
    #   5. (Ejercicio 1) Descartar precio_unitario > 1_000_000
    #   6. Imputar precios faltantes con la mediana por producto
    #   7. Calcular 'total_venta' y unir con df_tiendas
    #   8. Agregar 'resumen_por_tienda'
    #
    # Tip: si hiciste el Ejercicio 3, este es el lugar ideal para llenar
    # una lista `log_limpieza` y retornarla también, o guardarla en un archivo.

    df = None  # <-- reemplaza
    resumen_por_tienda = None  # <-- reemplaza

    return df, resumen_por_tienda


def load(df, resumen_por_tienda, db_path="data_warehouse.db"):
    """
    Carga los datos limpios y el resumen agregado en una base de datos SQLite.

    Parámetros:
        df (pd.DataFrame): ventas limpias (salida de transform()).
        resumen_por_tienda (pd.DataFrame): agregado por tienda (salida de transform()).
        db_path (str): ruta del archivo de base de datos SQLite.
    """
    # TODO (Ejercicio 5): envuelve esta carga en un try/except que capture
    # cualquier error y lo reporte de forma clara, sin detener el programa
    # de forma abrupta.
    try:
        conn = sqlite3.connect(db_path)

        # TODO: carga 'df' en la tabla 'ventas_limpias' y 'resumen_por_tienda'
        # en la tabla 'resumen_ventas_tienda', igual que en el notebook (sección 3).

        conn.close()
        print(f"Datos cargados correctamente en '{db_path}' ✅")
    except Exception as e:
        print(f"❌ Error al cargar los datos en '{db_path}': {e}")


def main():
    """Orquesta el pipeline completo: extract -> transform -> load."""
    df_ventas, df_tiendas = extract()
    df, resumen_por_tienda = transform(df_ventas, df_tiendas)
    load(df, resumen_por_tienda)


if __name__ == "__main__":
    main()
