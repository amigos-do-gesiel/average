>## Average-framework

[![Build Status](https://travis-ci.org/amigos-do-gesiel/average.svg?branch=development)](https://travis-ci.org/amigos-do-gesiel/average)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/badge/python-3.5-orange.svg)](https://img.shields.io/badge/python-3.5-orange.svg)
[![Code Health](https://landscape.io/github/amigos-do-gesiel/average/master/landscape.svg?style=flat)](https://landscape.io/github/amigos-do-gesiel/average/master)
[![Coverage Status](https://coveralls.io/repos/github/amigos-do-gesiel/average/badge.svg?branch=development)](https://coveralls.io/github/amigos-do-gesiel/average?branch=development)

Framework para acompanhamento e visualização de Estatísticas.
Informações detalhadas na wiki do repositorio.

>## Quick start

1. Adicione django-average ao seu INSTALLED_APPS, exemplo::

```python
INSTALLED_APPS = [
    ...
    'polls',
]
```

2. Inclua django-average URLconf na urls.py do seu projeto, exemplo::

```python
url(r'^polls/', include('polls.urls')),
```

3. Rode `python manage.py migrate` para criar as models do django-average.
