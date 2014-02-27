all: build

build: bootstrap
	bin/buildout

bootstrap:
	if [ ! -f bin/buildout ] ; \
	then \
		python bootstrap.py ; \
	fi;

clean:
	-find . -type f -name "*.py[co]" -exec rm {} \;
	-find . -type d -name "__pycache__" -exec rm -r {} \;

superclean: clean
	-rm -rf \
		bin/ \
		develop-eggs/ \
		parts/ \
		*.egg-info/ \
		*.egg \
		log/ \
		/var/tmp/mixpanel-gevent-proxy-eggs

	-rm .installed.cfg

test: clean
	python setup.py test

public: test
	python setup.py sdist upload
