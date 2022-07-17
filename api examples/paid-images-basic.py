import requests

session = requests.session()

request = session.get('https://yiffer.xyz/api/paid-images-basic')

print(request.json()) #returns all the sponsored links and images

for item in request.json(): #example on how to loop through the json
    print(f'"{item["mainText"]}"', f'"{item["secondaryText"]}"', f'"{item["link"]}"')

for item in request.json(): #example on how to get all the images
    print(f'https://static.yiffer.xyz/pi/{item["id"]}.{item["filetype"]}')

#all ad types are card, banner, and topSmall