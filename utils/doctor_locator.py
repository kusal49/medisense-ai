# utils/doctor_locator.py
import os
import requests

GOOGLE_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def find_nearby_doctors(
    specialty: str,
    location: str,
    radius: int = 5000  # meters
):
    """
    location = city name or 'lat,lng'
    specialty = 'urologist', 'cardiologist', etc.
    """

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    params = {
        "query": f"{specialty} doctor near {location}",
        "radius": radius,
        "key": GOOGLE_API_KEY
    }

    response = requests.get(url, params=params).json()

    doctors = []
    for place in response.get("results", [])[:5]:
        doctors.append({
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "rating": place.get("rating", "N/A"),
            "maps_url": f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}"
        })

    return doctors
