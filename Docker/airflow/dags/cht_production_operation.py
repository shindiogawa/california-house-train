from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

from datetime import timedelta
import datetime

default_args = {
    'owner' : 'airflow',
    'retries' : 0
}

dag = DAG(
    dag_id = 'dbt_cht_transforming',
    start_date = airflow.utils.dates.days_ago(2),
    schedule_interval = '0 */6 * * *',
    catchup=False,
    default_args = default_args
)

dbt_stg_debug = BashOperator(
    task_id='dbt_stg_debug',
    bash_command= 'cd /usr/app/cht-dbt;dbt debug',
    dag=dag
)

stg_cht_raw = BashOperator(
    task_id='stg_cht_raw',
    bash_command= 'cd /usr/app/cht-dbt;dbt run --m stg_cht_raw',
    dag=dag
)

cht_math = BashOperator(
    task_id='cht_math',
    bash_command= 'cd /usr/app/cht-dbt;dbt run --m cht_math',
    dag=dag
)

dbt_stg_debug >> stg_cht_raw >> cht_math