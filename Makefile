# Force install the latest production version of Quilt
inst:
	pip install -U quilt_lang
    
# Install the dependencies
deps:
    pip install -r requirements.txt

# Minify the code (Linux only)
min:
    pip install -pyminifier
    find quilt_lang -type f -name "*.py" -exec pyminifier --gzip --obfuscate-variables --outfile="{}" "{}" \;

# Generate the Mkdocs documentation
mdoc:
    pip install mkdocs mkdocs-material pymdown-extensions pygments
    mkdocs build --verbose --clean --strict

# Generate the Sphinx documentation
cdoc:
	pip install sphinx sphinx_materialdesign_theme
	cd docs-sphinx
	sphinx-build -b html rst html

# Build the PyPi package
pack:
    pip install setuptools-git-version setuptools wheel
    cd src
    python setup.py sdist bdist_wheel
