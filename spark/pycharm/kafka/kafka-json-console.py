from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType, IntegerType, ArrayType

spark = SparkSession.\
    builder.\
    appName("kafka-demo").\
    master("local[3]").\
    getOrCreate()

schema = StructType([
            StructField("id", IntegerType(), nullable=False),
            StructField("name", StringType(), nullable=False)
        ])

kafka_df = spark.readStream.\
    format("kafka").\
    option("kafka.bootstrap.servers", "localhost:9092").\
    option("subscribe", "topic4").\
    option("spark.streaming.stopGracefullyOnShutdown", "true"). \
    option("startingOffsets", "earliest"). \
    load(). \
    select(col("value").cast(StringType()).alias("value")).\
    select(from_json(col("value"), schema).alias("value")).\
    select("value.id", "value.name").\
    writeStream.\
    outputMode("update").\
    format("console").\
    trigger(processingTime='1 minute'). \
    start()

kafka_df.awaitTermination()



