from pyspark.sql import SparkSession

spark = SparkSession.\
    builder.\
    appName("kafka-demo").\
    master("local[3]").\
    getOrCreate()

kafka_df = spark.readStream.\
    format("kafka").\
    option("kafka.bootstrap.servers", "localhost:9092").\
    option("subscribe", "quickstart-events").\
    option("spark.streaming.stopGracefullyOnShutdown", "true"). \
    option("startingOffsets", "earliest"). \
    load()

write_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").\
    writeStream.\
    format("console").\
    option("checkpointLocation", "chk-point-dir").\
    outputMode("append").\
    start()


write_df.awaitTermination()
