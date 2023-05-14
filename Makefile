init:
    conda install -f enviroment.yml

test:
    py.test tests

.PHONY: init test