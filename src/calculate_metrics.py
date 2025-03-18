from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, to_date

spark = SparkSession.builder.appName("GameAnalytics").getOrCreate()
df = spark.read.parquet("data/processed/game_logs")
dau = df.groupBy(to_date("timestamp").alias("date")).agg(countDistinct("player_id").alias("daily_active_users"))
dau.write.parquet("data/analytics/dau")
print("Calculated DAU and saved to data/analytics/dau")