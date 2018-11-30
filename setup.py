from setuptools import setup, find_packages


setup(
    name='cattp',
    version='0.0.2',
    url='https://github.com/lotrekagency/cattp',
    install_requires=[],
    description="Django responses with cats from https://http.cat",
    long_description=open('README.rst').read(),
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
