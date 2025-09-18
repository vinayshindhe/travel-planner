import googlemaps
import os

# Replace with your Google Maps API key
GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")

def get_directions_and_distance(origin: str, destination: str, travel_mode: str = "driving") -> dict:
    """
    Finds directions and distance between two locations using Google Maps.

    Args:
        origin: The starting point (address or place ID).
        destination: The ending point (address or place ID).
        travel_mode: The mode of transport (e.g., "driving", "walking", "bicycling", "transit").

    Returns:
        A dictionary containing route information (distance, duration, summary),
        or an error message if the request fails.
    """
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

    try:
        directions_result = gmaps.directions(
            origin,
            destination,
            mode=travel_mode,
            units="imperial" # or "metric"
        )

        if not directions_result:
            return {"status": "error", "message": "Could not find directions."}

        # Extract relevant information from the first route
        route = directions_result[0]
        distance_text = route['legs'][0]['distance']['text']
        duration_text = route['legs'][0]['duration']['text']
        summary = route['summary']

        return {
            "status": "success",
            "origin": origin,
            "destination": destination,
            "travel_mode": travel_mode,
            "distance": distance_text,
            "duration": duration_text,
            "summary": summary
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
