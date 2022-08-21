from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

lines = spark \
    .readStream \
    .format("text") \
    .option("path", "/Users/avinashs/Desktop/spark-streaming/") \
    .load()

words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# wordCounts = words.groupBy("word").count()

query = words \
    .writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "output-dir") \
    .option("checkpointLocation", "check_point_dir") \
    .start()


query.awaitTermination()
