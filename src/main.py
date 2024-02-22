import random
import discord
from discord.ext import commands
from decouple import config

TOKEN = config('TOKEN', default='') 
PREFIX = config('PREFIX', default='/')
IDAUTHOR = config('IDAUTHOR', default='')

red = 0xC70039
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
        title="Escolha seu cargo FODA!!",
        color=red,
        description="- Goza Fino  = 🤓\n"
                    "- Goza Grosso  = 😎\n"
                    "- Cintura Ignorante  = 🥵\n"
                    "- Cheira Peido  = 💩\n"
                    "- LÍNGUA PRETA  = 👅\n"
                    "- Adora Leite  = 🍼\n"
                    "- Tem Amizade com o Patrão?  = 👥\n"
                    "- Beija bem?  = 💋\n"
                    "- Faz Gostoso?  = 🤨\n"
                    "- BRUHH  = ☣️\n",
    )
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("🤓")
    await botmsg.add_reaction("😎")
    await botmsg.add_reaction("🥵")
    await botmsg.add_reaction("💩")
    await botmsg.add_reaction("👅")
    await botmsg.add_reaction("🍼")
    await botmsg.add_reaction("👥")
    await botmsg.add_reaction("💋")
    await botmsg.add_reaction("🤨")
    await botmsg.add_reaction("☣️")

    global msg_id
    msg_id = botmsg.id
    global msg_user
    msg_user = ctx.author

@bot.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    guild = user.guild

    if reaction.emoji == "🤓" and msg.id == msg_id:
        role = discord.utils.get(guild.roles, name="Goza Fino")
        member = guild.get_member(user.id)
        await member.add_roles(role)
        print("adicionou")

    if reaction.emoji =="😎" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Goza Grosso", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🥵" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cintura Ignorante", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="💩" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cheira Peido", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="👅" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "LÍNGUA PRETA", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🍼" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Adora Leite", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="👥" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Tem Amizade com o Patrão?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="💋" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Beija bem?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🤨" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Faz Gostoso?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="☣️" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "BRUHH", msg.guild.roles)
        await bot.add_roles(user, role)

@bot.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    guild = user.guild

    if reaction.emoji == "🤓" and msg.id == msg_id:
        role = discord.utils.get(guild.roles, name="Goza Fino")
        member = guild.get_member(user.id)
        await member.remove_roles(role)
        print("removeu")

    if reaction.emoji =="😎" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Goza Grosso", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🥵" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cintura Ignorante", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="💩" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Cheira Peido", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="👅" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "LÍNGUA PRETA", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🍼" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Adora Leite", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="👥" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Tem Amizade com o Patrão?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="💋" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Beija bem?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="🤨" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Faz Gostoso?", msg.guild.roles)
        await bot.add_roles(user, role)

    if reaction.emoji =="☣️" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "BRUHH", msg.guild.roles)
        await bot.add_roles(user, role)

    
if not TOKEN:
    raise ValueError("A variável de ambiente TOKEN não foi definida.")


bot.run(TOKEN)