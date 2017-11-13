from python:3.5
run mkdir /average
workdir /average
add . /average/
run pip install -r requirements.txt && python3 setup.py install
cmd average