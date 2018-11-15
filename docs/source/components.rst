Using component apps in Django
==============================

The component apps in politico-civic are designed to be plug-and-play. You can install any of them in your own Django project and they should work within your project and install all their necessary dependencies. Each app contains its own bootstrap management command that will seed your models with real data.

For example, let's install ``politico-civic-vote`` in a Django project. You can follow these steps for any of POLITICO Civic's component apps.

First, you need to set up your Django project with a PostgreSQL database. Read the `Django docs on databases <https://docs.djangoproject.com/en/2.1/topics/install/#database-installation>`__ if you don't know how to do this.

Then, install the component application.

``$ pip install politico-civic-vote``

In your Django settings, add the app *and its dependencies* to your ``INSTALLED_APPS`` section. Consult the dependency diagram in the quickstart section to determine your dependencies.

.. code-block:: python
  
    INSTALLED_APPS = [
        ...
        "rest_framework",
        "entity",
        "geography",
        "government",
        "election",
        "vote",
    ]

Then, migrate your database.

``$ python manage.py migrate``

No matter which component app you choose to install, you can use a Django management command to seed your database with real data. For ``politico-civic-vote``, the command is ``bootstrap_vote``. The naming convention extends to whichever app you isntalled. Each component app will seed its own data and the data of the apps it depends on.

Run the management command like this:

``$ python manage.py bootstrap_vote``

.. note::
    If you use anything depending on ``politico-civic-government``, you will need an API key from the `ProPublica Congress API <https://projects.propublica.org/api-docs/congress-api/>`__. Export it into your environment as ``PROPUBLICA_CONGRESS_API_KEY``.

That's it! Open your Django admin and see your seed data.