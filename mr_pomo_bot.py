# This example requires the 'message_content' intent.

from dotenv import load_dotenv
import os
import discord
import asyncio
from timer import Timer
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', help_command=None)
COLOR_SUCCESS = 0x33c633
COLOR_DANGER = 0xc63333
timer = Timer()


@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot.user))


@bot.command(name="start", help="Starts a Pomodoro timer")
async def start_timer(ctx):

    await show_message(ctx, "Time to start working!", COLOR_SUCCESS)

    timer.start()
    while timer.is_running():
        await asyncio.sleep(1)  # 25 * 60
        timer.tick()

    await show_message(ctx, "Time to start your break!", COLOR_SUCCESS)


async def show_message(ctx, title, color):
    embed_msg = discord.Embed(
        title=title, color=color)
    await ctx.send(embed=embed_msg)


@bot.command(name="stop", help="Stop a Pomodoro timer")
async def stop_timer(ctx):
    await show_message(ctx, "Timer has stopped!", COLOR_DANGER)
    timer.stop()


@bot.command(name="time", help="Show current time")
async def show_time(ctx):
    await ctx.send(f"Current timer status is :  {timer.is_running()}")
    await ctx.send(f"Current time is :  {timer.get_ticks()}")


@bot.command(name="help", help="Show help text")
async def show_help(ctx):
    help_commands = dict()
    for command in bot.commands:
        help_commands[command.name] = command.help
    description = "Bot commands are: {}".format(help_commands)
    show_help_em = discord.Embed(
        title="This is Mr Pomo Dorio, a friendly pomodorio bot.", description=description, color=0xc63333)
    await ctx.send(embed=show_help_em)
    timer.stop()


bot.run(os.environ['BOT_TOKEN'])
