from airflow import DAG
import datetime as dt
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="demo_vanessa",
    schedule_interval="@yearly",
    start_date=dt.datetime(1988,12,9,1,45)
)

hello = BashOperator(
    task_id="hello",
    dag=dag,
    bash_command="echo 'Bonjour à tous!'"
)

task2 = BashOperator(
    task_id="t2",
    dag=dag,
    bash_command="ls"
)

#hello >> task2
