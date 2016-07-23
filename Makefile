GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

clean:
	rm -rf images/fotos
	rm -rf _build

sigal:
	cd images && sigal build

build: sigal
	python -m urubu build
	touch _build/.nojekyll

serve:
	python -m urubu serve

publish: clean
	./_publish.sh	

install:
	sudo pip install urubu sigal awscli
