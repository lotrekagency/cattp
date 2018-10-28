from setuptools import setup, find_packages
from m2r import parse_from_file


setup(
    name='cattp',
    version='0.0.1',
    url='https://github.com/lotrekagency/cattp',
    install_requires=[],
    description="Django responses with cats from https://http.cat",
    long_description=parse_from_file('README.md'),
    license="MIT",
    author="Lotrek",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
