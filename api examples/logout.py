import requests

session = requests.session()

# Login would be here

request = session.get('https://yiffer.xyz/api/logout')

print(request.status_code) # Prints the response of the server