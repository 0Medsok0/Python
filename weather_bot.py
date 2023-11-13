import requests
from telegram.ext import Updater, CommandHandler
import os

def get_weather():
    api_key = "YOUR_API_KEY"
    location = "YOUR_LOCATION"
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={location}"
        f"&appid={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    return (
        f"Weather forecast for {location}:\n"
        f"Description: {weather_description}\n"
        f"Temperature: {temperature}°C\n"
        f"Humidity: {humidity}%"
    )

def weather(update, context):
    message = get_weather()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("weather", weather))
    updater.start_polling()

if __name__ == '__main__':
    main()
