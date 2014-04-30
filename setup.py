from setuptools import setup, find_packages

setup(name='example',
      version=0.5,
      description='An example python project.',
      author='Adam Gray',
      author_email='adam@addumb.com, akshay@quixey.com',
      packages=find_packages(exclude=["tests*"]),
      setup_requires = ['sphinx', 'sphinxcontrib-napoleon'],
      scripts=['examplescript'],
      tests_require = [
          'nose>=1.3.0',
          'coverage',
          'mox',
          'sphinxcontrib-napoleon'
          ],
      install_requires = [
          'python-dateutil'
      ]
    )

