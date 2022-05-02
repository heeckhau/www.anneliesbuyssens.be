GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

clean:
	rm -rf images/fotos
	rm -rf _build

sigal:
	cd images && sigal build

build: sigal
	python3 -m urubu build
	touch _build/.nojekyll

serve:
	python3 -m urubu serve

publish: clean
	./_publish.sh	

install:
	sudo pip3 install urubu sigal awscli

# pip3 install --upgrade 'markdown < 3'

