import discord
from discord import message
from discord.ext import commands
import random
from discord.flags import Intents

description = "a bot to kick the assholes that won't stop spamming/pinging on a discord server"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='?', description=description, intents=intents)
client = discord.Client()

@commands.has_permissions(kick_members=True)

@bot.command(pass_context = True, name="kick")
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('version 1.0.7 BETA')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('@everyone'):
        await kick(ctx="none",user=message.author,reason="spam")

client.run('ODQ0MjQ5NzM1ODM2OTkxNTk4.YKPq1g.6WkNPpgA6o7WYbiMqEnlnyrdYfo')