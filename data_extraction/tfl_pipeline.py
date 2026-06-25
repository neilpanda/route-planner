from config import TFL_API_KEY
import pandas as pd
import requests

BASE_TFL_URL = "https://api.tfl.gov.uk"

# fetcher:

def fetch_tfl_data(end_point, extra_params=None):
    """Fetches a .json file containing API data for a given endpoint."""
    url = f"{BASE_TFL_URL}/{end_point}"
    params = {"app_key" : TFL_API_KEY}

    if extra_params: # uses this version to detect empty structures ie. {}
        params.update(extra_params)
    
    print(f"Fetching at {url}...")
    print()
    response = requests.get(url, params=params)

    try:
        response.raise_for_status()
        print("Fetch success!")
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"API error: {err}")
        return None
    
# parsers:

def parse_bikes():
    pass