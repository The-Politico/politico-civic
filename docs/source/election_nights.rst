Running election nights
-----------------------

There are ``onespot`` commands that help you set up an election
night. Most of these commands require a positional date argument,
formatted ``YYYY-MM-DD``, and an optional ``--test`` flag if you need to
interact with test data.

Initializing election night data
''''''''''''''''''''''''''''''''

``onespot election init <DATE>``

This will run elex and hydrate all of the models elex touches, as well as create the content model objects for
the eventual baked out pages. Remember to pass ``--test`` if you need to use the test data from AP.

Starting election night results processes
'''''''''''''''''''''''''''''''''''''''''

``onespot election start <DATE>``

This command starts the results process and the reupload process. Remember to pass ``--test`` if you need to use the test data from AP.

Stopping election night results processes
'''''''''''''''''''''''''''''''''''''''''

``onespot election stop``

This command stops the results and reupload processes indiscriminately.

Finishing an election night
'''''''''''''''''''''''''''

``onespot election finish <DATE>``

This command stops the results and reupload processes, and then runs them one more time to ensure all races are marked as tabulated. Remember to pass ``--test`` if you need to use the test data from AP.


Publishing zeroes from your local computer
------------------------------------------

In order to publish zeroes from your local computer, first set up your local `politico-civic-election-night` app and database so that you can preview pages locally.

Then, run ``python manage.py prepare_zeroes <DATE> --test`` to set up your local database with the current election.

Visit the election page locally (for example, localhost:3000/runoff/2018/alabama/2018-07-17) and make sure everything looks correct. Most importantly, all results should be zeroed out.

If all looks good, you're ready to publish to production:

1. Go into your Django project's settings and set ``ELECTIONNIGHT_AWS_S3_BUCKET`` and ``ELECTIONNIGHT_AWS_S3_STATIC_ROOT`` to the production settings.
2. Run ``python manage.py collectstatic`` to ensure you have the latest JS and CSS for publishing.
3. Run ``python manage.py publish_zeroes <DATE> --test``.
4. Visit your new election pages on production and make sure they're correct.
5. Change your Django project settings back to staging, just in case ;).