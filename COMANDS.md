docker-compose up --scale spark-worker=3 -d
Jars Folder path: /opt/bitnami/spark/jars

cd /opt/bitnami/spark/python_files/

docker-compose exec pyspark-spark-master-1 spark-submit --master spark://172.27.0.2:7077 test_spark_sum.py
spark-submit --master spark://172.28.0.2:7077 test_spark_sum.py

mv /opt/bitnami/spark/jars/guava-14.0.1.jar /opt/bitnami/spark/jars/guava-14.0.1.bk
cp /opt/bitnami/spark/python_files/jar/guava-30.1-jre.jar /opt/bitnami/spark/jars/

spark-submit --packages com.google.cloud.bigdataoss:gcs-connector:hadoop3-2.2.0 test_spark_cloud_storage.py