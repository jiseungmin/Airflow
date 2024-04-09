from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Jiseungmin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id='dag_with_catchuo_backfill_v01',
    default_args=default_args,
    start_date=datetime(2024, 4, 8),
    schedule_interval='@daily'
) as dag :
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command'
    )