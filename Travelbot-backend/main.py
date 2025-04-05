from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Travel Bot API"}

@app.get("/location/{city}")
def get_city_info(city: str):
    api_key = os.getenv("GEODB_API_KEY")
    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities?namePrefix={city}"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

    try:
        data = response.json()
        print("API raw JSON response:", data)


        if "data" not in data or not data["data"]:
            return {"error": "City not found or invalid response from API"}

        city_data = data["data"][0]
        return {
            "city": city_data["city"],
            "country": city_data["country"],
            "region": city_data["region"],
            "latitude": city_data["latitude"],
            "longitude": city_data["longitude"],
            "population": city_data["population"]
        }

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}