from airflow import DAG
import datetime as dt
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from mail import send_mail

default_args = {
    "email":['vanessakovalsky@gmail.com'],
    "email_on_failure":True
}

dag = DAG(
    dag_id="email_vanessa",
    schedule_interval="@yearly",
    start_date=dt.datetime(1988,12,9,1,45),
    catchup=False,
    default_args=default_args
)

def send_email_retry(**context)
    titre="Un super memail"
    contenu = "Le contenu du mail"
    send_mail("vanessakovalsky@gmail.com", titre, contenu)

hello = BashOperator(
    task_id="hello",
    dag=dag,
    bash_command="echo 'Bonjour à tous!'"
    on_retry_callback = MySendEmailRetry()
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
