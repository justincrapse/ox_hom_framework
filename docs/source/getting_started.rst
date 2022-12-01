.. image:: images/index/under_construction.jpg
    
Getting Started
===============



*this should be in italics*
**this should be bold**
``this is a code example``
text with **bold text** in the middle 
text with\ **bold text**\ in the middle with escaped spaces

* this
* is a list

    * and this is nested

* and this is original list 

#. This is a numbered list
#. another entry

    #. sub entry in numbered list

My Term
    definition of my Term

    more stuff

Next Term
    description

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

.. image:: images/my_test.jpg
   :width: 600
   :alt: alt text here

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
bloogers

