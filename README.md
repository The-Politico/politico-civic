![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# politico-civic


<img src="https://media3.giphy.com/media/zCNFcXsVRGhi/giphy.gif" width="400" />

## Server Setup

Civic provides a cli called `onespot` that handles server management for you. To get it installed on your path, make sure your virtual environment is activated, and run `python setup.py develop`.

##### Destroy server

To destroy the current server architecture, run `onespot server destroy`.

##### Provision new server

To create a new server, run `onespot server launch`

##### Setup new server

To setup a server you just created, run `onespot server setup`

##### Updating existing server

To update an existing server, push all of the latest code to Github. Then, run `onespot server update`.