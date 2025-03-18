from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("GameAnalytics").getOrCreate()
df = spark.read.json("data/raw/game_logs.json")
df.write.parquet("data/processed/game_logs")
print("Processed game_logs.json to data/processed/")