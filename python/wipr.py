import discord
from discord.ext import commands
from discord import app_commands
from typing import NoReturn
from discord.utils import get
from twikit import Client, Tweet
import validators
import os
import time
import random
import asyncio
import requests
import urllib.parse

TOKEN = os.environ["DISCORD_TOKEN3"]

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
#bot.remove_command('help')

async def main():
    
    latest_id = 50
    client = Client('en-US')
    check_interval = 83580
    USER_ID = '517004655'
    tweet_channel = bot.get_channel(1391016775407374357)
    tweet_channel2 = bot.get_channel(1485792521740091494)
    cookies_path = "cookies.json"
    
    if os.path.exists(cookies_path):
        client.load_cookies(cookies_path)
    else:
        await client.login(
        auth_info_1=os.environ["AUTH_INFO1"],
        auth_info_2=os.environ["AUTH_INFO2"],
        password=os.environ["AUTH_INFO3"])
        client.save_cookies(cookies_path)

    while True:
        tweets = await client.get_user_tweets(USER_ID, 'Tweets')
        latest_id = tweets[0].id
        dailyrotationmessage = await tweet_channel.send(f'https://fxtwitter.com/SkinSpotlights/status/{latest_id}')
        dailyrotationmessage2 = await tweet_channel2.send(f'https://fxtwitter.com/SkinSpotlights/status/{latest_id}')
        await asyncio.sleep(check_interval)
        check_interval = 24 * 60 * 60
        await dailyrotationmessage.delete()
        await dailyrotationmessage2.delete()

@bot.event
async def on_ready():
    print('Break the chain')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="the chain"))
    await tree.sync()
    await main()

@tree.command(name="ping", description="Teste le Ping du bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong ! {round(bot.latency * 1000)}ms')

bot.run(TOKEN)