import math

def locate_camera(plane_lat, plane_lon, altitude, elevation_angle, azimuth):
    azimuth = azimuth + 180

    d = altitude / math.tan(math.radians(elevation_angle))
    change_in_latitude = d * math.cos(math.radians(azimuth)) / 111132
    change_in_longitude = d * math.sin(math.radians(azimuth)) / (111132 * math.cos(math.radians(plane_lat)))
    camera_lat = plane_lat + change_in_latitude
    camera_lon = plane_lon + change_in_longitude
    
    return camera_lat, camera_lon
