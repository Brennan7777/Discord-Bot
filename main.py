# This file runs the bot

import discord
import os
from dotenv import load_dotenv
from responses import get_response

load_dotenv()
TOKEN = os.getenv('TOKEN')
# print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test'):
        print("successful")
        await message.channel.send("Test")


client.run(TOKEN)
