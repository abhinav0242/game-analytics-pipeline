# Game Analytics Pipeline

A local data pipeline that processes simulated player telemetry data to deliver marketing insights like daily active users (DAU). Built with Python, Spark, and Airflow. Forked and adapted from [NYC_Taxi_Data_Pipeline](https://github.com/trannhatnguyen2/NYC_Taxi_Data_Pipeline). AWS S3 integration is planned.

## Current Features
- Generates mock game events (e.g., logins, purchases) with Python and Faker.
- Stores data locally in `data/raw/` (AWS S3 pending).
- Work-in-progress: Spark processing and Airflow orchestration.

## Setup
1. Clone the repo: `git clone https://github.com/abhinav0242/game-analytics-pipeline.git`
2. Install Python dependencies: `pip install faker`
3. Run: `python src/generate_game_data.py` then `python src/local_to_raw.py`