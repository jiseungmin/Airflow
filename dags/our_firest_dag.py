from airflow import DAG
from airflow.operators.bash import BashOperator  # Airflow 2.0 이상을 사용하는 경우
from datetime import datetime, timedelta

default_args = {  # 오타 수정
    'owner': "Jiseungmin",
    'retries': 5,
    'retry_delay': timedelta(minutes=2),  # 올바른 위치에 쉼표 추가
}

with DAG(
    dag_id='our_first_dag_v4',
    default_args=default_args,  # 오타 수정
    description="This is our first dag that we write",
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily',
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hello world, this is the first task!",
    )
    
    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hello i am task2",
    )
    
    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Hello i am task3 ",
    )
    
    # Task dependency method 1
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    # Task dependency method 2
    task1 >> task2
    task2 >> task3
    
    # Task dependency method 3
    # task1 >> [task2, task3]