# Rendre son DAG dynamique

Cet exercice vous permet pas à pas d'ajouter du dynamisme dans votre DAG

## DAG de départ

Cet exercice nécessite les éléments suivant :
* un environnement airflow (comme Composer de Google Cloud par exemple)
* La création d'un fichier DAG de départ contenant le code suivant :

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

DAG_NAME = "all_tasks_in_one_dag"

args = {"owner": "airflow", "start_date": days_ago(1), "schedule_interval": "@once"}

with DAG(dag_id=DAG_NAME, default_args=args) as dag:
    start = DummyOperator(task_id="start")

    task_1 = BashOperator(task_id="op-1", bash_command=":", dag=dag)

    task_2 = BashOperator(task_id="op-2", bash_command=":", dag=dag)

    some_other_task = DummyOperator(task_id="some-other-task")

    task_3 = BashOperator(task_id="op-3", bash_command=":", dag=dag)

    task_4 = BashOperator(task_id="op-4", bash_command=":", dag=dag)

    end = DummyOperator(task_id="end")

    start >> [task_1, task_2] >> some_other_task >> [task_3, task_4] >> end
```

Cela nous permet d'avoir un dag ressemblant à ça :

![](https://cloud.google.com/static/composer/docs/images/workflow-group-dags.png)

## Regrouper ces tâches avec un groupe de tâches

* Nous voulons modifier le dag de départ pour que les taches 1 et 2 soit regroupé dans un groupe de tache, et les tache 3 et 4 dans un autre.
* Le DAG ressemblera alors à :
![](https://cloud.google.com/static/composer/docs/images/workflow-taskgroup-dag.png)

* Pour cela modifier votre dag de la manière suivante à l'aide de la documentation https://docs.astronomer.io/learn/task-groups :
* * Créer un TaskGroup1 contenant les taches 1 et 2
  * Créer un TaskGroup2 contenant les taches 3 et 4
  * Modifier l'ordonnancement de votre DAG pour appeler les groupes de taches plutôt que les taches 1,2 et 3,4.
* Une fois les modifications apportées, vous pouvez importer votre DAG et l'exécuter

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

## Ajouter une notification par mail

* Nous voulons ensuite ajouter une notification par email lorsque notre DAG a terminé (quelque soit le résultat).
* Pour cela :
* * : Configurer votre environnement composer pour pouvoir envoyer des emails : https://cloud.google.com/composer/docs/configure-email?hl=fr
  * Ajouter une tache d'envoi d'email avec l'opérateur Emailoperator (vous avez un exemple dans lien ci dessus)
* Charger votre DAG et exécuter le pour voir le résultat

## Faire passer des données d'une tâches à une autre

* Lors de l'envoi du fichier sur le bucket nous voulons récupérer l'URI du fichier et la mettre dans l'email envoyé
* Pour cela, nous allons devoir récupérer la données de la tâche de dépôt de fichier, puis la transmettre à la tâche d'envoi d'email
* Nous allons donc utiliser les Xcom pour le faire, voir un exemple ici : https://marclamberti.com/blog/airflow-xcom/
* Charger votre DAG et exécuter le pour voir le résultat

## Utiliser les paramètres

* Nous voulons rendre le nom du bucket et du fichier utilisé paramètrables
* * Définir au niveau du DAG les params : bucket et filename (tout deux de type string et obligatoire) : voir ici : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#dag-level-params
  * Dans les tâches qui ont besoin de ces informations utiliser les paramètres : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html#referencing-params-in-a-task
* Charger votre DAG et exécuter le pour voir le résultat


## Utiliser les templates

* Lors de l'envoi du mail nous voulons ajouter certains paramètres dans le corps du mail
* * Récupérer dans les templates disponibles https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html les paramètres suivants :
  * Id du DAG run
  * Nom du dag
  * Instance de la tâche
  * Afficher ces paramètres dans le corps du mail envoyé
* Charger votre DAG et exécuter le pour voir le résultat

 ## Pour aller plus loin

 * Mettre en place un DAG déclenché par Pub/Sub sur lesquels les messages sont publiés par Cloud Functions : https://cloud.google.com/composer/docs/composer-2/triggering-gcf-pubsub?hl=fr
 * Utiliser les templatesfield : https://www.restack.io/docs/airflow-knowledge-apache-templates-fields
