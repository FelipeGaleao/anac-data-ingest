from sched import scheduler
from airflow import DAG 
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import sys, os

sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))

from tasks import ingest


with DAG(dag_id= "adi_anac_data_ingest",
         start_date=datetime(2022, 4, 14),
         max_active_runs = 4,
         catchup=False) as dag:
    
    with TaskGroup(group_id='data_ingest') as data_ingest:
        for year in range(2000, 2023):
            with TaskGroup(group_id=f'{year}') as month:
                for month in range(1, 13):       
                    task_ingest = PythonOperator(task_id=f"{year}-{month}",
                                        python_callable=ingest.ingest_file_from_anac,
                                        op_kwargs={'month': month,
                                                   'year': year})
                    task_ingest