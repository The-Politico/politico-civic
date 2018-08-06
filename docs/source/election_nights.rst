Running an election night
-------------------------

Here's a complete guide to running elections.

The Friday before
'''''''''''''''''

Consult the instructions on publishing zeroes below.


The day before
''''''''''''''

Email Scott asking for lead graphs for each of the election pages. Usually he will get these to you by the next morning.

You should also draft your Tuesday morning link email so you're not scrambling the next morning. It should contain the following:

1. Links to each results page and links to the share image for each page. The social image link is predictable: ``https://www.politico.com/election-results/2018/cdn/img/2018/share/<state postal code>/share.jpg``.
2. Link to the live chat, if we're running one.
3. Results embed codes for all statewide races (Senate and governor). The embed is a standard Pym embed, and the URL is constructed as follows: ``https://www.politico.com/interactives/2018/embed/civic-homepage-embed/graphics/graphic.html?state=<STATE FIPS CODE>&id=<RACE ID>&type=<OFFICE TYPE>``. You can get the race id from the production pages by inspecting the results tables. The class of the wrapping ``<article>`` is ``race-table-<RACE ID>``. The office type is either ``senate`` or ``governor``. You can check these URLs directly to make sure maps load.
4. A link list embed for the homepage that links to all of our results pages. You can follow `this format <https://gist.github.com/TylerFisher/f09b7660c412507d4d8fe1d0a924da5b>`_, just change all the links to your current pages.


Mornings
''''''''

**Server setup**

1. Set up the production server. In the ``politico-civic`` repo, set the ``server_size`` variable in ``terraform/production/terraform.tfvars`` to a larger size for the day. The size will depend on the number of elections, but I usually go no smaller than a ``t2.large``.
2. Run ``onespot server launch --target=production``. This will upgrade the size of the production server.
3. Run ``onespot server update --target=production``. This will ensure that the latest version of Civic is on the server.
4. Run ``onespot election init <DATE> --target=production``. This bootstraps the initial data for your election date on the production server.
5. Login to the admin and put Scott's content on each of the pages. Go to the `page contents admin <https://civic.politicoapps.com/admin/electionnight/pagecontent/>`_ and search for the page location for each state. It should look like ``2018/<state-slug>/``. On the page, put Scott's content in a ``before-results`` content type block and a ``live-results`` content-type block. In the ``before-results`` block, I also add the poll closing time and first results expected time, which you will find in the Election Day Advisory email from the AP.
6. Start the daemons by running ``onespot election start <DATE> --target=production``.
7. Fire up two terminals and ssh into the production server on both. Tail the logs for each daemon by running ``tail -f /var/log/politico-civic/results.log`` and ``tail -f /var/log/politico-civic/reup.log``. Watch the processes run a few times and check for errors. A note: the reup process republishes the pages and contextual data every five iterations. Wait for that to happen, and then check your published pages to see the content blocks publish. 

If you have no errors, close the logs and get off the server.

**The morning email**

The next thing to do is to send the morning email you drafted to TP-Webteam, Paul, Ali, Annie, Mitch, Jon and Lily with all of our links for the day. Just double check the race IDs in your embed codes to make sure AP hasn't changed any IDs on us.


Evenings
''''''''

1. Before polls close in your first state, open your logfiles again. Open our production pages and our competitors (NYT, WaPo, etc.) while awaiting first results.
2. Nervously wait for first results. Wait. Wait. Wait.
3. Watch our results load faster than everyone else's. 

**What to watch for**

1. Weirdness in the AP data. Look for candidates flipping vote totals, unexpected blowouts, or way too many votes in a particular county or district. Those kinds of things can mean a tabulation error on AP's end. If anything weird persists, reach out to the AP.
2. Race calls. You should get Slack notifications for all of our race calls. When you see one, make sure @politicoelex tweeted.
3. SEO performance. We try to optimize for the "<STATE> election results 2018" search. See how we're performing against our competitors.
4. Chartbeat. See how our results pages are performing and how well they are recirculating with our live chats. If you see anything interesting, screenshot it so we can pass it along.

Leave the results daemons running overnight as AP finishes tabulating.


The day after
'''''''''''''

Leave the results daemons running until you get an End of Election Advisory email from the AP. Usually, this comes the afternoon after an election. Once you get that advisory:

1. Stop the results daemons by running ``onespot election finish --target=production``.
2. Downgrade the production server to a micro by changing the ``server_size`` variable in ``terraform/production/terraform.tfvars`` file to ``t2.micro``.
3. Run ``onespot server launch --target=production`` to complete the downgrade.


Onespot election commands
-------------------------

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