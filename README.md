# 🌤️ Pipeline de Dados Climáticos - Airflow

## 💼 Contexto de Negócio

**Desafio**: Uma empresa de turismo em Boston precisava de um sistema automatizado para extrair e processar dados meteorológicos semanais, permitindo planejar os melhores roteiros turísticos baseados nas condições climáticas previstas.

**Problema**: A empresa não possuía uma solução escalável para:
- Coletar dados meteorológicos de forma consistente e automatizada
- Processar e organizar informações climáticas para tomada de decisão
- Adaptar ofertas de passeios às condições meteorológicas previstas

**Solução Desenvolvida**: Pipeline de dados robusto usando Apache Airflow que:
- ✅ Extrai automaticamente dados da API Visual Crossing Weather
- ✅ Processa e estrutura informações meteorológicas
- ✅ Armazena dados organizados para análise de negócio
- ✅ Executa semanalmente de forma automatizada

**Impacto**: Capacita a empresa a tomar decisões data-driven sobre roteiros turísticos, melhorando a experiência do cliente e otimizando operações.

---

## 🏗️ Arquitetura Técnica

Este projeto implementa DAGs (Directed Acyclic Graphs) do Apache Airflow para extração e processamento automatizado de dados climáticos.

### DAGs Implementados:

### 🎯 1. `dados_climaticos` - Pipeline Principal
- **Objetivo**: Extração automatizada de dados meteorológicos para análise de negócio
- **Fonte**: API Visual Crossing Weather (Boston, MA)
- **Frequência**: Semanal (segundas-feiras às 00:00 UTC)
- **Processamento**:
  - 📁 Criação de estrutura de diretórios organizados por semana
  - 🌡️ Extração de dados completos da API meteorológica
  - 📊 Separação em datasets especializados:
    - `dados_brutos.csv`: Dataset completo da API
    - `temperaturas.csv`: Métricas de temperatura (máx, mín, média)
    - `condicoes.csv`: Condições meteorológicas e iconografia

### 🧪 2. `meu_primeiro_dag` - Exemplo Educacional
- **Objetivo**: Demonstração de conceitos fundamentais do Airflow
- **Funcionalidades**: Tarefas sequenciais e paralelas, criação de estruturas de dados

## �️ Stack Tecnológica

- **Orquestração**: Apache Airflow 2.0+
- **Linguagem**: Python 3.7+
- **Processamento**: pandas para manipulação de dados
- **Scheduling**: pendulum para gerenciamento de tempo
- **API Integration**: Visual Crossing Weather API
- **Versionamento**: Git + GitHub

## 🏆 Características Técnicas

- **Arquitetura orientada a eventos** com DAGs modulares
- **Processamento automatizado** com agendamento robusto
- **Tratamento de dados estruturados** em múltiplos formatos
- **Integração com APIs externas** com tratamento de erros
- **Logging e monitoramento** nativo do Airflow
- **Estrutura escalável** para expansão futura

## � Casos de Uso e Extensões

### Aplicações Atuais
- 🎯 **Planejamento Turístico**: Otimização de roteiros baseada em condições meteorológicas
- 📊 **Análise Temporal**: Identificação de padrões climáticos semanais
- 🔔 **Alertas Automáticos**: Base para sistemas de notificação meteorológica

### Possíveis Expansões
- 🌍 **Multi-cidade**: Extensão para múltiplas localidades
- 🤖 **ML Integration**: Modelos preditivos baseados em histórico
- 📱 **API própria**: Desenvolvimento de endpoints para consumo
- 📧 **Notificações**: Sistema de alertas automáticos
- 🔗 **Integração CRM**: Conexão com sistemas de gestão de clientes

---

## 🚀 Quick Start

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

## 📊 Dados e Métricas

### Fonte de Dados
- **API**: Visual Crossing Weather
- **Localização**: Boston, Massachusetts, USA
- **Cobertura**: Previsão de 7 dias
- **Atualização**: Semanal automatizada
- **Volume**: ~1000 registros/mês

### Datasets Gerados
| Arquivo | Descrição | Campos Principais |
|---------|-----------|-------------------|
| `dados_brutos.csv` | Dataset completo da API | Todos os campos meteorológicos |
| `temperaturas.csv` | Métricas térmicas | datetime, tempmax, tempmin, temp |
| `condicoes.csv` | Condições meteorológicas | datetime, description, icon |

### Estrutura de Saída
```
airflowalura/
├── semana=2025-09-15/
│   ├── dados_brutos.csv      # Dataset completo
│   ├── temperaturas.csv      # Análise térmica
│   └── condicoes.csv         # Condições climáticas
└── semana=2025-09-22/
    ├── dados_brutos.csv
    ├── temperaturas.csv
    └── condicoes.csv
```

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

---

## 📝 Licença & Contato

**Licença**: MIT License - Projeto educacional e demonstrativo

**Desenvolvedor**: [@tmarsbr](https://github.com/tmarsbr)

**Contato**: Para dúvidas ou discussões técnicas, abra uma [issue](https://github.com/tmarsbr/airflowalura/issues) no repositório.

---

*Este projeto demonstra competências em engenharia de dados, orquestração de workflows, integração de APIs e automação de processos usando ferramentas modernas da stack de dados.*