from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 12, 18),
    'depends_on_past': False,
    'email': ['sharshav.nimmag@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG('employee_data',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

with dag:
    #Task 1
    run_script_task = BashOperator(
        task_id='extract_data',
        bash_command='python /home/airflow/gcs/dags/scripts/extract.py', #default dags folder: /home/airflow/gcs/dags
    )

    #Task 2
    start_pipeline = CloudDataFusionStartPipelineOperator(
    location="us-central1",
    pipeline_name="ETL1-Pipeline",
    instance_name="etl1-instance1",
    task_id="start_datafusion_pipeline",
    )

    run_script_task >> start_pipeline #this defines the order in which tasks should perform