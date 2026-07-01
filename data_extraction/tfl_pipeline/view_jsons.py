from data_extraction.tfl_pipeline.fetcher import fetch_tfl_data
import json

end_point = "Bikepoint"
extra_params = None

raw_json = fetch_tfl_data(end_point, extra_params)

if raw_json:
    first_station = raw_json[0]
    print(json.dumps(first_station, indent=4))
