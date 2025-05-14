#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Get the letter from command-line arguments or use an empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send the POST request with q as a parameter
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
