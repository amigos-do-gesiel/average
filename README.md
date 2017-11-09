
=====
django-average
=====

Framework para acompanhamento e visualização de Estatísticas.
Informações detalhadas na wiki do repositorio.

Quick start
-----------

1. Adicione django-average ao seu INSTALLED_APPS, exemplo::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Inclua django-average URLconf na urls.py do seu projeto, exemplo::

    url(r'^polls/', include('polls.urls')),

3. Rode `python manage.py migrate` para criar as models do django-average.
