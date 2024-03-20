import Token.Token as Token
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
    try: # Try to sync slash commands
        synced = await bot.tree.sync(guild=discord.Object(id=Token.ID))
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
    
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

@bot.tree.command(name = "ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

client.run(Token.TOKEN)
