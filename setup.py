import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pydropbox_fdw',
    version='0.0.2',
    description=('dropbox fdw for postgresql'),
    long_description=read('README.rst'),
    author='Dmitriy Olshevskiy',
    author_email='olshevskiy87@bk.ru',
    license='MIT',
    keywords='dropbox postgres pgsql fdw wrapper',
    packages=['pydropbox_fdw'],
    install_requires=['dropbox'],
    url='https://github.com/olshevskiy87/pydropbox_fdw'
)
