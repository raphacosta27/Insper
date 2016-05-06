# Installing tox
$ pip install tox

# Running tests
$ tox

# Generating documentation
$ tox -e docs

# Uploading a new release
$ easy_install wheel twine
$ python setup.py sdist bdist_wheel
$ twine upload dist/*

# Copy docs to gh-pages
$ tox -e docs && mv docs/_build/html generated_docs && git clean -Xdi && git checkout gh-pages