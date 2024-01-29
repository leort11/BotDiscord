import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como: {bot.user.name}')
    print(f"ID: {bot.user.id}")

@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("Olá Mundo, estou aqui!")


bot.run('MTIwMDA1NjQxMzcwNDE3OTc2Mg.GNl2Vk.oGeiRiTvZ6pi8R89oKGUx751XIRADkfdOKbfMo')
