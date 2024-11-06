from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

from google.cloud import storage

from pendulum import datetime



@dag(start_date=datetime(2024,11,5), schedule=None, catchup=False)
def pull_file_vanessa():
    @task(task_id="lecture_fichier")
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
            texte = (f.read())
        return texte
    write_read()

    @task.bash
    def affiche_fichier() -> str:
        ti = get_current_context()["ti"]

        value =  ti.xcom_pull(task_ids='lecture_fichier')

        return 'echo "XCom fetched: { value }"'
    affiche_fichier()

pull_file_vanessa() 