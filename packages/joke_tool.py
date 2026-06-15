import requests

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    except:
        return "Couldn't fetch joke right now."