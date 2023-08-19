<img src="https://i.imgur.com/lQJojh4.png"/>

# 🛒 Super Mercado 🛍️


Este projeto permitirá que a rede de supermercados compreenda melhor as interações entre clientes e funcionários, identificando oportunidades de aprimoramento no atendimento. Aumentando a satisfação do cliente e melhorando a eficiência, a empresa poderá criar uma experiência mais positiva para seus clientes, promovendo a fidelização e o sucesso a longo prazo.A analise pode ser conferida [aqui](https://github.com/Jandersolutions/super_mercado/blob/main/notebooks/projeto.ipynb)  🌟🤝

## Inicializando o projeto 🚀

- Clone o projeto: ```git clone https://github.com/Jandersolutions/super_mercado.git```
- Crie uma máquina virtual: ```python -m venv myvenv```
- Ative a máquina virtual: ```source myvenv/bin/activate```
- Instale as requisições: ```pip install -r requirements.txt```
- Abra o JupyterLab: ```jupyter-lab``` 📊🔬

## Materiais e links 📕
------------
| Material | Link |
|---------|------|
| Notebook | https://github.com/Jandersolutions/super_mercado/blob/main/notebooks/projeto.ipynb |
| Gerador de Dataset¹ | https://github.com/Jandersolutions/super_mercado/blob/main/src/data/geraDatasetVendas.py |
| Dataset | https://github.com/Jandersolutions/super_mercado/blob/main/data/raw/venda_07-2023.csv |
| Cookiecutter Data Science | https://drivendata.github.io/cookiecutter-data-science/ |
| CRISP-DM | https://pt.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining |
| Faker | https://faker.readthedocs.io/en/master/ |
| Documentação do projeto |https://github.com/Jandersolutions/super_mercado/blob/main/references/descric%C3%A3o%20do%20projeto.pdf |
| Dicionário de dados | https://github.com/Jandersolutions/super_mercado/blob/main/references/dicionario%20dos%20dados.pdf |

1 artigo que publiquei sobre o gerador de dataset -> [artigo](https://web.dio.me/articles/gerador-de-dataset-sintetico-gere-seus-arquivos-csvs?back=%2Farticles&page=1&order=oldest)


## Como o projeto esta organizado  📚


    ├── LICENSE
    ├── Makefile           <- Makefile com comandos como make data ou make train
    ├── README.md          <- O README de nível superior para desenvolvedores que utilizam este projeto.o arquvo que você esta lendo
    ├── data
    │   ├── external       <- Dados de fontes de terceiros.
    │   ├── interim        <- Dados intermediários que foram transformados.
    │   ├── processed      <- Conjuntos de dados finais e canônicos para modelagem.
    │   └── raw            <- O dado original e imutável.
    │
    ├── docs               <- Um projeto Sphinx padrão; veja sphinx-doc.org para detalhes.
    │
    ├── models             <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos.
    │
    ├── notebooks          <- Notebooks Jupyter. A convenção de nomenclatura é um número (para ordenação),
    │                         
    │                         
    │
    ├── references         <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    │
    ├── reports            <- Análises geradas como HTML, PDF, LaTeX, etc
    │   └── figures        <-  Gráficos e figuras geradas para uso em relatórios
    │
    ├── requirements.txt   <- O arquivo de requisitos para reproduzir o ambiente de análise
    │                      
    │
    ├── setup.py           <- Torna o projeto instalável via pip (pip install -e .), para que src possa ser importado.
    ├── src                <- Código-fonte para uso neste projeto
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts para baixar ou gerar dados.
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts para transformar dados brutos em recursos para modelagem.
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts para treinar modelos e usar modelos treinados para fazer previsões
    │   │   │                
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts para criar visualizações exploratórias e orientadas por resultados.
    │       └── visualize.py
    │
    └── tox.ini            <- Arquivo tox com configurações para executar o tox; veja tox.readthedocs.io


--------

<p><small>Este projeto foi baseado nas melhores praticas <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
