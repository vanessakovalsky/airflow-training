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


 * Utiliser les templatesfield : https://www.restack.io/docs/airflow-knowledge-apache-templates-fields
