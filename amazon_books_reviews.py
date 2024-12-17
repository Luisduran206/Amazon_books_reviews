#!/usr/bin/python3
# amazon_books_reviews.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, udf, round
from pyspark.sql.types import DoubleType
from textblob import TextBlob
import sys

# Función UDF para análisis de sentimiento usando TextBlob
def get_polarity(text):
    try:
        return TextBlob(text).sentiment.polarity
    except Exception:
        return 0.0

def get_subjectivity(text):
    try:
        return TextBlob(text).sentiment.subjectivity
    except Exception:
        return 0.0

def main():
    # Inicializar SparkSession
    spark = SparkSession.builder.appName("AmazonBooksReviews").getOrCreate()

    # Argumentos de entrada y salida
    input_path = sys.argv[1]  # Ruta de entrada
    output_path = sys.argv[2]  # Ruta de salida

    # Leer los datos como DataFrame de Spark
    df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)

    # Registrar funciones UDF para agregar columnas de polaridad y subjetividad
    polarity_udf = udf(get_polarity, DoubleType())
    subjectivity_udf = udf(get_subjectivity, DoubleType())

    # Aplicar las funciones UDF y crear nuevas columnas
    df = (
        df.withColumn("polarity", polarity_udf(col("review/text")))
          .withColumn("subjectivity", subjectivity_udf(col("review/text")))
    )

    # Calcular estadísticas agregadas
    resultado = (
        df.groupBy("Id", "Title")
          .agg(
              avg(col("review/score")).alias("avg_review_score"),
              avg(col("polarity")).alias("avg_polarity"),
              avg(col("subjectivity")).alias("avg_subjectivity"),
          )
          .withColumn("avg_review_score", round(col("avg_review_score"), 4))
          .withColumn("avg_polarity", round(col("avg_polarity"), 4))
          .withColumn("avg_subjectivity", round(col("avg_subjectivity"), 4))
          .orderBy(col("avg_review_score").desc())  # Ordenar en orden descendente
    )

    # Guardar el resultado en la ruta de salida
    resultado.write.csv(output_path, header=True)

    spark.stop()  # Detener la sesión de Spark

if __name__ == "__main__":
    main()
