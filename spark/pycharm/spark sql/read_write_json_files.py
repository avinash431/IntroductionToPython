from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("read_write_json_files").getOrCreate()


df = spark.read. \
    format("json").\
    option("inferSchema", "true").\
    option("path", "./data/flight_data/json/2015-summary.json"). \
    load()

df.printSchema()
df.show()

df.write.\
    format("json").\
    mode("overwrite").\
    option("path", "tmp/my_json").\
    save()

spark.stop()
