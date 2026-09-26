import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
import validators
import time
import random
import asyncio
import requests
import urllib.parse
import os

TOKEN = os.environ["DISCORD_TOKEN2"]

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
#bot.remove_command('help')

@bot.event
async def on_ready():
    print('Né pour Détruire.')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="辐射深渊Gouffre Irradié监控SURVEILLANCE"))
    await tree.sync()

@bot.event
async def on_message(message):
    if (message.channel.id == 1369960921383960616 or message.channel.id == 1136803727509041182): 
        if message.attachments:
            await message.add_reaction('<GOVERNMENTAPPROVED:1370304353700675624>')
        else:
            await asyncio.sleep(21600)
            await message.delete()
    
#@slash.slash(name="irradiate", description="IRRADIATE")
#async def embed(ctx):
#      embedchall = discord.Embed(title='MESSAGE DU GOUVERNEMENT武装航空民兵', description="Les messages textuels non approuvés par le système武装航空民兵 seront automatiquement éradiqués", colour=0xac0000)
#      embedchall.set_footer(text="Museum宣传博物馆exposition", icon_url="https://cdn.discordapp.com/attachments/1311277508737368130/1364546627733426206/64px-Gathering_Storm_28Wild_Rift29_rune.png?ex=681e7fd4&is=681d2e54&hm=6ddc18e5e6d303d7b13cd75167539c82f4c8d8047afb48ad2d3ad96034567fa4&")
#      embedchall.set_image(url="https://cdn.discordapp.com/attachments/549515851418697741/1370287737311068241/pokemon-firered-and-leafgreen-video-game-wallpaper-2304x768-41585_103.png?ex=681ef367&is=681da1e7&hm=2bb1f639548ce715613484d042271f2a188fdb4625bd823163f29df0b134a3d4&")
#      await ctx.channel.send(embed=embedchall)
      
@tree.command(name="ping", description="Teste le Ping du bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong ! {round(bot.latency * 1000)}ms')

@tree.command(name="doxx", description="Traque une adresse IP format x.x.x.x")
async def traque(interaction: discord.Interaction, ipaddr: str = '9.9.9.9'):
    r = requests.get(f"http://ip-api.com/json/{ipaddr}")
    geo = r.json()
    await interaction.response.send_message("```IP "+geo['query']+"\n"+"ZIP "+geo['zip']+"\n"+"ISP "+geo['isp']+"\n"+"City "+geo['city']+", Country "+geo['country']+", CountryCode "+geo['countryCode']+"\n"+"Region "+geo['region']+" "+geo['regionName']+"\n"+"AS"+geo['as']+"\n"+"Latitude "+str(geo['lat'])+" Longitude "+str(geo['lon'])+"\n"+"Org "+geo['org']+"\n"+"Status "+geo['status']+"```")

@tree.command(name="peche", description="partir à la pêche")
async def fish(interaction: discord.Interaction):
    await interaction.response.send_message("En attente du poissongue (clueless)")
    await asyncio.sleep(3)
    await interaction.edit_original_response(content="En attente du poissongue (clueless).")
    await asyncio.sleep(3)
    await interaction.edit_original_response(content="En attente du poissongue (clueless)..")
    await asyncio.sleep(3)
    await interaction.edit_original_response(content="En attente du poissongue (clueless)...")
    await asyncio.sleep(3)
    catchrate = random.randint(1,10)
    if catchrate == 10:
          await interaction.followup.send("Ca mord !")
    else:
          await interaction.followup.send("Rien de rien..")
        
bot.run(TOKEN)