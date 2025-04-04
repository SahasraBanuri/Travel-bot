import requests

# Your API key
API_KEY = "AIzaSyBy1BjsBrVFkRBkZLSIlTQ2S1Ey13IyTK8"
place = "Eiffel Tower Paris"

# API URL
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={place}&key={API_KEY}"

# Get response
response = requests.get(url)
data = response.json()

# Step 1: Check if response is OK
if data.get("status") == "OK":
    # Step 2: Get the first result
    result = data["results"][0]

    # Step 3: Extract required fields
    name = result.get("name", "N/A")
    address = result.get("formatted_address", "N/A")
    rating = result.get("rating", "N/A")
    lat = result.get("geometry", {}).get("location", {}).get("lat", "N/A")
    lng = result.get("geometry", {}).get("location", {}).get("lng", "N/A")

    place_info = {
        "name": name,
        "address": address,
        "rating": rating,
        "latitude": lat,
        "longitude": lng
}

    # Step 4: Print nicely formatted output
    print("📦 Structured Output:\n", place_info)
else:
    print("❌ API Error:", data.get("status"))
