from config import TFL_API_KEY
import pandas as pd
import requests

BASE_TFL_URL = "https://api.tfl.gov.uk"

# fetcher:

def fetch_tfl_data(end_point, extra_params=None):
    url = f"{BASE_TFL_URL}/{end_point}"
    params = {"app_key" : TFL_API_KEY}

    if extra_params is not None:
        params.update(extra_params)
