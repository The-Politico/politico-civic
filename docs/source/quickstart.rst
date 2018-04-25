Quickstart
==========

1. Install global dependencies for the project:

.. code-block:: shell
    $ brew install jq
    $ pip install pipenv

Get `Terraform <https://www.terraform.io/downloads.html>`__ from the
project website.

2. Create local PostgreSQL database

.. code-block:: shell
    $ createdb civic

3. Fill out your .env file

.. code-block:: shell
    DATABASE_URL=“postgresql://username:password@localhost:5432/civic”
    ...
    (get all of our API keys from someone on the team)

4. Install local dependencies for the project:

.. code-block:: shell
    $ pipenv install
    $ pipenv shell
    $ python setup.py develop

5. Bootstrap database

.. code-block:: shell
    $ python manage.py bootstrap_electionnight

6. Check it out!

.. code-block:: shell
    $ python manage.py runserver
