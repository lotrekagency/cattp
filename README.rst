Installation
------------

.. code-block:: sh

   pip install cattp

Usage
-----

.. code-block:: python

   from cattp.http import HttpCatResponse

   def my_view():
       return HttpCatResponse(status_code=200)

Run tests
---------

.. code-block:: sh

   $ pip install -r requirements-dev.txt
   $ make test
