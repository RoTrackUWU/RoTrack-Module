# Made By The Developers At rotrack.xyz
import requests

username = input("Enter the Roblox username: ")
response = requests.get(f"https://api.rotrack.xyz/user?username={username}")
print(response.text if response.ok else f"Error: {response.status_code}")
# only four lines!
