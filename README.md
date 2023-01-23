# Zscaler - Internet Access
## URL Category [User Defined] {urlcatmaker}

## Background
This script was created to apply organisation wide URL listing for specific location groups. Without the use of Cloud App Control.
The end goal is the script will ingest manually formatted logs that are exported from Zscaler Web Analytics Logging feature [max 92days as of 23/01/23],
and produce *.txt files based off the location.

## Steps [logging information]
1. 'Access Zscaler Internet Access Administrator' portal
2. Browse to 'Analytics'
3. Select 'Insights - Web Sights'
4. Select 'Logs' [check you have the right permissions if you cannot see it]
5. Filter for the logs you require and export as CSV [rinse and repeat if there is a specific filter applied that has more than one group]
6. Open up the exported *.csv then remove the first four rows [Administrator, Report Created, Locations and Location]
7. Delete all but these three columns [User, URL, Policy Action]
8. Filter out based on "Policy Action" if you are planning on whitelist/blacklist methodology.
9. Save *.csv
10. Install 'requirements.txt'
11. Run the script & GLHF





#### Note
This script can easily be reconfigured for any two columns or more, just make the right changes 😀 .
