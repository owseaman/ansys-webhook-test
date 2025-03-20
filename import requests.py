import requests
import json

# Define the headers as a Python dictionary
headers = {
    'Content-type': 'application/json',
    'X-Automation-Webhook-Token': '021458c07124f92e6a50860784d5b3f4daaeeb9e'
}

# Define the webhook URL
url = 'https://api-private.atlassian.com/automation/webhooks/jira/a/426b94c7-ccb3-4be5-b9a2-e9d7f68ca87f/0195aa58-cbbb-7e07-8bd3-be692afa8c6b'

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