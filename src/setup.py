# Import setuptools module
import setuptools

# Parse the readme markdown file
with open("../README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="quilt-lang",
    version="0.4.26",
    author="Richie Bendall",
    author_email="richiebendall@gmail.com",
    description=
    "A Python library that lets you write less code to do more things.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Richienb/quilt",
    packages=setuptools.find_packages(),
    install_requires=['clipboard', 'colour', 'loremipsum'],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)
