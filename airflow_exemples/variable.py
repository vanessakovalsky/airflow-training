from airflow import DAG
import datetime as dt
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from airflow.models.param import Param

DAG_NAME = "monsuperdag"



dag = DAG(
    dag_id={DAG_NAME},
    schedule_interval="@yearly",
    start_date=dt.datetime(1988,12,9,1,45),
    catchup=False,
    params={
        "macle1": "mavaleur1",
        "macle2": Param(
            42,
            type="integer"
        )
    }

)


def my_python_function_with_param(**context):
    return print(context["params"]["macle1"]) 

hello = PythonOperator(
    task_id="python_task",
    params={"macle1":"masupervaleur"}
    python_callable=my_python_function_with_param,
    dag=dag
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
    to=['vanessakovalsky@gmail.com'],
    subject="Hello from Airflow!",
    html_content="<i>Message from Airflow</i>"
)

hello >> task2 >> task3
