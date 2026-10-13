from opensky_api import OpenSkyApi, TokenManager

BBOX = (37.8, 38.0, -122.4, -122.1) #[min_latitude, max_latitude, min_longitude, max_longitude]

token_manager = TokenManager.from_json_file("credentials.json")
with OpenSkyApi(token_manager=token_manager) as api:
    response = api.get_states(bbox=BBOX)

    if response is None or not response.states:
        print("No planes found in the specified bounding box.")
    else:
        print(f"{len(response.states)} planes found.")

        print(f"{'Callsign':<13}{'Latitude':<13}{'Longitude':<13}{'Altitude':<13}")
        print("-" * 47)
        for p in response.states:
            print(f"{p.callsign:<13}{p.latitude:<13}{p.longitude:<13}{str(p.baro_altitude):<13}")