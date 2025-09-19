import requests
import json

url = 'https://randomuser.me/api/?results=5'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API Data Fetched Succssfully!\n")
    print(json.dumps(data, indent=4))

    users = []
    for user in data['results']:
        users.append({
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
        })

    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)
        print("\nProcessed user data saved to users.json")
else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")

    
