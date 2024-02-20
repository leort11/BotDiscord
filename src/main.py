import random
import discord
from discord.ext import commands
from decouple import config

TOKEN = config('TOKEN', default='') 
PREFIX = config('PREFIX', default='/')
IDAUTHOR = config('IDAUTHOR', default='')

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

@bot.command(name='salve')
async def slv_command(ctx):
    await ctx.send("Salveeee!!!")

@bot.command(name='moeda')
async def moeda_command(ctx):
    choice = random.randint(1, 2)

    if choice == 1:
        await ctx.message.add_reaction('😀')
        
    elif choice == 2:
        await ctx.message.add_reaction('👑')

        
    
if not TOKEN:
    raise ValueError("A variável de ambiente TOKEN não foi definida.")


bot.run(TOKEN)