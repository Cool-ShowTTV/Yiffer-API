import requests

session = requests.session()

request = session.get('https://yiffer.xyz/api/artists')

for item in request.json(): #example on how to get all names
    print(item['name'])