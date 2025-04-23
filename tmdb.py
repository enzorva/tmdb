import urllib.request
import urllib.error
import argparse
import json
import os
from dotenv import load_dotenv
import sys

load_dotenv()

api_key = os.getenv('TMDB_API_KEY')

if not api_key:
    print("API key not found. Please set the TMDB_API_KEY environment variable.")
    sys.exit(1)

url = "https://api.themoviedb.org/3/authentication"

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + api_key,
}

def fetch_data(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            return json.loads(data)
    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e.msg}")

data = fetch_data(url)
if data:
    print(json.dumps(data, indent=4))