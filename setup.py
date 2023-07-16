#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md") as file:
    read_me_description = file.read()

setup(
    name='emiliiak_calculator',
    version='0.1.1',
    packages=find_packages(),
    author='Emiliia Karpiuk',
    author_email='emiliiakarpiuk@gmail.com',
    description='A calculator package for performing basic arithmetic operations',
    url='https://github.com/emiliiak/turing-calculator.git',
)