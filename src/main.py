import random
import discord
from discord.ext import commands
from decouple import config

TOKEN = config('TOKEN', default='') 
PREFIX = config('PREFIX', default='/')
IDAUTHOR = config('IDAUTHOR', default='')

purple = 0x4b173d
msg_id = None
msg_user = None

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

@bot.command(name='cargos')
async def cargos_command(ctx):
    embed = discord.Embed(
        title="Exemplo de caixa que adiciona cargos",
        color=purple,
        # Adicione oque sera escrito na caixa
        description="- Cargo 1 = 🤓\n"
                    "- Cargo 2 = 😎\n"
                    "- Cargo 3 = 🤨\n",
    )

    # Coloque os emojis correspondentes ao cargo
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("🤓")
    await botmsg.add_reaction("😎")
    await botmsg.add_reaction("🤨")

    global msg_id
    msg_id = botmsg.id
    global msg_user
    msg_user = ctx.author

@bot.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    guild = user.guild

    if user.bot:  # Ignorar reações de bots
        return

    # Para cada cargo coloque o nome Exatamente igual ao do servidor e o emoji correspondente
    if reaction.emoji == "🤓" and msg.id == msg_id:
        role = discord.utils.get(guild.roles, name="Cargo 1")
        await user.add_roles(role)
        print(f"Adicionou o cargo {role.name} para {user.name}")

    if reaction.emoji =="😎" and msg.id == msg_id:
        role = discord.utils.get(guild.roles, name="Cargo 2")
        await user.add_roles(role)
        print(f"Adicionou o cargo {role.name} para {user.name}")

    if reaction.emoji =="🤨" and msg.id == msg_id:
        role = discord.utils.get(guild.roles, name="Cargo 3")
        await user.add_roles(role)
        print(f"Adicionou o cargo {role.name} para {user.name}")

    
if not TOKEN:
    raise ValueError("A variável de ambiente TOKEN não foi definida.")


bot.run(TOKEN)