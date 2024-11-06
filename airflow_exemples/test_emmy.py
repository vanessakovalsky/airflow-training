from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow.operators.dummy import DummyOperator
from google.cloud import storage
from airflow.operators.python import get_current_context
from airflow.providers.google.cloud.sensors.gcs import (
    GCSObjectExistenceSensor)

# Arguments par défaut pour toutes les tâches du DAG
args = {'owner': 'airflow','start_date': days_ago(1),"schedule_interval": "@once"}

# Définition du DAG
with DAG(dag_id='ExistenceSensor_EB_test',default_args=args) as dag:

    start = DummyOperator(task_id="start")

    @task(task_id="write_read")
    def write_read():
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        bucket_name = "europe-west9-formationairfl-d4ff149a-bucket"

        # The ID of your new GCS object
        blob_name = "data/demo.txt"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        with blob.open("r") as f:
            return f.read()

    @task(task_id="afficher_fichier")
    def afficher_fichier():
        ti = get_current_context()["ti"]
        value =  ti.xcom_pull(task_ids='write_read')
        print(value)
        return value
    
    gcs_object_exists = GCSObjectExistenceSensor(
        bucket="europe-west9-formationairfl-d4ff149a-bucket",
        object="data/demo.txt",
        task_id="gcs_object_exists_task"
    )

    end = DummyOperator(task_id="end")

    start >> [gcs_object_exists] >>  write_read() >> afficher_fichier() >> end


