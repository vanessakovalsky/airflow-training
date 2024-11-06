from airflow.decorators import dag, task_group
from airflow.operators import DummyOperator

from pendulum import datetime

@dag(start_date=datetime(2024,11,5), schedule=None, catchup=False)
def groupe_imbrique_exemple():
    @task_group(group_id='mon_groupe_parent')
    def mgp():
        premiere_dependance = DummyOperator(task_id='tache_1')
        @task_group(group_id='premier_groupe_enfant')
        def pge():    
            tache_2 = DummyOperator(task_id='tache_2') 
            premiere_dependance >> tache_2
        mgp.append(pge())
        @task_group(group_id='deuxieme_groupe_enfant')
        def dge():
            tache_3 = DummyOperator(task_id='tache_3') 
            premiere_dependance >> tache_3
        # dge(pge())
        mgp.append(dge())
    mgp()
groupe_imbrique_exemple() 