# setup.py

from setuptools import find_packages, setup

setup(
  name='tp-python',
  version='1.0.0',
  packages=find_packages(),
  entrypoints={
    'console_scripts': [
      'tp-python=src.app.main',
    ],
  },
)