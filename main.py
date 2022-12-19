import requests
from twilio.rest import Client


# API_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
api_key = "[YOUR API KEY]"
city = "Sao Paulo,br"

# Twilio
account_sid = "[YOUR ACCOUNT SID]"
auth_token = "[YOUR ACCOUNT TOKEN]"


parameters = {
    "q": city,
    "appid": api_key
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["weather"][0]["id"]
print(weather_id)

if weather_id == 701:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_="[TWILIO PHONE NUMBER]",
        to="[YOUR PHONE NUMBER]"
    )
    print(message.sid)
