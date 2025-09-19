# %% 
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.macros import ds_add
import pendulum
import os
from os.path import join
import pandas as pd

# %%
with DAG(
        "dados_climaticos", 
         start_date=pendulum.datetime(2025, 9, 1, tz="UTC"),
         schedule_interval="0 0 * * 1" # executa toda segunda-feira às 00:00
) as dag:

    tarefa_1 = BashOperator(
        task_id = "cria_pasta",
        bash_command = 'mkdir -p "/home/tiago/Documents/airflowalura/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extrai_dados(data_interval_end):
        city = 'Boston'
        # Obtém a chave da API de variável de ambiente por segurança
        key = os.getenv('VISUAL_CROSSING_API_KEY', 'SUA_CHAVE_AQUI')
        
        if key == 'SUA_CHAVE_AQUI':
            raise ValueError("API key não encontrada! Configure a variável de ambiente VISUAL_CROSSING_API_KEY")

        URL = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
                f"{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv")

        # %% 
        dados = pd.read_csv(URL)
        

        # %%
        # Salvando os dados em CSV

        folder_path = f'/home/tiago/Documents/airflowalura/semana={data_interval_end}/'
        

        dados.to_csv(folder_path + "dados_brutos.csv")
        dados[['datetime', 'tempmax', 'tempmin', 'temp']].to_csv(folder_path + "temperaturas.csv")
        dados[['datetime', 'description', 'icon']].to_csv(folder_path + "condicoes.csv")

    tarefa_2 = PythonOperator(
        task_id = "extrai_dados",
        python_callable = extrai_dados,
        op_kwargs={'data_interval_end' : '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )  

    tarefa_1 >> tarefa_2
