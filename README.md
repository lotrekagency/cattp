<p align="center">
    <img src="https://raw.githubusercontent.com/lotrekagency/cattp/master/logo.jpg" alt="Cattp Logo" />
<br>
<a href="https://travis-ci.org/lotrekagency/cattp" target="blank">
<img src="https://travis-ci.org/lotrekagency/cattp.svg?branch=master"></a>
<a href="https://codecov.io/gh/lotrekagency/cattp">
  <img src="https://codecov.io/gh/lotrekagency/cattp/branch/master/graph/badge.svg" />
</a>
<p>

## Installation
```sh
pip install cattp
```

## Usage
```python
from cattp.http import HttpCatResponse

def my_view():
    return HttpCatResponse(status_code=200)
```



## Run tests
```sh
$ pip install -r requirements-dev.txt
$ make test
```
