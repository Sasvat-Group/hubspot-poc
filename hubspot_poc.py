from hubspot import HubSpot
import requests

####### hotspot
api_client = HubSpot(access_token='pat-na1-f28957a8-ad77-4d5d-af8f-06ef20720a91')

all_contacts = api_client.crm.contacts.get_all()

print(all_contacts)


##############Atera


url = 'https://app.atera.com/api/v3/customers?page=1'
headers = {'Accept': 'text/plain','X-API-KEY': 'f9e8df27950a4e80af07084f4ebbecda'}

print(requests.get(url, headers=headers))