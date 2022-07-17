import requests

session = requests.session()

request = session.get('https://yiffer.xyz/api/keywords')

print(request.json()) # Prints the response of the server