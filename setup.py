import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='myicrypto',
    packages = ['myicrypto'],
    version = '0.2-alpha',
    license = 'Apache License 2.0',
    description = 'Algorithms in Crytography',
    author = 'Yi Lyu',
    author_email = 'marcolyu@g.ucla.edu',
    url = 'https://github.com/MarcoYLyu/myicrypto',
    download_url = 'https://github.com/MarcoYLyu/myicrypto/releases/tag/v_0.1-alpha',
    keywords = ['cryptography', 'math116'],
    install_requires=[
            'numpy'
    ],
    classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)