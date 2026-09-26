from pydoc import describe
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import datetime
import time
import random
import asyncio
import requests
#import aiocron
import os

TOKEN = os.environ["DISCORD_TOKEN1"]
intents = discord.Intents().all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
#bot.remove_command('help')

@bot.event
async def on_ready():
    print('Screw the odds.')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="LE 501 DU BONHOMME"))
    await tree.sync()

@bot.event
async def on_message(message):
    if message.author.bot : return
    val2 = random.randint(1,10000)
    val4 = random.randint(1,20000)
    val5 = random.randint(1,5000)
    if val2 == 1 :
     embedmain = discord.Embed(title='ALERTE', description="Vous avez été visité par un rat magique sauvage. C'est une manifestation rare d'un esprit malin instable et très puissant.", colour =0x39ff14)
     embedmain.set_footer(text='Malédiction à celui qui ne lui répondra pas : \"Jtm poti rat\"')
     embedmain.set_image(url="https://media.discordapp.net/attachments/247380295228194817/895287871206985739/unknown.png?width=938&height=604")
     await message.channel.send(embed=embedmain)

    # if val5 == 1 :
    #  valchall = random.randint(1,3)
    #  if valchall == 1:
    #   embedchall = discord.Embed(title='ALERTE ANIMATION', description="Hé Salut vous ! c'est Louis de l'équipe d'animation du discord ! je sors du néant distordu pour égayer votre journée avec un MAXI CHALLENGE XXL !! Come vedi parlo italiano! fai uno screenshot dell'immagine qui sotto, traduci ed ESEGUI", colour =0xff7f00)
    #   embedchall.set_footer(text='Et n\'oubliez pas que vous êtes des CHIENS MALAISANTS si vous trichez ou si vous ne voulez pas vous abaisser à faire ces trucs stupides ! allez on dévisse son cul de sa chaise et on bouge ! (les trucs longs à faire abrégez)')
    #   embedchall.set_image(url="https://cdn.discordapp.com/attachments/574252797655252998/903115468963975248/6sHnSLuyVQAAAABJRU5ErkJggg.png")
    #   await message.channel.send(embed=embedchall)
    #   await message.channel.send("https://tenor.com/view/challenge-random-gif-16597878")
    #  elif valchall == 2:
    #   embedchall = discord.Embed(title='ALERTE ANIMATION', description="Salut les L9 PISSCRINGERS ! C'est Louis de l'équipe d'animation du discord ! C'est parti pour un MAXI CHALLENGE XXL ! L9 SMURFING ON PISSRANDOMS XDDD ?? Alors, vous vous sentez chauds ? ca clique vite et bien ? Vous pensez avoir l'APM de Sardoche ? Parfait pour ce challenge !")
    #   embedchall.set_footer(text='ALLEZ ON SE BOUGE BORDEL HURRY UP YOU PISSCRINGER CASINO GRIEFER CANCERTARD SHITRANDOM')
    #   embedchall.set_image(url="https://cdn.discordapp.com/attachments/574252797655252998/903118914341453844/20jYVsJdNyoJYDBebVcqDfmwP9X55VUtGJzuThAAAAAElFTkSuQmCC.png")
    #   await message.channel.send(embed=embedchall)
    #   await message.channel.send("https://cdn.discordapp.com/attachments/549515851418697741/903111283832926248/016eb08aed7d908f5b8fe0bf9ac2a9db.gif")
    #  elif valchall == 3:
    #   embedchall = discord.Embed(title='ALERTE ANIMATION', description="Salut les Bouffons avec un grand B ! C'est Louis de l'équipe d'animation du discord ! C'est l'heure du MAXI CHALLENGE XXL ! C'est l'heure de troller un peu, on va normaliser le fait de déranger la paix avec des petites farces ! La Malice :)")
    #   embedchall.set_footer(text='Pas de triche :) si j\'étais toi je ne jouerais pas avec le feu surtout quand il y\'a de la MALICE dans l\'histoire :)')
    #   embedchall.set_image(url="https://cdn.discordapp.com/attachments/574252797655252998/903123513316106240/o9G4FlzVP0OprnIwAAAABJRU5ErkJggg.png")
    #   await message.channel.send(embed=embedchall)
    #   await message.channel.send("https://cdn.discordapp.com/attachments/549515851418697741/903120414065172550/7iv4pkrienb71.gif")

    if 'https://tenor.com/view/cat-cat-jumping-cat-excited-excited-dance-gif-19354605' in message.content:
      await message.channel.send("https://tenor.com/view/cat-cat-jumping-cat-excited-excited-dance-gif-19354605")
    if 'drip' in message.content or 'DRIP' in message.content or 'Drip' in message.content:
      messagedrip = await message.channel.send("https://media.discordapp.net/attachments/247380295228194817/896798734925561876/EvrhhmAXcAArBIs.png?width=609&height=603")
      await asyncio.sleep(1)
      await messagedrip.delete()
    if 'chaussure' in message.content or 'chaussures' in message.content or 'Chaussure' in message.content or 'Chaussures' in message.content:
     await message.channel.send("https://cdn.discordapp.com/attachments/247380295228194817/895327521950793748/st.couiugKC7DXP.mp4")
    if 'wtf' in message.content:
     await message.channel.send("wtf")

@tree.command(name="ping", description="Teste le Ping du bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong ! {round(bot.latency * 1000)}ms')

#@bot.command()
#async def say(ctx,arg):
#    await ctx.send(arg)

@tree.command(name="combiensinje", description="Remonte le nombre de sinjes récupérés au total")
async def combiensinje(interaction: discord.Interaction):
    user = interaction.user
    r = requests.get(f"http://"+os.environ["API_URL"]+"/recovery/sinje/combien/"+str(user.id))
    geo = r.json()
    nbsinje = geo[0]
    await interaction.response.send_message(str(nbsinje)+" sinjes")

@tree.command(name="l9generator", description="L9GENERATOR 联盟戦亡選機稿 NEW RATEARL SCRIPT 100% UNDETECTED 400 TUMORS 24 SEC 癌症 [ROLEX LASER BOOST]")
async def l9generator(interaction: discord.Interaction):
    #spacegliding in cthululow
    r = requests.get(f"http://"+os.environ["API_URL"]+"/recovery/l9/random/")
    l9json = r.json()
    sentence = l9json['prefix']+l9json['verb']+" in "+l9json['low']+"low"
    await interaction.response.send_message(sentence)

#@tree.command(name="start_the_trollage", description="=START THE TROLLAGE [EXTERMINATION PROTOCOL] 癌症 <AUTHORIZATION GRANTED>")
#async def start_the_trollage(interaction: discord.Interaction):
#    guild = ctx.guild
#    agentrole = guild.get_role(1030197512927203430)
#    await ctx.send("ENABLE TROLLAGE PROTOCOL 癌症 AGENCY TECHNOLOGY [UNDETECTED] ^ GAME LOOP (script) LABORATORY PROCESSING 789 NEW TECHNOLOGIES PER GAME [EXPERIMENTING IN HAMSTERLOW] / MENTAL ASYLUM L9 PTSD SPREADER ? TERRORIZING THE IRONLOWS ON CD ... INSTALLING ONE SHOT PROTOCOL ._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._. [GATHERING STORM INJECTION][10G/s]")
#    await asyncio.sleep(2)
#    message = await ctx.send("--------------------")
#    await message.edit(content="#-------------------")
#    await message.edit(content="##------------------")
#    await message.edit(content="###-----------------")
#    await message.edit(content="####----------------")
#    await message.edit(content="#####---------------")
#    await message.edit(content="######--------------")
#    await message.edit(content="#######-------------")
#    await message.edit(content="########------------")
#    await message.edit(content="#########-----------")
#    await message.edit(content="##########----------")
#    await message.edit(content="###########---------")
#    await message.edit(content="############--------")
#    await message.edit(content="#############-------")
#    await message.edit(content="##############------")
#    await message.edit(content="###############-----")
#    await message.edit(content="################----")
#    await message.edit(content="#################---")
#    await message.edit(content="##################--")
#    await message.edit(content="###################-")
#    await message.edit(content="####################")

#    await asyncio.sleep(2)
#    await ctx.channel.send(agentrole.mention+" WAKE UP")
#    await ctx.channel.send("[ERROR_SYSTEM_SHUTTING_DOWN]")

#@aiocron.crontab('0/1 * * * *')
#async def disrupcron():
#    guild = bot.get_guild(247380295228194817)
#    gamerchannel = guild.get_channel(696507936029278319)
#    gamerrole = guild.get_role(1163864301149360138)
#    request = requests.get(f"https://api.warframestat.us/pc/fissures/")
#    geo = request.json()
#    for mission in geo:
#       datestart = mission["activation"]
#       datestart = datestart[:-5]
#       datemission = datetime.datetime.strptime(datestart,"%Y-%m-%dT%H:%M:%S")
#       datestamp = datemission.timestamp()
#       print(datestamp)
#       ts = time.time()
#       print(ts)
#       if datestamp > (ts - 60):
#            type = mission["missionType"]
#            print(type)
#            if type == "Disruption":
#                await gamerchannel.send("DISRUPTION_MISSION"+mission["id"])
#                print(mission)
#                await gamerchannel.send(gamerrole.mention+" WAKE UP")
#                await channel.send("[ERROR_SYSTEM_SHUTTING_DOWN]")
#    await gamerchannel.send("CRON TASK COMPLETE")

#@slash.slash(name="disruption", description="XD")
#async def disruption(ctx):
#    guild = ctx.guild
#    gamerchannel = guild.get_channel(696507936029278319)
#    gamerrole = guild.get_role(1163864301149360138)
#    request = requests.get(f"https://api.warframestat.us/pc/fissures/")
#    geo = request.json()
#    for mission in geo:
#       type = mission["missionType"]
#       print(type)
#       if type == "Disruption":
#            await ctx.channel.send("DISRUPTION_MISSION"+mission["id"])
#            print(mission)
#            #await ctx.channel.send(gamerrole.mention+" WAKE UP")
#            #await ctx.channel.send("[ERROR_SYSTEM_SHUTTING_DOWN]")
#    await ctx.send("############_")

#@bot.command()
#@commands.cooldown(1,random.randint(21600,64800),commands.BucketType.guild)
#async def archimonstre(ctx):
#     newuser = ctx.message.author
#     guild = ctx.guild
#     role = guild.get_role(864605123110764645)
#
#     for user in guild.members:
#      if role in user.roles:
#       await user.remove_roles(role)
#       role = guild.get_role(864605123110764645)
#       await newuser.add_roles(role)
#
#       embedmeta = discord.Embed(title='Apykulteur de Récolteur', description="Un archimonstre est présent dans le discord !")
#       embedmeta.set_footer(text='Il réapparaîtra d\'ici 6 à 18 heures')
#       embedmeta.set_image(url="https://cdn.discordapp.com/attachments/807408208301129769/864600457681567824/x9g6AicmNBzWAAAAABJRU5ErkJggg.png")
#       await ctx.send(embed=embedmeta)
#       await ctx.send('GG à '+ctx.message.author.mention+' qui récupère la flamme (Précédemment détenue par '+user.mention+') <:chart_with_upwards_trend:864866720086097950><a:azf:863997449378725898>')
#       break

@tree.command(name="cinqcentun", description="REGULAAAAAAAAARRRREUH REGULLARRRRRR")
async def cinqcentun(interaction: discord.Interaction):
    await interaction.response.send_message('REGULAAAAAAAAAAAREUUUUH REGULAAAAAAARRRRRRR https://fxtwitter.com/Chap_GG/status/1436328594498850819?s=20')

bot.run(TOKEN)
