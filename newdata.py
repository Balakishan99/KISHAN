#author Balakishan Molankula
import splunklib.client as client # need splunk sdk and libraries 

HOST = "xx.xx.xx.xx"
PORT = 8089
USERNAME = "xxxxxx"
PASSWORD = "xxxxxxxxx"

# Create a Service instance and log in 
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)
print "waiting to connect -_-"
# Print installed apps to the console to verify login
for app in service.apps:
    print app.name
