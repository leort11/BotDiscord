import discord
from discord import Intents

intents = Intents.default()
intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready() :
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('----------PR----------')

@client.event
async def on_message(message) :
    if message.author == client.user :
        return
    
    if message.content.lower() == '?test' :
        await message.channel.send("Olá Mundo, estou aqui")

client.run('MTIwMDA1NjQxMzcwNDE3OTc2Mg.GNl2Vk.oGeiRiTvZ6pi8R89oKGUx751XIRADkfdOKbfMo')
