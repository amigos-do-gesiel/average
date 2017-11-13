from python:3.5
run mkdir /average
workdir /average
add . /average/
run python3 setup.py install && \
    average --version
cmd average