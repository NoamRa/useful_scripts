## Two scripts to give better understanding of network response time.

### check_internet_connection.py 
Every x seconds, send head request to a list of IPs or domain address and writes to csv.
If a number is added when calling the script it will limit the amount of requests. Otherwise it will run indefinitely.
test interval, and domain list are configureable inside the script

### plot_internet_connection.py 
Uses the csv created by check_internet_connection.py to generates a plot. Will open a local html file.
Requires pandas and plotly.
