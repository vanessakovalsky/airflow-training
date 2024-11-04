## Ajouter des conditions et utiliser le BranchOperator

* Ensuite nous voulons ajouter une condition à notre DAG : Si le fichier latest.zip est présent dans notre bucket, alors on continue le traitement, sinon on appelle on charge le fichier dans le bucket
* Pour cela :
* * Utiliser un branch operateur qui va vérifier notre condition : https://docs.astronomer.io/learn/airflow-branch-operator 
  * Pour vérifier la présence d'un fichier sur un bucket on peut utiliser GCSObjectExistenceSensor : https://registry.astronomer.io/providers/google/versions/latest/modules/gcsobjectexistencesensor
  * Créer une tache qui utilise le PythonOperator et contient le code suivant (vous pouvez aussi mettre ce code dans Cloud function et déclencher la fonction avec l'operator SimpleHTTPOperator) :
```python
from google.cloud import storage

def write_read(bucket_name, blob_name):
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    with blob.open("w") as f:
        f.write("Hello world")

    with blob.open("r") as f:
        print(f.read())

```
* Charger votre DAG et exécuter le pour voir le résultat

