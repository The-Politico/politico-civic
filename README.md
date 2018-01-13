![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# politico-civic


<img src="https://media3.giphy.com/media/zCNFcXsVRGhi/giphy.gif" width="400" />


## Deployment to servers

To deploy code to the server, first commit your latest changes and push them to Github. Then, run:

```
$ fab master deploy_server
```

To run a Django management command on the server, run:

```
$ fab django.management:<management command>
```

Other things that might be useful:

- Restarting uwsgi: `fab servers.restart_service:uwsgi`
- Install requirements: `fab servers.install_requirements`
