clean:
	rm -rf *.egg
	find . -name '*.py[co]' -print -exec rm {} \;
test:
	python setup.py nosetests 
doc:
	sphinx-apidoc -F -H "python-example" example -o docs
	python setup.py build_sphinx -E -s docs --build-dir docs
install:
	python setup.py install \
		--root=debian/addumb-example/opt/example \
		--install-base=. \
		--install-purelib=. \
		--install-platlib=. \
		--install-lib=. \
		--install-scripts=. \
		--install-data=data \
		--install-headers=lib
