Stuff Tracker
#############
:Author: Roie Black
:Email: roie.black@gmail.com
:Docs: https://rblack42.github.io/stuff-tracker

..  start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github| |coverage| |black|

.. |coverage| image:: https://coveralls.io/repos/github/rblack42/math-magik/badge.svg?branch=main
    :target: https://coveralls.io/github/rblack42/math-magik?branch=main
    :alt: Code Coverage"

..  image:: rst/_static/lpp.gif
    :align: center
    :width: 600

.. i|black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. end-badges


This project was created to help catalog all of my personal and professional
"stuff". At present, it is set to track books, and physical gadgets found in my
home and shop. All of this stuff is cataloged in different categories to aid in
location things.

The application developed here is a basic Python Flask application that can be
run on a local laptop. All items in the catalog are stored in a **sqlite3**
database. Access to this database is managed by a *Flask-Restful* API which
runs on my development laptop.

I tag all containers I use to store stuff with a QR label. The application
supports scanning a QR code using my iPhone, which brings up a web page showing
the contents of that container.
