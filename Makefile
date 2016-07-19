GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

clean:
	rm -rf images/_build
	rm -rf _build

sigal:
	cd images && sigal build

build: sigal
	python -m urubu build
	touch _build/.nojekyll

serve:
	python -m urubu serve

publish:
	git subtree push --prefix _build origin gh-pages    

install:
	pip install urubu sigal awscli
