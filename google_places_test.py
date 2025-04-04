from dotenv import load_dotenv
import os
import requests

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get the API key securely
API_KEY = os.getenv("API_KEY")

# ✅ Check if API key is loaded correctly
if not API_KEY:
    print("❌ Error: API Key not found! Make sure you have a .env file.")
    exit()

# ✅ Continue with the existing place search logic...
place = input("🌍 Enter a place you'd like to search for: ")
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={place}&key={API_KEY}"

response = requests.get(url)
data = response.json()

if data.get("status") == "OK":
    result = data["results"][0]
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

    print("\n📦 Result Found:")
    print(place_info)

else:
    print("❌ No results found or API error:", data.get("status"))
