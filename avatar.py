import discord
import requests
import os

def download_image(image_url, save_path):

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"Image downloaded successfully to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

class Client(discord.Client):
    async def on_ready(self):
        print("ready")
    async def on_message(self, message):
        if message.content == ("!join"):
            id = message.author
            avatar = id.avatar
            user = id.name
            download_image(avatar.url, os.path.join("DiscordImages", f"{user}.png"))

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents = intents)
client.run('Your Token')