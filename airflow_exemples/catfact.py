
5.2 [Pratique] Coder notre premier DAG

Voir ici : https://github.com/vanessakovalsky/airflow-training/blob/main/write-firs-dag.md
6.7 [Pratique] Configurer un LocalExcutor et run un DAG
6.8 [Pratique] Configurer un CeleryExecutor et run un DAG

from airflow.decorators import dag, task
from pendulum import datetime

import requests
import json

url = "http://catfact.ninja/fact"

default_args = {"start_date": datetime(2021, 1, 1)}

@dag(schedule="@daily", default_args=default_args, catchup=False)
def xcom_taskflow_dag():
    @task
    def get_a_cat_fact():
        """
        Gets a cat fact from the CatFacts API
        """
        res = requests.get(url)
        return {"cat_fact": json.loads(res.text)["fact"]}

    @task
    def print_the_cat_fact(cat_fact: str):
        """
        Prints the cat fact
        """
        print("Cat fact for today:", cat_fact)
        # run some further cat analysis here

    # Invoke functions to create tasks and define dependencies
    print_the_cat_fact(get_a_cat_fact())

xcom_taskflow_dag()

Dans ce DAG utilisant la syntaxe traditionnelle, il existe deux tâches PythonOperator qui partagent des données à l’aide des fonctions xcom_push et xcom_pull. Dans la fonction get_a_cat_fact, la méthode xcom_push a été utilisée pour permettre de spécifier le nom de la clé. Alternativement, la fonction pourrait être configurée pour renvoyer la valeur « cat_fact », car toute valeur renvoyée par un opérateur dans Airflow est automatiquement transmise à XCom.

Pour l’appel xcom_pull dans la fonction analyze_cat_facts, vous spécifiez la key et les task_ids associés au XCom que vous souhaitez récupérer. Cela vous permet d’extraire n’importe quelle valeur XCom (ou plusieurs valeurs) à tout moment dans une tâche. Il n’est pas nécessaire qu’il provienne de la tâche immédiatement précédente, comme le montre cet exemple.

from airflow.decorators import dag, task
from pendulum import datetime

import requests
import json

url = "http://catfact.ninja/fact"

default_args = {"start_date": datetime(2021, 1, 1)}

@dag(schedule="@daily", default_args=default_args, catchup=False)
def xcom_taskflow_dag():
    @task
    def get_a_cat_fact():
        """
        Gets a cat fact from the CatFacts API
        """
        res = requests.get(url)
        return {"cat_fact": json.loads(res.text)["fact"]}
    get_a_cat_fact()
    @task
    def print_the_cat_fact(**context):
        """
        Prints the cat fact
        """
        contenu_xcom = context["ti"].xcom_pull(
            task_ids="get_a_cat_fact",
            key="cat_fact"
        )
        print("Cat fact for today:", contenu_xcom)
        # run some further cat analysis here

    # Invoke functions to create tasks and define dependencies
    print_the_cat_fact()

xcom_taskflow_dag()