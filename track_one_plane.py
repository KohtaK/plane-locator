import time
from datetime import datetime, timezone
from opensky_api import OpenSkyApi, TokenManager

SAMPLES = 10
INTERVAL = 15
BBOX = (37.70, 37.92, -122.35, -122.15)

def track_one_plane(api):
    response = api.get_states(bbox=BBOX)

    if response is None or not response.states:
        print("No planes found in the specified bounding box.")
    else:
        for p in response.states:
            if not p.on_ground:
                print(f"Found plane: icao24 - {p.icao24} callsign - {p.callsign}")
                callsign = p.callsign
                icao24 = p.icao24
                return icao24

token_manager = TokenManager.from_json_file("credentials.json")
with OpenSkyApi(token_manager=token_manager) as api:
    target_icao24 = track_one_plane(api)
    for i in range(SAMPLES):
        response = api.get_states(icao24=target_icao24)            
        if response and response.states:
            altitude = response.states[0].baro_altitude
            latitude = response.states[0].latitude
            longitude = response.states[0].longitude
            print(f"Altitude: {altitude}, Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("no updates this round")
        time.sleep(INTERVAL)


