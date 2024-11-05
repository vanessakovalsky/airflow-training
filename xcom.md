## Faire passer des données d'une tâches à une autre

* Créer un DAG avec une tache qui va aller lire le fichier demo.txt sur le bucket (le nom du bucket vous est donné par le formateur) et qui contient le code suivant (la tache utilise Python operator)
```
from airflow.decorators import dag, task_group
from airflow.operators import DummyOperator
from google.cloud import storage

from pendulum import datetime



@dag(start_date=datetime(2024,11,5), schedule=None, catchup=False)
def pull_file():
    @task(task_id="lecture_fichier")
    def write_read(bucket_name, blob_name):
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        bucket_name = "europe-west9-formationairfl-d4ff149a-bucket "

        # The ID of your new GCS object
        blob_name = "/data/demo.txt"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        with blob.open("r") as f:
            return (f.read())
    write_read()


pull_file() 
```
* Lors du traitement de données nous voulons récupérer le contenu du fichier et le passer à une dernière tache qui sera en charge d'afficher le contenu du fichier.
* Nous allons donc utiliser les Xcom pour le faire, voir un exemple ici : https://marclamberti.com/blog/airflow-xcom/
* Charger votre DAG et exécuter le pour voir le résultat

