import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='yfhd',
    version='0.0.1',
    python_requires=">=3.8",
    description='Getting data from Yahoo Finance Historical Data',
    url='https://github.com/luizcalliari/Yahoo-Finance-Historical-Data.git',
    author='Luiz Antonio Calliari Filho',
    author_email='luizcalliari.filho@protonmail.com',
    license='wtfpl',
    long_description=read('README'),
    install_requires=[
        'numpy',
        'requests',
        'pandas',
        'pytest'
    ],
    packages=['yfhd'],
    zip_safe=False
)
