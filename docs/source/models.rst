Models
======

almanac
-------

Almanac uses the Democrats' election calendar to discern distinct statewide election events that happen on particular election days.

:code:`ElectionEvent`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: almanac.models.ElectionEvent


demography
----------

Demography collects and aggregates Census variables by the political divisions defined in Geography.

:code:`CensusEstimate`
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: demography.models.CensusEstimate

:code:`CensusLabel`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: demography.models.CensusLabel

:code:`CensusTable`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: demography.models.CensusTable

:code:`CensusVariable`
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: demography.models.CensusVariable


election
--------

Election models information about races for particular offices. It also models candidate information, which inherits people from Entity and attaches them to races in Election.

:code:`BallotAnswer`
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.BallotAnswer

:code:`BallotMeasure`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.BallotMeasure

:code:`Candidate`
~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.Candidate

:code:`CandidateElection`
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.CandidateElection

:code:`Election`
~~~~~~~~~~~~~~~~
.. autoclass:: election.models.Election

:code:`ElectionCycle`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.ElectionCycle

:code:`ElectionDay`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.ElectionDay

:code:`ElectionType`
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: election.models.ElectionType

:code:`Race`
~~~~~~~~~~~~
.. autoclass:: election.models.Race


electionnight
-------------

Election Night builds live results pages based on AP data and models the text content needed on those pages.

:code:`APElectionMeta`
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.APElectionMeta

:code:`CandidateColorOrder`
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.CandidateColorOrder

:code:`PageContent`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.PageContent

:code:`PageContentBlock`
~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.PageContentBlock

:code:`PageContentType`
~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.PageContentType

:code:`PageType`
~~~~~~~~~~~~~~~~
.. autoclass:: electionnight.models.PageType


entity
------

Entity houses models for people and organizations. For example, the Republican Party is an organization, and Mitt Romney is a person. Their roles as political parties and candidates will come in downstream apps, but Entity houses the base level information about them.

:code:`ImageTag`
~~~~~~~~~~~~~~~~
.. autoclass:: entity.models.ImageTag

:code:`Organization`
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: entity.models.Organization

:code:`OrganizationClassification`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: entity.models.OrganizationClassification

:code:`OrganizationImage`
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: entity.models.OrganizationImage

:code:`Person`
~~~~~~~~~~~~~~
.. autoclass:: entity.models.Person

:code:`PersonImage`
~~~~~~~~~~~~~~~~~~~
.. autoclass:: entity.models.PersonImage


geography
---------

Geography houses models for all of the geographic political divisions in the United States. It contains bootstrap scripts that get shapefiles from the Census Bureau for states, counties and congressional districts and load them into your database. It also creates a simplified geography for each of those objects.

:code:`Division`
~~~~~~~~~~~~~~~~
.. autoclass:: geography.models.Division

:code:`DivisionLevel`
~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: geography.models.DivisionLevel

:code:`Geometry`
~~~~~~~~~~~~~~~~
.. autoclass:: geography.models.Geometry

:code:`IntersectRelationship`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: geography.models.IntersectRelationship


government
----------

Government contains information about political jurisdictions, bodies, and offices. For example, the United States Federal Government is a jurisdiction, the U.S. Senate is a body, and the Class 1 Senate seat from Texas is an office. It also contains the modeling for political parties.

:code:`Body`
~~~~~~~~~~~~
.. autoclass:: government.models.Body

:code:`Jurisdiction`
~~~~~~~~~~~~~~~~~~~~
.. autoclass:: government.models.Jurisdiction

:code:`Office`
~~~~~~~~~~~~~~
.. autoclass:: government.models.Office

:code:`Party`
~~~~~~~~~~~~~
.. autoclass:: government.models.Party


vote
----

Vote models various types of voting that happens in elections.

:code:`Delegates`
~~~~~~~~~~~~~~~~~
.. autoclass:: vote.models.Delegates

:code:`ElectoralVotes`
~~~~~~~~~~~~~~~~~~~~~~
.. autoclass:: vote.models.ElectoralVotes

:code:`Votes`
~~~~~~~~~~~~~
.. autoclass:: vote.models.Votes