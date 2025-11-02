import requests

api_key = "P8p9BnUx95Q8nySurPYrp7wWtVS1noQ2"
query = "coding"
limit = 5

endpoint = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit={limit}"
response = requests.get(endpoint)

if response.status_code == 200:
    data = response.json()
    for gif in data["data"]:
        print(gif["images"]["original"]["url"])
else:
    print("Error:", response.status_code)
    print(response.text)
