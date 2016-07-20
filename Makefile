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

publish: clean build
	aws s3 cp _build  s3://www.anneliesbuyssens.be/ --recursive --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers    

install:
	pip install urubu sigal awscli
