# STEP 1 : Libraries needed 
from datetime import timedelta, datetime
from airflow import models
from airflow.operators.bash import BashOperator
#from airflow.operators.bash import BaseOperator
#from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators import dataproc_operator
from airflow.utils import trigger_rule

# STEP 2 : Define a start date 
# In this case yesterday
yesterday = datetime(2023, 8, 27)

# Spark references 
SPARK_CODE = (f'gs://us-central1-dataproc-airflo-aa05c7b3-bucket/spark-code/transformation.py')
dataproc_job_name = 'spark_job_dataproc'

# STEP 3 : Set default arguments for DAG
default_dag_args = {
    'start_date' : yesterday,
    'depends_on_past ' : False,
    'email_on_failure ' : False,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : timedelta(minutes=5),
    'region' : 'us-central1',
    'project_id': 'dataproc-397308'
}

# STEP 4 : Define DAG
# set the DAG name, and A DAG description, define the schedule interval and pass the default arguments defined before
with models.DAG(
    'spark_workflow',
    description='DAF for deployment a Dataproc Cluster',
    schedule_interval=None,
    default_args=default_dag_args) as dag:

    #STEP 5 : Set Operators 

    #bashOperator
    # A simple print date 
    
    #print_date = BaseOperator(
    print_date = BashOperator(
        task_id='print_date',
        bash_command = 'date'
    )
    

    #dataproc_operator
    #Create small dataproc Cluster
    create_dataproc = dataproc_operator.DataprocClusterCreateOperator(
        task_id = 'create_dataproc',
        project_id =  'dataproc-397308',
        cluster_name = 'dataproc-cluster-airflow',
        num_workers= 2,        
        region = 'us-central1',
        zone = 'us-central1-b',
        image_version = '2.1-debian11',        
        master_machine_type='n1-standard-4',
        worker_machine_type='n1-standard-4'
        )

    #Run the PySpark job
    run_spark = dataproc_operator.DataProcPySparkOperator(
        task_id = 'run_spark_job',
        main= SPARK_CODE,
        cluster_name='dataproc-cluster-airflow',
        job_name= dataproc_job_name
    )
    #dataproc_operator
    #delete Cloud Dataproc Cluster
    delete_dataproc = dataproc_operator.DataprocClusterDeleteOperator(
        task_id = 'delete_dataproc',
        project_id =  'dataproc-397308',
        cluster_name = 'dataproc-cluster-airflow',
        region = 'us-central1',
        trigger_rule= trigger_rule.TriggerRule.ALL_DONE
        #trigger_rule = trigger_rule.TriggerRule.ALL_SUCCESS
    )
    #STEP 6 : Set DAGS dependencies 
    # Each task should run after have finished the tas before
    print_date >> create_dataproc >> run_spark >> delete_dataproc