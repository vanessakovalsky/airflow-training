from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago


DAG_NAME = "all_tasks_in_one_dag"

args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}

with DAG(dag_id=DAG_NAME, default_args=args) as dag:
    start = DummyOperator(task_id="start")
    
    task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)
    
    task_42 = BashOperator(task_id="op-42", bash_command=":", dag=dag)

    task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)

    some_other_task = DummyOperator(task_id="some-other-task")

    task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)

    task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)

    end = DummyOperator(task_id="end")

    start >> [task_1, task_2, task_42] >> some_other_task >> [task_3, task_4] >> end