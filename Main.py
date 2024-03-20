import Token.Token as Token
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.watching, name="dir zu")
bot = commands.Bot(command_prefix = "!", activity=activity, intents = intents, status=discord.Status.online)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! Keimschleuder made me")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def roll(ctx, count: int = 1, sides: int = 6):
    if count <= 0:
        await ctx.send(f"Cannot Roll less that one dice")
        return
    if sides <= 0:
        await ctx.send(f"Cannot have a dice with less than one Side")
        return
    if count > 15:
        await ctx.send(f"Too many Dice, reduce the number of Dice by {count - 15}")
        return
    
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)

    rolls_str = ", ".join(str(roll) for roll in rolls)
    await ctx.send(f"You rolled {count} dice with {sides} sides: {rolls_str}. **Total: {total}**")

@bot.command()
async def hug(ctx, to: discord.User = commands.Author):
    await ctx.send(f"Hey, {to.mention}, you were just hugged by {ctx.author.mention}")
    await ctx.send(f"https://tenor.com/view/boo-hug-monsters-inc-sully-warm-hug-gif-17849453")

@bot.command()
async def wave(ctx, to: discord.User = commands.Author):
    await ctx.send(f'Hello {to.mention} :wave:')

@bot.command()
async def helpme(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}! \nI'm a Discord Bot made by Keimschleuder. I have some commands:\n\n1. `!roll count_of_dice number_of_sides` this command lets you roll dice.\n2. `!hug user` Hugs the given User\n3. `!ping` Responds with `Pong`\n4. `!wave` waves to a server member metioned\n5. `!hello` Just a friendly greeting")

bot.run(Token.TOKEN)
