import requests

response = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt&safe-mode")
print(response.text)
