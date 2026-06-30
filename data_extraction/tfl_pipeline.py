from config import TFL_API_KEY
from typing import Any
import pandas as pd
import requests

BASE_TFL_URL = "https://api.tfl.gov.uk"

# fetcher:

def fetch_tfl_data(end_point: str, extra_params: dict[str, Any] | None = None):
    """_Acquires a JSON file from TFL API in the form of a url request._

    Args:
        end_point (_str_): _end of the URL request for data specific TFL API request._
        extra_params (_dict_, None): _contains extra parameters to include in the
        search. Defaults to None.

    Returns:
        response (_list or dict_): _the JSON response if successful_

    Raises:
        HTTPError (_exception_): _if unsuccessful_
    """

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

def parse_bikes(raw_json: dict[str, float] | list[Any]):
    pass
