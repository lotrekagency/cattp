<p align="center">
    <img src="https://raw.githubusercontent.com/lotrekagency/cattp/master/logo.jpg" alt="Cattp Logo" />
<p>

[![Latest Version](https://img.shields.io/pypi/v/cattp.svg)](https://pypi.python.org/pypi/cattp/)
[![codecov](https://codecov.io/gh/lotrekagency/cattp/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/cattp)
[![Build Status](https://travis-ci.org/lotrekagency/cattp.svg?branch=master)](https://travis-ci.org/lotrekagency/cattp)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lotrekagency/cattp/blob/master/LICENSE)

Django responses with cats from [http.cat](https://http.cat) 🐱

## Installation
```sh
pip install cattp
```

## Usage
```python
from cattp.http import HttpCatResponse

def my_view(request):
    return HttpCatResponse(status_code=200)
```



## Run tests
```sh
$ pip install -r requirements-dev.txt
$ make test
```
