super mercado
==============================

Este projeto permitirá que a rede de supermercados compreenda melhor as interações entre clientes e funcionários, identificando oportunidades de aprimoramento no atendimento. Aumentando a satisfação do cliente e melhorando a eficiência, a empresa poderá criar uma experiência mais positiva para seus clientes, promovendo a fidelização e o sucesso a longo prazo.

Como projeto esta organizado
------------

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
