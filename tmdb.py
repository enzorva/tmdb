import urllib.request
import urllib.error
import argparse
import json

url = "https://api.themoviedb.org/3/authentication"

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkOWJmYThlZGIzZmM2M2ZjMGU5NzkwNmMyMjI0YTU2YiIsIm5iZiI6MTc0NTQxMTkxNC4zNiwic3ViIjoiNjgwOGRmNGEyNzZiZjY0ZTQxYWI1ZmFjIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.v7cdNS5UXdah9Y3c3nDmBt2izyixytkUB1o2oBRmMpE'
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