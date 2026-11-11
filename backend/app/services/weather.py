
import httpx

WEATHER_API = "https://api.open-meteo.com/v1/forecast"

async def get_forecast():
    params = {
        "latitude": 37.7749,
        "longitude": -122.4194,
        "daily": [
            "temperature_2m_max",
            "sunshine_duration",
            "precipitation_probability_max"
        ],
        "timezone": "America/Los_Angeles",
        "forecast_days": 7
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            WEATHER_API,
            params=params
        )
        response.raise_for_status()

    data = response.json()
    daily = data["daily"]

    forecast = []

    for i, date in enumerate(daily["time"]):
        forecast.append({
            "date": date,
            "temperature_high": daily["temperature_2m_max"][i],
            "sunshine_hours": round(
                daily["sunshine_duration"][i] / 3600, 1
            ),
            "precipitation_probability":
                daily["precipitation_probability_max"][i]
        })

    return forecast
