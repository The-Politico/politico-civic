Servers
-------

Civic provides a cli called ``onespot`` that handles server management
for you. 

To get it installed on your path, make sure your virtual
environment is activated, and run ``python setup.py develop``.

**IMPORTANT: Each ``onespot`` command takes a ``--target=production``
argument in order to make these commands run on the production server.
By default, the commands go to staging**.

You will also need to ensure that you have environment files for the
servers in your project. These are gitignored because they contain API
keys that we cannot leak to the public. In both the
``terraform/staging`` and ``terraform/production`` folders, you will
need both a ``.env`` file and a ``terraform.tfvars`` file. Talk to Tyler
if you don’t have these.

You can always run ``onespot help`` for information on the command line.

Provisioning
^^^^^^^^^^^^

Run these commands when you need to create new servers or push new code
to the servers.

Destroy server
''''''''''''''

``onespot server destroy``

Provision new server
''''''''''''''''''''

``onespot server launch``

Setup new server
''''''''''''''''

``onespot server setup``

Updating existing server
''''''''''''''''''''''''

``onespot server update``.

Running election nights
^^^^^^^^^^^^^^^^^^^^^^^

There are also ``onespot`` commands that help you set up an election
night. Most of these commands require a positional date argument,
formatted ``YYYY-MM-DD``, and an optional ``--test`` flag if you need to
interact with test data.

Initializing election night data
''''''''''''''''''''''''''''''''

``onespot election init <DATE>``

This will run elex and hydrate all of the models elex touches, as well as create the content model objects for
the eventual baked out pages.

Starting election night results processes
'''''''''''''''''''''''''''''''''''''''''

``onespot election start <DATE>``

Stopping election night results processes
'''''''''''''''''''''''''''''''''''''''''

``onespot election stop``