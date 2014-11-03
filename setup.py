from setuptools import setup, find_packages

setup(name='example',
      version=0.1,
      description='An example python project.',
      author='Adam Gray',
      author_email='adam@addumb.com',
      packages=find_packages(exclude=["tests*"]),
      setup_requires = ['nose>=1.3.0', 'sphinx', 'sphinxcontrib-napoleon'],
      scripts=['examplescript'],
      tests_require = [
          'nose>=1.3.0',
          'coverage',
          'mox',
          'sphinx',
          'sphinxcontrib-napoleon'
          ],
      install_requires = [
          'python-dateutil'
      ]
    )

