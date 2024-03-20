import Token.Token as Token
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def wave(ctx, to: discord.User = commands.Author):
    await ctx.send(f'Hello {to.mention} :wave:')


client.run(Token.TOKEN)
