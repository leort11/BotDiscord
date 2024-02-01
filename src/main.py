import discord
from discord.ext import commands
from decouple import config

TOKEN = config('TOKEN', default='') 
PREFIX = config('PREFIX', default='/')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como: {bot.user.name}')
    print(f"ID: {bot.user.id}")

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("Olá Mundo, estou aqui!")
    
if not TOKEN:
    raise ValueError("A variável de ambiente TOKEN não foi definida.")

bot.run(TOKEN)
