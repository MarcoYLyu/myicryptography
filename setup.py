import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
      name='math116',
      version='0.1dev',
      license='Apache License 2.0',
      packages=find_packages('math116'),
      description='Algorithms in Crytography',
      long_description=read('README.md'),
      url='https://github/marcoylyu/math116',
      install_requires=[
              'cython', 'numpy'
              ]
)