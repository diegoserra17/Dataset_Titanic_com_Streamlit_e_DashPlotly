# Dashboard Titanic & Machine Learning

Este projeto consiste em uma aplicação web interativa desenvolvida em **Python** utilizando **Dash** e **Dash Bootstrap Components**, integrada a um modelo preditivo de **Machine Learning** baseado no famoso dataset do **Titanic**, cedido pela Universidade de Stanford e amplamente utilizado em estudos de aprendizado de máquina.

O objetivo da aplicação é explorar visualmente os dados demográficos e de sobrevivência dos passageiros, além de fornecer páginas estruturadas para formulários interativos e predições baseadas em inteligência artificial.

---

## Funcionalidades da Aplicação

* **Navegação Multipágina:** Sistema integrado de rotas utilizando `dcc.Location` para alternar dinamicamente entre as páginas do dashboard.
* **Módulo de Gráficos e EDA:** Visualização da distribuição de idades, taxas de sobrevivência e outras análises exploratórias do Titanic com Plotly, Matplotlib e Seaborn.
* **Formulários Interativos:** Funcionalidades práticas embutidas na aplicação (como cálculo automatizado de IMC através de inputs e states com callbacks do Dash)[cite: 3].
* **Modelo Preditivo (Machine Learning):** Classificador treinado com **XGBoost** para prever a sobrevivência de passageiros com base em características como classe, idade, tarifas e gênero.

---

## Estrutura do Repositório

```text
├── app.py              # Inicialização padrão da aplicação Dash com Bootstrap Theme[cite: 1]
├── main.py             # Arquivo principal de rotas e layout estrutural do Dashboard[cite: 4]
├── form.py             # Módulo de formulários, inputs e callbacks interativos (ex: cálculo de IMC)[cite: 3]
├── modelo.py           # Script de tratamento de dados, treinamento do modelo XGBoost e exportação
├── dados.ipynb         # Jupyter Notebook contendo a análise exploratória inicial dos dados do Titanic[cite: 2]
├── model_titanic.pkl   # Artefato serializado do modelo treinado (`joblib`)[cite: 5, 6]
├── .gitignore          # Arquivos e pastas ignoradas pelo controle de versão (ex: ambientes virtuais)[cite: 7]
└── README.md           # Documentação do projeto 
```
---

### Tecnologias e Bibliotecas Utilizadas

Python 3.10+

Plotly Dash / Dash Bootstrap Components (Interface web e componentes visuais)

Pandas & NumPy (Manipulação e estruturação de dados)

Plotly, Matplotlib & Seaborn (Gráficos e visualizações estatísticas)

Scikit-Learn & XGBoost (Pré-processamento, divisão de bases e modelagem preditiva)

Joblib (Persistência e salvamento do modelo treinado)

### Como Executar o Projeto Passo a Passo

Siga os procedimentos abaixo para configurar o ambiente e rodar o dashboard localmente:

## 1. Clonar o Repositório e Acessar a Pasta

Abra o seu terminal de preferência na pasta do projeto.

## 2. Criar e Ativar o Ambiente Virtual

Recomenda-se isolar as dependências utilizando um ambiente virtual:

### Criando o ambiente virtual
python -m venv venv

### Ativando no Windows
venv\Scripts\activate

### Ativando no Linux/macOS
source venv/bin/activate


## 3. Instalar as Dependências

Instale as bibliotecas necessárias para rodar o painel e os scripts de machine learning:

pip install dash dash-bootstrap-components pandas numpy scikit-learn xgboost plotly matplotlib seaborn joblib


## 4. Executar o Treinamento do Modelo (Opcional)

Caso queira gerar ou atualizar o arquivo binário do modelo preditivo a partir da base de dados de Stanford:

python modelo.py


## 5. Iniciar a Aplicação Dash

Execute o arquivo principal para colocar o servidor de desenvolvimento do dashboard no ar:

python main.py


Com o servidor rodando, abra o navegador e acesse o link local indicado no terminal (geralmente http://127.0.0.1:8050/).

📊 Sobre a Base de Dados

O conjunto de dados utilizado é proveniente do repositório educacional da Universidade de Stanford (CS109). Ele traz informações limpas e estruturadas sobre os passageiros a bordo do RMS Titanic, sendo uma referência clássica para introdução a técnicas de engenharia de dados e algoritmos de classificação.

👤 Autor

Desenvolvido por Diego Serra.
