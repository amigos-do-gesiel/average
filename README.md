>## Average-framework

[![Build Status](https://travis-ci.org/amigos-do-gesiel/average.svg?branch=master)](https://travis-ci.org/amigos-do-gesiel/average)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-3.5-orange.svg)](https://img.shields.io/badge/python-3.5-orange.svg)
[![Code Health](https://landscape.io/github/amigos-do-gesiel/average/master/landscape.svg?style=flat)](https://landscape.io/github/amigos-do-gesiel/average/master)
[![Coverage Status](https://coveralls.io/repos/github/amigos-do-gesiel/average/badge.svg?branch=master)](https://coveralls.io/github/amigos-do-gesiel/average?branch=master)

<p align="justify">Average é um framework de código livre, seu objetivo é oferecer uma maneira simples para se gerar relatórios e gráficos. Teve inicio a partir da necessidade gerenciar doações da ONG providas, para que os administradores observem e policiem as doações recebidas, e façam planejamentos de acordo.</p>
<p align="justify"> Deve ser utilizado juntamente ao Django.</p>
<p align="justify"> O framework além de encapsular a criação de relatórios promove a reutilização de código, e se preocupa com o desempenho, toda vez que acontece uma alteração nos valores dos gráficos, existe um pre-processamento que evita gargalos quando necessários realizar cálculos. </p>  
<p align="justify"> Por default é possível gerar relatórios diários, mensais e anuais. Existe ainda a possibilidade de se criar relatórios variados, adaptando as necessidades envolvidas, caso seja necessário gerar relatórios para os últimos 45 dias, por exemplo, basta implementar a interface EstatisticTime, responsável por policiar os intervalos de tempos dos relatórios, ao implementar os métodos da interface é possível consumir os gráficos da aplicação que são do formato Json e Xml.</p>

>## Quick start

1. Adicione django-average ao seu INSTALLED_APPS, exemplo::

```python
INSTALLED_APPS = [
    ...
    'average',
]
```

2. Inclua django-average URLconf na urls.py do seu projeto, exemplo::

```python
url(r'^average/', include('average.urls')),
```

3. Rode `python manage.py migrate` para criar as models do django-average.
