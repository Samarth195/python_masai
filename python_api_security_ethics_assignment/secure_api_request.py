import os
import requests

api_key = os.getenv("API_KEY")

if not api_key:
    print("API key not found. Please set API_KEY in environment variables.")
else:
    url = "https://api.example.com/data"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.json())

        elif response.status_code == 429:
            print("Rate limit reached. Try again later.")

        else:
            print("Request failed", response.status_code)

    except requests.exceptions.RequestException:
        print("Request failed due to connection error")
# Note: The API endpoint is a placeholder. Exception handling is added
# to gracefully manage connection errors.