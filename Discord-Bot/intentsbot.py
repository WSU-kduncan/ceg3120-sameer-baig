# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')

        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hitchhiker_quotes = [
        'The Cleveland Cavaliers currently have 4 All-Stars on their roster.',
        'It has been reported by Brian Windhorst that Donovan Mitchell is excited with the prospect of playing with Darius Garland.',
        'There is still room for improvement if the Cavs do not sign or trade for a 3&D wing.',
        'The Cleveland Cavaliers still have one more roster spot left, as it is knwon that they are trying out a few players.',
        'Ricky Rubio had so much faith in the Cavaliers, that he resigned on a smaller contract after being traded.',
    ]
    if message.content == 'Cavs':
    #if message.content.startswith('$towel'):
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

client.run(TOKEN)
