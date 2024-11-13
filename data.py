import requests, json

endpoint = "https://api.github.com/users/gabriel-victor933/repos"
repos = json.loads(requests.get(endpoint).text)

print(repos)