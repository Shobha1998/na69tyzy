from distutils.core import setup
from setuptools import find_packages

setup(name='idm_id',
      version='0.1',
      author='DSSS',
      author_email='shobha.rajanna@fau.de',
      packages=find_packages(),
      install_requires=['numpy','Pillow','ipywidgets'])
      