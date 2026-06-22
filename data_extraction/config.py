"""
Acts as a hub for all global constants and configurations.

Any changes made to these constants and/or configurations should be altered here.
"""
import os
import dotenv

dotenv.load_dotenv()
TFL_API_KEY = os.getenv("TFL_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

MAXIMUM_WALKING_DISTANCE_METERS = 10000 # m
MAXIMUM_CYCLING_DISTANCE_METERS = 50000 # m
