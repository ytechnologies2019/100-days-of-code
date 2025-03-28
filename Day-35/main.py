import os
import requests
from twilio.rest import Client
import weather_message
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch API credentials from environment variables
api_key = os.getenv('API_KEY')
api_endpoint = os.getenv('API_ENDPOINT')

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

weather_parameter = {
    'lat': '16.866070',
    'lon': '96.195129',
    'appid': api_key,
}

# Fetch weather data
response = requests.get(api_endpoint, params=weather_parameter)
weather_data = response.json()

# Extract weather details
sky_condition = weather_data['weather'][0]['description']
kelvin_value = float(weather_data['main']['temp'])
celsius = kelvin_value - 273.15

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Determine the weather message
if celsius > 38:
    so_hot_message = weather_message.so_hot_random_line
    today_message = f'Sky has {sky_condition}☀️️\nWeather is so hot 🔥\n{so_hot_message}'

elif 32 <= celsius <= 37:
    hot_message = weather_message.so_hot_random_line
    today_message = f'Sky has {sky_condition}🌤️\nToday weather is Hot 🥵\n{hot_message}'

elif 23 <= celsius <= 31:
    warm_message = weather_message.warm_random_line
    today_message = f'Sky has {sky_condition}⛅️\nToday weather is warm 😮‍💨\n{warm_message}'

else:
    fine_message = weather_message.find_random_line
    today_message = f'Sky was {sky_condition} \nHey! Today weather is fine 😄\n{fine_message}'

# Send SMS (Uncomment when ready to send)
message = client.messages.create(
    body=today_message,
    from_="+18787865355",  # Your Twilio phone number
    to=["+959966113099", "+959978060703"]
)


print(message.body)
