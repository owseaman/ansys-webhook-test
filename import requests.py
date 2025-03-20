import requests
import json

# Define the headers as a Python dictionary
headers = {
    'Content-type': 'application/json',
    'X-Automation-Webhook-Token': '*' ### Add your webhook token here
}

# Define the webhook URL
url = '*' ### Add your webhook URL here

try:
    # Make the POST request
    response = requests.post(url, headers=headers)

    # Print the response status code
    print(f"Status Code: {response.status_code}")

    # Print the response content (if any)
    if response.text:
        try:
            print("Response JSON:")
            print(json.dumps(response.json(), indent=4))
        except json.JSONDecodeError:
            print("Response Content:")
            print(response.text)

    # Raise an exception for bad status codes (optional)
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")