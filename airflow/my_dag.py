from datetime import timedelta
import requests
import json
import logging

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'Diana',
    'depends_on_past': False,
    'email': ['ximena.garcia7482@alumnos.udg.mx'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}


def extract():
    resultado = requests.get('https://jsonplaceholder.cypress.io/todos')
    return json.loads(resultado.content)


def transform(ti=None):
    datos = ti.xcom_pull(task_ids="extract")
    usuarios = []
    for usuario in datos:
        usuarios.append({
            'UsuarioID': usuario['userId'],
            'ID': usuario['id'],
            'Titulo': usuario['title'],
            'Completado': usuario['completed']
        })
    return usuarios


def load(ti=None):
    datos = ti.xcom_pull(task_ids="transform")
    archivo = open('/usr/local/lib/python3.8/dist-packages/airflow/example_dags/datos.json', 'w')
    json.dump(datos, archivo, indent=5)
    archivo.close()


with DAG(
    'airflow_dag',
    default_args=default_args,
    description='Airflow dag con proceso etl',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    catchup=False,
    tags=['airflow dag']
) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    load_task = PythonOperator(task_id="load", python_callable=load)

    extract_task >> transform_task >> load_task
