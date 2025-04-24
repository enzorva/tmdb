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
    return None

def fetch_playing_now():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    return fetch_data(url)

def fetch_popular():
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    return fetch_data(url)

def fetch_top_rated():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    return fetch_data(url)

def fetch_upcoming():
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    return fetch_data(url)
    
parser = argparse.ArgumentParser(description='Fetch movie data from TMDB API.')
parser.add_argument('--popular', action='store_true', help='Fetch popular movies')
parser.add_argument('--top-rated', action='store_true', help='Fetch top rated movies')
parser.add_argument('--upcoming', action='store_true', help='Fetch upcoming movies')
parser.add_argument('--playing-now', action='store_true', help='Fetch movies currently playing in theaters')
args = parser.parse_args()

if args.popular:
    data = fetch_popular()
    if data:
        print(json.dumps(data, indent=4))
elif args.top_rated:
    data = fetch_top_rated()
    if data:
        print(json.dumps(data, indent=4))
elif args.upcoming:
    data = fetch_upcoming()
    if data:
        print(json.dumps(data, indent=4))
elif args.playing_now:
    data = fetch_playing_now()
    if data:
        print(json.dumps(data, indent=4))
else:
    print("Please specify an option: --popular, --top-rated, --upcoming, or --playing-now.")
    sys.exit(1)