from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName('PySpark Code triggered by Apache Airflow script') \
    .getOrCreate()

abalone_dataset = spark.read.options(header='true', inferSchema='true').csv("gs://us-central1-dataproc-airflo-aa05c7b3-bucket/dataset/abalone.csv")
abalone_dataset.printSchema()

abalone_dataset.createOrReplaceTempView("abalone_details")

averaged_out_stats = spark.sql("""
                        SELECT 
                            sex, 
                            avg(Length), 
                            avg(Diameter), 
                            avg(Height), 
                            avg(rings) 
                        FROM abalone_details
                        GROUP BY Sex
                        """)    
#select * from abalone_details where UnitPrice >= 3.0")
averaged_out_stats.write.mode("overwrite").parquet("gs://us-central1-dataproc-airflo-aa05c7b3-bucket/temp-transformed-datasets/abalone_avg_stats_parquet/")


print("\n=================== Displaying the data in the parquet files =========================\n")

parquet_data = spark.read.parquet("gs://us-central1-dataproc-airflo-aa05c7b3-bucket/temp-transformed-datasets/abalone_avg_stats_parquet/")

print(parquet_data.show(truncate = False))