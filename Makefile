test:
	python ./setup.py nosetests
lint:
	python ./setup.py lint
pep8:
	python ./setup.py pep8
check: test lint pep8
deb:
	fpm -s python -t deb -f .
doc:
	sphinx-apidoc -F -H "python-example" example -o docs
	python ./setup.py build_sphinx -E -s docs --build-dir docs
clean:
	rm -rf .eggs example/__pycache__ tests/__pycache__ *.egg-info */*.pyc
