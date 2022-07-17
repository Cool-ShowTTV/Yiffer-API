import requests

session = requests.session()

request = session.get('https://yiffer.xyz/api/blogs')

for item in request.json(): #example on how to get all titles
    print(item['title'])