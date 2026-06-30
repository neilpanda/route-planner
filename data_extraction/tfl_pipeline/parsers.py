
from data_extraction.tfl_pipeline.fetcher import fetch_tfl_data
from typing import Any
import pandas as pd
import numpy as np

# parsers:

# bike parser:
raw_json = fetch_tfl_data("Bikepoint")
def parse_bikes(raw_json: dict[str, float] | list[Any]):
    pass
