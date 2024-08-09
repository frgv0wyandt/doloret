import requests

# Make a GET request to an API
response = requests.get('https://www.example.com Parse the JSON response
data = response.json()

# Now you can access the data as a Python dictionary
print(data['key'])
