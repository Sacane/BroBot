import os
from discord.ext import commands
import discord
import pfc_game as p
import random
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("bot is ready...")
    await bot.change_presence(activity=discord.Game("attendre que vous jouez à Pierre-Feuille-Ciseau"))


@bot.command(name='del')
async def delete(ctx, numberOfMessagesToDelete: int):
    messages = await ctx.channel.history(limit=numberOfMessagesToDelete + 1).flatten()

    for each_message in messages:
        await each_message.delete()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to specify a second player")

@bot.command(name='pfc')
async def pfc_start(ctx, name_player1: discord.Member = None, name_player2: discord.Member = None, numberBestOf: int = 3):
    if numberBestOf > 5:
        await ctx.send("STOP, le nombre de partie est trop élevé voyons !")
    elif name_player1 == None or name_player2 == None:
        await ctx.send("Vous devez specifier au 2 joueurs")
    else:
        random.seed(None)
        i = 0
        player1 = p.Player(str(name_player1.display_name))
        player2 = p.Player(str(name_player2.display_name))

        await ctx.send(f"{player1} VS {player2}")
        while max(player1.score, player2.score) != numberBestOf:
            p.updateRound(player1, player2)
            if player1.equals(player2):
                await ctx.send(f"```{p.display_score(player1, player2)}```")
                continue

            await ctx.send(f"```Round {i+1} :\n" f"{player1.current_plays()}\n"
                           f"{player2.current_plays()}```")
            await ctx.send(f"```{p.display_score(player1, player2)}```")
            i += 1
        await ctx.send(f"```{p.display_winner(player1, player2)}```")

bot.run(os.getenv("TOKEN"))
