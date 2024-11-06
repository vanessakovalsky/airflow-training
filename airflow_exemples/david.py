from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup 

DAG_NAME = "all_tasks_in_one_dag_david"
 
args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}
 
with DAG(dag_id=DAG_NAME, default_args=args) as dag:
    start = DummyOperator(task_id="start")
 
    with TaskGroup(group_id='taskgroup_1') as tg1:
        task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)
        task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)
    
    some_other_task = DummyOperator(task_id="some-other-task")
 
    with TaskGroup(group_id='taskgroup_2') as tg2:
        task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)
        task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)
 
    end = DummyOperator(task_id="end")
 
    start >> tg1 >> some_other_task >> tg2 >> end