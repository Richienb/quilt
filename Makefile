install:
	pip install -U quilt_lang

doc:
	pip install sphinx
	cd docs-sphinx
	sphinx-build -b html rst html
