from setuptools import setup, find_packages


setup(
    name="example",
    version=0.5,
    description="An example python project.",
    author="Adam Gray",
    author_email="adam@addumb.com",
    packages=find_packages(exclude=["tests*"]),
    setup_requires=[
        "nose",
        "sphinx<1.4",
        "sphinxcontrib-napoleon",
        "setuptools-pep8",
        "setuptools-lint",
    ],
    scripts=["examplescript"],
    tests_require=["nose", "coverage", "sphinx", "sphinxcontrib-napoleon"],
    install_requires=["python-dateutil",],  # Just an example...
)
