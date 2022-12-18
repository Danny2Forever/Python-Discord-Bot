import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from random import *
from datetime import datetime
import asyncio
import ffmpeg
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!',intents=intents) 

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == client.user:
        return
  
    if user_message.lower() == "hello" or user_message.lower() == "hi":
        await message.channel.send(f'Hello {username}')
        return

    if user_message.lower() == "bye":
        await message.channel.send(f'Bye {username}')
        return

    if user_message.lower() == "กี่โมงครับ":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send(f'{current_time} โมงครับ')
        return

    if user_message.lower() == "dice":
        num = random.randint(0,7)
        await message.channel.send(num)
        return

    if user_message.lower() == "โย่ว":
        await message.add_reaction('\N{PARTY POPPER}')
        return
    
    if user_message.lower() == "ว่าไง":
        await message.add_reaction('สวัสดีคุณนิวัตรครับ')
        return

@client.event
async def on_ready():
    print("Bot is ready!")

client.run(TOKEN)
