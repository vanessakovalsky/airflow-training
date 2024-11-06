from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

DAG_NAME = "all_tasks_in_one_dag_group"

args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}

with DAG(dag_id=DAG_NAME, default_args=args) as dag:
    start = DummyOperator(task_id="start")
    
    # def choix(resultats):
    #     if resultats > 2:
    #         return['tg1']
    #     return['tg2']
    
    # resultats = 1
    
    
    # tache_condition = BranchPythonOperator(
    #     task_id='condition',
    #     python_callable=choix,
    #     op_args=[resultats]
    # )
    
    with TaskGroup(group_id='groupe-tache-1') as tg1:
        task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)

        task_42 = BashOperator(task_id="op-42", bash_command=":", dag=dag)

        task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)
        
        task_1 >> task_2

    some_other_task = DummyOperator(task_id="some-other-task")

    with TaskGroup(group_id='groupe-tache-2') as tg2:
        task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)

        task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)

    end = TriggerDagRunOperator(
        task_id="end",
        trigger_dag_id="all_tasks_in_one_dag",
    )

    start >> tg1 >> some_other_task >> tg2 >> end
