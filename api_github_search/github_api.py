import requests

# calling the github api to search for python repositories
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}
response = requests.get("https://api.github.com/search/repositories", params=params)
data = response.json()

# printing repo name and stars
for repo in data["items"]:
    print("Name:", repo["name"])
    print("Stars:", repo["stargazers_count"])
    print()