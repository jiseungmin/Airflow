from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {  # 오타 수정
    'owner': "jiseungmin",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}

def greet(ti):  # 함수 이름 수정(great -> greet)
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name') 
    last_name = ti.xcom_pull(task_ids='get_name', key='last_naem') 
    age = ti.xcom_pull(task_ids='get_age', key = 'age')
    print(f"Hello world! My name is {first_name} {last_name}, and I am {age} years old!")  # 오타 수정(end -> and)

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_naem', value='Fridman')

def get_age(ti):
    ti.xcom_push(key='age', value=19)
  


with DAG(
    'our_dag_with_python_operator_v06',  # dag_id 직접 전달
    default_args=default_args,  # 오타 수정
    description="Our first dag using python operator",
    start_date=datetime(2024, 4, 8),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        provide_context=True,  # Task Instance를 인자로 전달
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )
    
    task3 = PythonOperator(
        task_id = "get_age",
        python_callable=get_age
    )
    
    [task2,task3] >> task1  # task2가 task1 전에 실행
