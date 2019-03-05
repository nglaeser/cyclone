from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='cyclone',
   version='1.0',
   description='Utilities for powers of cycle graphs',
   license="GPL",
   long_description=long_description,
   author='Noemi Glaeser',
   author_email='nglaeser@email.sc.edu',
   url="https://github.com/nglaeser/cyclone",
   packages=['cyclone'],  #same as name
   install_requires=['numpy', 'random'], #external packages as dependencies
)