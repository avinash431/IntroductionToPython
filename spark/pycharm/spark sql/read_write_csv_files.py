from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StructField, StructType, StringType

spark = SparkSession.builder.appName("read_write_csv_files").getOrCreate()


flightSchema = StructType([
    StructField("DEST_COUNTRY_NAME", IntegerType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", IntegerType(), True)
])

df = spark.read.\
    format("csv").\
    option("header", "true").\
    option("mode", "FAILFAST").\
    option("inferSchema", "true").\
    schema(flightSchema).\
    load("./data/flight_data/csv/2010-summary.csv")

df.printSchema()
df.show(truncate=False)


df.write.\
    format("csv")\
    .mode("overwrite")\
    .option("sep", "\t")\
    .option("path", "tmp/my_tsv")\
    .save()


spark.stop()
