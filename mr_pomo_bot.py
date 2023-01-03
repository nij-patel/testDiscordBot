# This example requires the 'message_content' intent.

from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')

#@client.event
@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))


#@client.event
@bot.command(name="start", help="Starts a Pomodoro timer")
async def start_timer(ctx):
    await ctx.send("Time to work!")


#    if message.author == client.user:
#        return

#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')

#client.run(os.environ['BOT_TOKEN'])
bot.run(os.environ['BOT_TOKEN'])
