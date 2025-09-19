# Projeto Airflow - Dados Climáticos

Este projeto contém DAGs (Directed Acyclic Graphs) do Apache Airflow para extração e processamento de dados climáticos.

## 📋 Descrição

O projeto inclui dois DAGs principais:

### 1. `dados_climaticos`
- **Função**: Extrai dados climáticos da API Visual Crossing Weather
- **Agendamento**: Executa toda segunda-feira às 00:00 UTC
- **Tarefas**:
  - Cria pasta semanal para armazenamento dos dados
  - Extrai dados climáticos de Boston para a semana
  - Salva os dados em três arquivos CSV:
    - `dados_brutos.csv`: Dados completos da API
    - `temperaturas.csv`: Temperaturas máxima, mínima e média
    - `condicoes.csv`: Descrição e ícones das condições climáticas

### 2. `meu_primeiro_dag`
- **Função**: DAG de exemplo para aprendizado
- **Agendamento**: Execução diária
- **Tarefas**: Sequência de tarefas vazias e criação de pasta

## 🚀 Requisitos

- Python 3.7+
- Apache Airflow 2.0+
- pandas
- pendulum

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd airflowalura
```

2. Instale as dependências:
```bash
pip install apache-airflow pandas pendulum
```

3. Configure o Airflow:
```bash
# Inicializar o banco de dados do Airflow
airflow db init

# Criar usuário admin (se necessário)
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```

## 🔧 Configuração

### API Key da Visual Crossing Weather

Para usar o DAG `dados_climaticos`, você precisa:

1. Obter uma API key gratuita em [Visual Crossing Weather](https://www.visualcrossing.com/weather-api)
2. Substituir a chave no arquivo `dags/dados_crimaticos.py`:
```python
key = "SUA_API_KEY_AQUI"
```

### Estrutura de Diretórios

O projeto gera a seguinte estrutura de dados:
```
airflowalura/
├── semana=YYYY-MM-DD/
│   ├── dados_brutos.csv
│   ├── temperaturas.csv
│   └── condicoes.csv
└── pasta=YYYY-MM-DDTHH:MM:SS+00:00/
```

## 🏃‍♂️ Como Executar

1. Inicie o servidor web do Airflow:
```bash
airflow webserver --port 8080
```

2. Em outro terminal, inicie o scheduler:
```bash
airflow scheduler
```

3. Acesse a interface web em `http://localhost:8080`

4. Ative os DAGs desejados na interface web

## 📊 Dados Extraídos

### Dados Climáticos de Boston
- **Fonte**: Visual Crossing Weather API
- **Cidade**: Boston, MA, USA
- **Frequência**: Semanal (toda segunda-feira)
- **Período**: 7 dias a partir da data de execução

### Campos dos Dados
- **datetime**: Data e hora
- **tempmax**: Temperatura máxima (°C)
- **tempmin**: Temperatura mínima (°C)
- **temp**: Temperatura média (°C)
- **description**: Descrição das condições climáticas
- **icon**: Ícone representativo do clima

## 📁 Estrutura do Projeto

```
airflowalura/
├── dags/
│   ├── dados_crimaticos.py    # DAG principal para dados climáticos
│   └── meu_primeiro_dag.py    # DAG de exemplo
├── logs/                      # Logs do Airflow
├── airflow.cfg               # Configuração do Airflow
├── airflow.db                # Banco de dados SQLite do Airflow
├── webserver_config.py       # Configuração do servidor web
└── README.md                 # Este arquivo
```

## 🔧 Personalização

### Alterando a Cidade
Para extrair dados de outra cidade, modifique a variável `city` em `dags/dados_crimaticos.py`:
```python
city = 'São Paulo'  # ou qualquer outra cidade
```

### Alterando a Frequência
Para mudar o agendamento, altere o `schedule_interval`:
```python
schedule_interval="0 0 * * *"  # Para execução diária
schedule_interval="@weekly"    # Para execução semanal
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue no GitHub.

---

**Nota**: Este projeto foi criado para fins educacionais e demonstração do Apache Airflow.