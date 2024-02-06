import random
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


@bot.command(name='moeda')
async def moeda_command(ctx):
    # Substitua 'ID_DO_AUTOR_PERMITIDO' pelo ID real do autor permitido
    autor_permitido_id = 'IDAUTOR'

    if ctx.message.author.id == autor_permitido_id:
        choice = random.randint(1, 2)

        if choice == 1:
            await ctx.message.add_reaction('😀')
        elif choice == 2:
            await ctx.message.add_reaction('👑')
    else:
        await ctx.send("Você não tem permissão para usar este comando!")

        
    
if not TOKEN:
    raise ValueError("A variável de ambiente TOKEN não foi definida.")

bot.run(TOKEN)