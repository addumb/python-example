from setuptools import setup, find_packages

setup(name='example',
      version=0.5,
      description='An example python project.',
      author='Adam Gray',
      author_email='adam@addumb.com',
      packages=find_packages(exclude=["tests*"]),
      setup_requires=[
          'nose',
      ],
      scripts=['examplescript', 'run.py'],
      requires=open('requirements.txt').read().splitlines(),
      tests_require=[
          'flask',
          'nose',
          'coverage',
          'mox',
          ],
    )

