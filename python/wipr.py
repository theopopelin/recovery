import discord
from discord import app_commands
from twikit import Client, Tweet
import validators
import os
import asyncio
import requests
import json
import urllib.parse
from datetime import datetime, timedelta
import aiocron

TOKEN = os.environ["DISCORD_TOKEN3"]

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
#bot.remove_command('help')

async def main():

    client = Client('en-US')

    USER_ID = '517004655'
    COOKIES_PATH = "/var/www/cookies.json"
    CHANNELS_PATH = "/var/www/channels.json"
    MESSAGES_ID_PATH = "/var/www/messagesid.json"

    with open(CHANNELS_PATH, "r", encoding="utf-8") as f:
        jsonids = json.load(f)
    tweet_channel_ids = jsonids["tweet_channels"]

    if os.path.exists(COOKIES_PATH):
        client.load_cookies(COOKIES_PATH)
    else:
        await client.login(
            auth_info_1=os.environ["AUTH_INFO_1"],
            auth_info_2=os.environ["AUTH_INFO_2"],
            password=os.environ["AUTH_INFO_3"]
        )
        client.save_cookies(COOKIES_PATH)

    @aiocron.crontab('0 0 * * *')
    async def delete_tweet():

        with open(MESSAGES_ID_PATH, "r", encoding="utf-8") as f:
            messageids = json.load(f)

        for item in messageids["messages"]:
            channel = bot.get_channel(int(item["channel_id"]))

            if channel is None:
                channel = await bot.fetch_channel(int(item["channel_id"]))

            message = await channel.fetch_message(int(item["message_id"]))
            await message.delete()

        with open(MESSAGES_ID_PATH, "w", encoding="utf-8") as f:
            json.dump({"messages": []}, f, indent=4)

    @aiocron.crontab('1 0 * * *')
    async def post_tweet():

        tweets = await client.get_user_tweets(USER_ID, 'Tweets')
        latest_id = tweets[0].id
        tweet_url = f'https://fxtwitter.com/SkinSpotlights/status/{latest_id}'

        messages = []

        for channel_id in tweet_channel_ids:
            channel = bot.get_channel(int(channel_id))

            if channel is None:
                channel = await bot.fetch_channel(int(channel_id))

            message = await channel.send(tweet_url)

            messages.append({
                "channel_id": int(channel_id),
                "message_id": message.id
            })

        with open(MESSAGES_ID_PATH, "w", encoding="utf-8") as f:
            json.dump({"messages": messages}, f, indent=4)
            
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