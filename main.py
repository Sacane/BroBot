import discord
from hide import token

client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready")

@client.event
async def on_message(ctx):
    print(ctx)
    if ctx.content.lower() == "hello":
        await ctx.channel.send("hi")
    if ctx.content.startswith("!pfc"):
        await ctx.channel.send("start")


client.run(token)
