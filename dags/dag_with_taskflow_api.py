from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': "Jiseungmin",
    "retries": 5,
    "retry_delay": timedelta(minutes=5)
}

@dag(dag_id="dag_with_taskflow_api_v02",
     default_args=default_args,
     start_date=datetime(2024,4,8),
     schedule_interval='@daily')
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jerry',
            'last_name': 'Fridman'
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name: str, last_name: str, age: int):  # 파라미터 타입 힌트 추가
        print(f"Hello World! My name is {first_name} {last_name} and I am {age} years old!")  # 오탈자 수정 및 문자열 분리 수정
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],  # 'first_naem' -> 'first_name' 오타 수정
          last_name=name_dict['last_name'],
          age=age)
    
greet_dag = hello_world_etl()
