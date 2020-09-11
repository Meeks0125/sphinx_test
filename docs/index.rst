.. SphinxTest documentation master file, created by
   sphinx-quickstart on Mon Sep  7 20:38:36 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SphinxTest's documentation!
======================================

.. toctree::
   :maxdepth: 2

   a/index
   b/index

inline markup *emphasis text* **strong text** ``code sample``
``a = b + c``

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

   * with a nested list
   * and some subitems

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

John Doe wrote::

>> Great idea! is not
>
> Why didn't I think of that?
> You just did!  ;-)

| These lines are
| broken exactly like in
| the source file.

This is a typical paragraph.  An indented literal block follows.

::

    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print a
    print "it's..."
    # a literal block continues until the indentation ends

Doctest blocks

>>> 1 + 1
2

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

`<https://domain.invalid/>`

This is a paragraph that contains `a link`_.

.. _a link: https://domain.invalid/

############# 
for parts
############# 

*************
for chapters
*************

============ 
for sections
============ 

----------------
for subsections
----------------

^^^^^^^^^^^^^^^^^^^^^^^^ 
for subsubsections
^^^^^^^^^^^^^^^^^^^^^^^^   

""""""""""""""""""""""""
for paragraphs
""""""""""""""""""""""""


   :Date: 2001-08-16
   :Version: 1
   :Authors: - Me
             - Myself
             - I
   :Indentation: Since the field marker may be quite long, the second
      and subsequent lines of the field body do not have to line up
      with the first line, but they must be indented relative to the
      field name marker, and they must line up with each other.
   :Parameter i: integer

.. strong test

:strong:`strong test`

If [#note]_ is the first footnote reference, it will show up as
"[1]".  We can refer to it again as [#note]_ and again see
"[1]".  We can also refer to it as note_ (an ordinary internal
hyperlink reference).

.. [#note] This is the footnote labeled "note".

[#]_ is a reference to footnote 1, and [#]_ is a reference to
footnote 2.

.. [#] This is footnote 1.
.. [#] This is footnote 2.
.. [#] This is footnote 3.

[#]_ is a reference to footnote 3.

.. note:: This is a note

   - Here is a bullet list.

.. warning:: This is a warning

   - Here is a bullet list.

.. hint:: This is a hint

   - Here is a bullet list.

.. danger:: This is a danger

   - Here is a bullet list.

.. error:: This is a error

   - Here is a bullet list.

.. tip:: This is a tip

   - Here is a bullet list.

.. caution:: This is a caution

   - Here is a bullet list.

.. image:: 1.jpg
.. figure:: 2.jpg

   Cristiano Ronaldo

.. function:: foo(x)
              foo(y, z)
   :module: some.module.name

   Return a line of text input from the user.

The |biohazard| symbol must be used on containers used to
dispose of medical waste.

.. |biohazard| image:: biohazard.jpeg

.. meta::
   :description: The Sphinx documentation builder
   :keywords: Sphinx, documentation, builder

.. meta::
   :keywords: backup
   :keywords lang=en: pleasefindthiskey pleasefindthiskeytoo
   :keywords lang=de: bittediesenkeyfinden


Copyright |copy| 2003, |BogusMegaCorp (TM)| |---|
all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign
.. |BogusMegaCorp (TM)| unicode:: BogusMegaCorp U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
