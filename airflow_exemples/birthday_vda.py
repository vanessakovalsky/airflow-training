import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 2

Create a DAG which will run on your birthday to congratulate you.
"""

MY_NAME = "Vanessa"
MY_BIRTHDAY = dt.datetime(1988,12,9,1,45)

dag = DAG(
    dag_id="happy_birthday_vda",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule_interval="@yearly",
    start_date={MY_BIRTHDAY},
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'happy birthday {MY_NAME} !'"
)
