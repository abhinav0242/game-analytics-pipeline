from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('game_analytics_pipeline', start_date=datetime(2025, 3, 16), schedule_interval='@daily') as dag:
    generate = BashOperator(task_id='generate_data', bash_command='python src/generate_game_data.py')
    to_raw = BashOperator(task_id='to_raw', bash_command='python src/local_to_raw.py')
    to_processed = BashOperator(task_id='to_processed', bash_command='spark-submit src/raw_to_processed.py')
    calc_metrics = BashOperator(task_id='calculate_metrics', bash_command='spark-submit src/calculate_metrics.py')
    generate >> to_raw >> to_processed >> calc_metrics