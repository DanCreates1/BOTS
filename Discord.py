from discord.ext import commands
import discord
import random
from datetime import datetime, timedelta
import pytz

BOT_TOKEN = ""
CHANNEL_ID = 

bot = commands.Bot(command_prefix="^", intents=discord.Intents.all())

# In-memory storage for user balances and work cooldowns
user_balances = {}
work_cooldowns = {}

# Predefined time zones
usa_timezones = {
    'Eastern': 'US/Eastern',
    'Central': 'US/Central',
    'Mountain': 'US/Mountain',
    'Pacific': 'US/Pacific',
    'Alaska': 'US/Alaska',
    'Hawaii': 'US/Hawaii'
}

middle_east_timezones = {
    'Iran': 'Asia/Tehran',
    'Saudi Arabia': 'Asia/Riyadh',
    'UAE': 'Asia/Dubai',
    'Israel': 'Asia/Jerusalem',
    'Turkey': 'Europe/Istanbul'
}


@bot.event
async def on_ready():
    print("Hello! Pouyan is the goat of programming and he made me")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hello sir Pouyan!")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")



@bot.command()
async def work(ctx):
    user = ctx.author
    now = datetime.now()
    if user.id in work_cooldowns:
        last_work_time = work_cooldowns[user.id]
        if now < last_work_time + timedelta(minutes=5):
            remaining_time = (last_work_time + timedelta(minutes=5)) - now
            minutes, seconds = divmod(remaining_time.seconds, 60)
            await ctx.send(f"{user.mention}, you can work again in {minutes} minutes and {seconds} seconds.")
            return

    earnings = random.randint(10, 100)  # Random earnings between 10 and 100
    user_balances[user.id] = user_balances.get(user.id, 0) + earnings
    work_cooldowns[user.id] = now

    await ctx.send(
        f"{user.mention}, you worked and earned {earnings} coins! Your new balance is {user_balances[user.id]} coins.")


@bot.command()
async def bal(ctx):
    user = ctx.author
    balance = user_balances.get(user.id, 0)
    await ctx.send(f"{user.mention}, your balance is {balance} coins.")


@bot.command()
async def time_usa(ctx):
    response = []
    now_utc = datetime.now(pytz.utc)
    for name, tz in usa_timezones.items():
        tz_time = now_utc.astimezone(pytz.timezone(tz))
        response.append(f"{name} Time: {tz_time.strftime('%Y-%m-%d %H:%M:%S')}")

    await ctx.send('\n'.join(response))


@bot.command()
async def time_me(ctx):
    response = []
    now_utc = datetime.now(pytz.utc)
    for name, tz in middle_east_timezones.items():
        tz_time = now_utc.astimezone(pytz.timezone(tz))
        response.append(f"{name} Time: {tz_time.strftime('%Y-%m-%d %H:%M:%S')}")

    await ctx.send('\n'.join(response))


@bot.command()
async def time(ctx, region: str):
    # Combine all known time zones
    all_timezones = {**usa_timezones, **middle_east_timezones}

    # Check if the region is a known predefined region
    if region in all_timezones:
        timezone = pytz.timezone(all_timezones[region])
    else:
        try:
            # Check if the region is a valid timezone string
            timezone = pytz.timezone(region)
        except pytz.UnknownTimeZoneError:
            await ctx.send(f"Unknown timezone: {region}. Please provide a valid timezone.")
            return

    # Get the current time in the given timezone
    now = datetime.now(timezone)
    await ctx.send(f"The current time in {region} is {now.strftime('%Y-%m-%d %H:%M:%S')}.")





bot.run(BOT_TOKEN)
