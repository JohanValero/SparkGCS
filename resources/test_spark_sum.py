# Import the necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
sparkApp = SparkSession.builder.appName("My App").getOrCreate()
rdd = sparkApp.sparkContext.parallelize(range(1, 100))

print(">> THE SUM IS HERE: ", rdd.sum())

# Stop the SparkSession
sparkApp.stop()