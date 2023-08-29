from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

# Crear una SparkSession
spark = SparkSession.builder \
    .appName("GCS with Spark") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.fs.gs.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/opt/bitnami/spark/python_files/jar/service-account-key.json") \
    .getOrCreate()

file_csv = f"gs://seti-bucket/sample_submission.csv"

df = spark.read.csv(file_csv, header=True)
df.show()

file_json = "gs://seti-bucket/json_results/"

df.write.json(file_json)

# Stop the SparkSession
spark.stop()