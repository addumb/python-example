test:
	python ./setup.py nosetests --with-coverage --cover-package example
doc: test
	sphinx-apidoc -F -H "python-example" example -o doc
	python ./setup.py build_sphinx -E -s doc --build-dir doc
