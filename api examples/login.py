import requests

session = requests.session()

# Username can be username or email
data = {'username': 'exampleLogin123', 'password': 'examplePassword123'}

request = session.post('https://yiffer.xyz/api/login', data=data)

print(request.text) # Prints the response of the server
print(request.cookies["yiffer_session"]) # Prints the cookie