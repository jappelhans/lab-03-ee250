import requests
from typing import Dict

# connect to a "real" API

## Example: Official Joke API
URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke() -> Dict:
    res = requests.get(URL)
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def main():

    for i in range(0,5):
        joke = get_joke()
        print("Category: ", joke["type"])
        print("Setup:    ", joke["setup"])
        print("Punchline:", joke["punchline"])
        print()



if __name__ == "__main__":
    main()

