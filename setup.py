'''
If finding anything ambiguous while writing this `setup.py`,
please refer to the following:
    https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide
'''
from setuptools import setup, find_packages

setup(name='devlog',
      version='0.0',
      packages=find_packages(),
      install_requires=[],

      # metadata for upload to PyPI
      author="Joonsang Jo",
      author_email="needoptimism@gmail.com",
      description="This is a personal devlog application",

      # setup_requires=["a", "b"]
      # A string or list of strings specifying what other distributions need to be present in order for the setup script to run.

      # could also include long_description, download_url, classifiers, etc.

)


