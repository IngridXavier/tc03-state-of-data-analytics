# State of Data Analytics — Tech Challenge 3

## 📌 Sobre o projeto

Este projeto está sendo desenvolvido como parte do Tech Challenge — Fase 3, com o objetivo de construir uma solução de Engenharia de Dados e Analytics em ambiente Cloud, utilizando serviços da Amazon Web Services (AWS) para processar e analisar as três pesquisas mais recentes disponíveis do **State of Data Brasil**.

O desafio consiste em transformar dados brutos sobre profissionais de Dados e Tecnologia no Brasil em informações úteis para a tomada de decisão de uma instituição financeira de grande porte, apoiando estratégias de contratação, capacitação profissional e investimentos em tecnologia e Inteligência Artificial.

A solução contempla a construção de um pipeline de dados com arquitetura em camadas, utilizando Amazon S3 para armazenamento, AWS Glue e Apache Spark para processamento e transformação, além do catálogo de dados e ferramentas de consulta e análise.

O projeto busca conectar conceitos de Big Data, Engenharia de Dados e Applied Analytics a um problema real de negócio.

---

## Objetivo

O objetivo do projeto é desenvolver uma solução analítica para organizar, processar e explorar os dados das pesquisas State of Data Brasil, identificando características, tendências e oportunidades relacionadas ao mercado brasileiro de Dados, Analytics e Inteligência Artificial.

O projeto contempla:

* ingestão e armazenamento dos dados no Amazon S3;
* organização dos dados nas camadas Bronze, Silver e Gold;
* desenvolvimento de processos ETL utilizando AWS Glue e Apache Spark;
* tratamento, padronização e preparação dos dados;
* catalogação das tabelas para facilitar sua descoberta e consulta;
* realização de análises exploratórias e consultas analíticas;
* geração de gráficos para apresentação dos resultados;


---

## Dataset

O projeto utiliza as três pesquisas mais recentes do State of Data Brasil, as bases reúnem informações sobre o perfil dos profissionais de Dados no Brasil, incluindo formação acadêmica, experiência profissional, remuneração, tecnologias utilizadas, entre outros.

### Pesquisas utilizadas

* State of Data Brasil 2023–2024;
* State of Data Brasil 2024–2025;
* State of Data Brasil 2025–2026.

**Fonte dos dados:** [Data Hackers — Datasets no Kaggle](https://www.kaggle.com/datahackers/datasets).

---

## Arquitetura da solução

A solução utiliza serviços da AWS para construir um fluxo de processamento de dados organizado em camadas, desde a ingestão até a disponibilização das informações para análises.

### Camada Bronze

A camada Bronze armazena os dados ingeridos em seu formato inicial de processamento, preservando a estrutura original de cada pesquisa. Nessa etapa, os arquivos são armazenados no Amazon S3 e disponibilizados por meio de tabelas registradas no AWS Glue Data Catalog.


### Camada Silver

A camada Silver é responsável pelo tratamento e pela padronização dos dados provenientes da camada Bronze.
Cada pesquisa foi processada considerando sua própria estrutura de origem, mantendo a identificação do respectivo período.

### Camada Gold

A camada Gold é responsável por disponibilizar os dados organizados para análises de negócio.
Nessa etapa, o objetivo é consolidar informações relevantes e preparar conjuntos de dados analíticos que facilitem a construção de indicadores e gráficos.

---

## Tecnologias utilizadas

* **Amazon S3:** armazenamento dos arquivos e das camadas do Data Lake.
* **AWS Glue:** processamento ETL e integração com o catálogo de dados.
* **AWS Glue Data Catalog:** catalogação e descoberta das tabelas.
* **Apache Spark / PySpark:** processamento distribuído e transformação dos dados.
* **AWS Glue Notebook:** desenvolvimento e execução dos processos de tratamento e análise.
* **Amazon Athena:** consultas analíticas SQL, conforme a evolução do projeto.
* **Draw.io:** documentação visual da arquitetura da solução.
* **Parquet:** formato de armazenamento dos dados processados.
* **Python:** linguagem utilizada na implementação dos processos de dados.


---

## Estrutura do projeto

A estrutura abaixo representa uma organização sugerida para o repositório, que poderá ser ajustada conforme os notebooks, arquivos e artefatos efetivamente desenvolvidos.

```text
tc03-state-of-data-analytics/
│
├── datasets/
│   ├── State of Data 2023 - Kaggle.csv
│   ├── State of Data 2024 - Kaggle.csv
│   └── State of Data 2025-2026 - Kaggle.csv
│
├── docs/
│   └── arquitetura.drawio
│
├── notebooks/
│   ├── 01_bronze_state_of_data.ipynb
│   ├── 02_silver_state_of_data.ipynb
│   └── 03_gold_state_of_data.ipynb
│
├── analises/
│   └── analises_athena
│
├── README.md
│
```


---

