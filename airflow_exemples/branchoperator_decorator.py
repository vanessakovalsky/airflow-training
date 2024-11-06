from airflow.operators.dummy import DummyOperator
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


DAG_NAME = "branchdemo_decorator"

@dag(
    DAG_NAME,
    start_date= days_ago(1),
    catchup= False,
    schedule="@daily"
)
def example_branche_decorator():
    start = DummyOperator(task_id="start")
    
    @task.branch(task_id="condition", params="")
    def choix(resultats):
        if resultats > 2:
            return 'op_1'
        return 'op_3'
    
    resultats = 1

    @task.bash(task_id="op_1")
    def op_1():
        return 'echo tache op1'

    @task.bash(task_id="op_3")
    def op_3():
        return 'echo tache op3'
    
    start >> choix(resultats) >> [op_1(), op_3()]

example_branche_decorator() 