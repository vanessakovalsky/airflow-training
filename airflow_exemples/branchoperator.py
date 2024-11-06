from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator
from airflow import DAG

DAG_NAME = "branchdemo"

args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}

with DAG(dag_id=DAG_NAME, default_args=args) as dag:
    start = DummyOperator(task_id="start")
    
    def choix():
        bucket_name = "europe-west9-formationairfl-d4ff149a-bucket"

        # The ID of your new GCS object
        blob_name = "data/demo.txt"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        resultat_exist = blob.exists()
        if resultat_exist:
            return 'op-1'
        return 'op-3'
    
     
    tache_condition = BranchPythonOperator(
        task_id='condition',
        python_callable=choix
    )

    tg1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)
    tg2 = BashOperator(task_id="op-3", bash_command=":", dag=dag)

    end = TriggerDagRunOperator(
        task_id="end",
        trigger_dag_id="all_tasks_in_one_dag",
    )

start >> tache_condition >> end