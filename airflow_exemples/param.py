from airflow import DAG
from airflow.models.param import Param
from airflow.operators.python import PythonOperator
import datetime as dt
 
with DAG(
    "the_dag",
    params={
        "x": Param(5, type="integer", minimum=3),
        "my_int_param": 6
    },
    start_date=dt.datetime(1988,12,9,1,45),
    schedule=None
):
     PythonOperator(
        task_id="from_template",
        op_args=[
            "{{ params.my_int_param + 10 }}",
        ],
        python_callable=(
            lambda my_int_param: print(my_int_param)
        ),
    )
