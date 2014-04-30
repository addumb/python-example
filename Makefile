test:
	python ./setup.py nosetests --with-coverage --cover-package example
doc:
	sphinx-apidoc -F -H "python-example" example -o docs
	python ./setup.py build_sphinx -E -s docs --build-dir docs
