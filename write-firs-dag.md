# Ecrire un premier DAG

Cet exercice vous permet

- d'écrire un premier DAG
- de l'exécuter

# Ecrire son premier dag

* Créer un fichier birthday.py et coller le code suivant à l'intérieur

```python
import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator

"""
Exercise 2

Create a DAG which will run on your birthday to congratulate you.
"""

MY_NAME = ...
MY_BIRTHDAY = dt.datetime(...)

dag = DAG(
    dag_id="happy_birthday",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule_interval="@yearly",
    start_date=...,
)

birthday_greeting = BashOperator(
    task_id="send_wishes",
    dag=dag,
    bash_command=f"echo 'happy birthday {MY_NAME}!'"
)
```
* Compléter le DAG pour qu'il soit déclencher une fois par an à la date de votre anniversaire
* N'hésitez pas à consulter la documentation pour vous aider : https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
* Une fois terminé, enregistrer votre fichier

## Exécuter son DAG sur Composer

* Ouvrer l'UI de Composer, et importer votre DAG (vous pouvez le faire en ligne de commande si vous préférez)
* Exécuter votre DAG
* Quel est le résultat ?

## Pour aller plus loin

* Modifier votre fichier pour ajouter une fonction qui calcul votre age
* Ajouter votre age au message affiché pour votre anniversaire puis réexcuter votre DAG.
