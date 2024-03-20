import Token.Token as Token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.watching, name="your fingers")
bot = commands.Bot(command_prefix = "!", activity=activity, intents = intents, status=discord.Status.online)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def wave(ctx, to: discord.User = commands.Author):
    await ctx.send(f'Hello {to.mention} :wave:')

bot.run(Token.TOKEN)
