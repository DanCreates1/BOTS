from discord.ext import commands
import discord




BOT_TOKEN = "put your bot token here"
#put you channel id down there. !! Do not put in the strings
CHANNEL_ID = 

bot = commands.Bot(command_prefix="^", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Dan is the goat of programming and he made me")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hello sir Dan!")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(BOT_TOKEN)
