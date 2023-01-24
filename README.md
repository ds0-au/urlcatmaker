# Zscaler - Internet Access
## URL Category [User Defined] {urlcatmaker}

## Background
This script was created to help apply organisation wide URL listing for specific location groups; for locations that cannot use Cloud App Control.
The script will ingest formatted logs, that are exported from Zscaler Web Analytics Logging feature and produce *.txt files based off the location.

## Steps [logging information]
1. 'Access Zscaler Internet Access Administrator' portal
2. Browse to 'Analytics'
3. Select 'Insights - Web Inights'
4. Select 'Logs' [check you have the right permissions if you cannot see it]
5. Filter for the logs you require and export as CSV [rinse and repeat if there is a specific filter applied that has more than one group]
6. Open up the exported *.csv then remove the first four rows [Administrator, Report Created, Locations and Location]
7. Delete all but these three columns [User, URL, Policy Action]
8. Filter out based on "Policy Action" if you are planning on whitelist/blacklist methodology.
9. Save *.csv
10. Install 'requirements.txt'
11. Run the script, enter the location of the *.csv & GLHF


## Steps [dedup.py]
1. From the export above you can run this script to ingest all of those files, to identify the duplicates/commonalities across the files and export as 'duplicates.txt' and then re-creates the input files but missing the duplicate URLs/IPs found.
2. Run the script
3. Select the file path
4. GLHF



#### Note
This script can easily be reconfigured for any two columns or more, just make the right changes 😀 .
