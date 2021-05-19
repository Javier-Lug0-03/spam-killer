#made by Javier Lugo
import discord
from discord import message
from discord.ext import commands
import random
from discord.flags import Intents
#defines the global variables used
description = "a bot to kick the assholes that won't stop spamming/pinging on a discord server"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='?', description=description, intents=intents)
client = discord.Client()

@commands.has_permissions(kick_members=True)
#defines the kick function
@bot.command(pass_context = True, name="kick")
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)
#shows some info in the terminal
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('version 1.0.8 BETA')
#kicks the person that sent the message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('@everyone'):
        await kick(ctx="none",user=message.author,reason="spam")
#kicks the person that sent the message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Una vez:sob::sneezing_face:estaba llorando :sob::sob::sob::sob::sob::sob:xq mis papás :couple::couple:se divorciaron:scream::cold_sweat::sweat::tired_face::broken_heart::broken_heart:y entre a Youtube :scream::star_struck::kissing_heart::kissing_closed_eyes:y en recomendaciones :scream::scream::scream::scream::scream:me salio :scream::scream::scream:una canción :star_struck::star_struck::star_struck::notes::notes::notes::notes::musical_note::musical_note::musical_score::musical_score::musical_score:de:star_struck::heart_eyes::kissing_heart:BTS:heart_eyes::heart_eyes::heart_eyes::heart_eyes::heart_eyes::heart_eyes::heart_eyes::kissing_heart::kissing_heart::kissing_heart:y me gusto:scream:xq:kissing_closed_eyes::kissing_closed_eyes::kissing_closed_eyes:su música :heart_eyes::heart_eyes::heart_eyes::heart_eyes:me salvo:scream::relieved::astonished:del suicidio :tired_face::heart_eyes::100::sparkles::star::heart:ya q sus cansiones:musical_score::musical_note::notes::notes:hablan:heart_eyes::kissing_heart::kissing_heart::kissing_heart:del amor:kiss::couple::two_women_holding_hands::two_men_holding_hands::couplekiss::couple_with_heart:y la amistad :couple_with_heart::100::kiss::couplekiss::sparkles::two_women_holding_hands:y derrepente :scream:me volvi bisexual:heart_eyes::heart_eyes::heart_eyes::heart_eyes::rainbow_flag::rainbow_flag::rainbow_flag::rainbow_flag:y feminista:green_heart::purple_heart::purple_heart::green_heart::purple_heart::green_heart::green_heart::purple_heart::green_heart::purple_heart::purple_heart: sabía qué :heart_eyes::heart_eyes::heart_eyes::heart_eyes::kissing_heart:el kpop había salvado mi vida:heart_eyes::kissing_heart: simplemente el mejor genero de la historia :heart_eyes_cat::heart_eyes_cat::punch: Jungkook es mi esposo:heart_eyes::heart_eyes::scream:y misueño es biajar a :flag_kr::flag_kr::flag_kr::flag_kr::flag_kr::flag_kr::flag_kr: simplemente increible como unos coreanos:heart_eyes::heart_eyes::heart_eyes::heart_eyes::flag_kr::flag_kr::flag_kr:superaron a The Beatles :heart_eyes::heart_eyes::punch:le pateó :kissing_heart::kissing_heart:la cara:face_with_symbols_over_mouth::face_with_symbols_over_mouth::face_with_symbols_over_mouth::face_with_symbols_over_mouth:a todo aquel q dise q no le gusta bts xq a todxs nos tiene que gusta BTS:flag_kr::face_with_symbols_over_mouth:'):
        await kick(ctx='none',user=message.author,reason="spam")

client.run('ODQ0MjQ5NzM1ODM2OTkxNTk4.YKPq1g.lGjo8WF0MRfvuXgOJk48k8Oz8RA')