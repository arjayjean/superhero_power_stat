import subprocess
import requests
import json

subprocess.run('clear')

URL = f'https://akabab.github.io/superhero-api/api/all.json'

# Requesting
response = requests.get(URL)

# Status code
status = response.status_code

# API data stored in json
data = response.json()
# print(data)

# Storing the API data in a JSON file
with open('data/superhero_api.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Extraction status
print("\n[Extract] Start")
print(f'[Response] {status}')  
print("[Extract] Ended\n")

