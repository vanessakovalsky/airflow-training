from airflow import DAG
import datetime as dt
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator

default_args = {
    "email":['vanessakovalsky@gmail.com'],
    "email_on_failure":True
}

default_params = {
    "to":"vanessakovalsky@gmail.com"
}

dag = DAG(
    dag_id="email_vanessa",
    schedule_interval="@yearly",
    start_date=dt.datetime(1988,12,9,1,45),
    catchup=False,
    default_args=default_args,
    params=default_params
)

task2 = BashOperator(
    task_id="t2",
    dag=dag,
    bash_command="ls",
    email=["v.david@kovalibre.com"],
    email_on_failure=True,
    email_on_retry=True
)



task3 = EmailOperator(
    task_id="email_task",
    to='{{params.to}}',
    subject="Hello from Airflow!",
    html_content="<i>Message from Airflow</i><br />{{ run_id }}</br>{{dag}}<br />{{ti}}"
)

task2 >> task3
