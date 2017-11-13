# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='average',
    version='0.0.1',
    #packages=find_packages(exclude=("average",)),
    include_package_data=True,
    license='MIT License',  # example license
    description='Framework para acompanhamento e visualização de Estatísticas.',
    long_description=README,
    url='https://github.com/amigos-do-gesiel/average',
    author='amigos-do-gesiel',
    author_email='ulysses3353@gmail.com',

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    
    install_requires=[
        #"django"
    ],
    
    extras_require={
        'dev': [
            #'pytest==3.2.3'
        ],
    },
    
    entry_points = {
       "console_scripts": ["average = __main__:main"] 
    },
    # Other configurations
    #zip_safe=False,
    #platforms='any',
)
