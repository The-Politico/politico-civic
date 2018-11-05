1. Upgrade servers to t2.2xlarge: update terraform production config and run `onespot server launch --target=production`
2. Update requirements: `onespot server update --target=production`
3. Bootstrap zeroes: `onespot election init 2018-11-06 --target=production`
4. Make changes to the following in the admin
    1. Bernie Sanders (VT), Angus King (ME), Bill Walker (AK-gov), Gary Johnson (NM-gov) should not be agreggable candidates
    2. Alyse Galvin (AK-AL) is a Democrat
5. Bake context: `fab production django.management:bake_elections 2018-11-06`
6. Test results processes:
    1. Run `onespot election start 2018-11-06`
    2. On east server, check `/var/log/politico-civic/state_results.log` and `/var/log/politico-civic/reup.log`
    3. On west server, check `/var/log/politico-civic/county-results.log`
    4. If all is well, make sure pages work