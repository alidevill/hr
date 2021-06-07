import discord
from discord.colour import Colour
from discord.enums import Status
from discord.ext import commands
import os
from discord.flags import Intents
from dotenv import load_dotenv
import re

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    
    # listening
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='phlolearn\'s playlist on spotify'))
    # watching
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='phlolearn\'s vedios'))
    # playing
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='assassin\'s creed'))
    # streaming
    await client.change_presence(status=discord.Status.idle, activity=discord.Streaming(name='assassin\'s creed', url='https://www.twitch.tv/hr_arsha'))
    print('bot is ready.')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'hello {member.name}')
    print(f'{member} has join to the server')

@client.event
async def on_member_remove(member):
   print(f'{member} has left from the server')

@client.command()
async def help(ctx):
    role = ctx.author.roles
    name = ctx.author.name
    avataar = ctx.author.avatar
    await ctx.send(f'''your name is {name}\nand yor avatar is {avataar}
    commands from this bot is
    !help
    !dastresi
    !play
    !embed
    ''')
    print(role)


@client.command()
async def dastresi(ctx):
    role = ctx.author.roles
    role_name = re.findall("name=\'(\w+)", str(role))
   
    if role_name == []:
        await ctx.send(str(role)) 
    elif role_name[0] == 'khodam':
        await ctx.send('شما دسترسی لازم را ندارید')   

@client.command()
async def play(ctx, song_name):
    print(song_name)

@client.command()
async def embed(ctx):
    philolearn_embed = discord.Embed(
        title='PhiloLearn',
        description='این بات یک آزمایش و یک تجربه ی کوچک برای من است.',
        colour=0x5c1e26,
        # colour=Colour.dark_blue,
    )
    philolearn_embed.set_image(url='https://hr-arsha.github.io/static-site/assets/img/portfolio/fullsize/3.jpg')
    philolearn_embed.set_footer(text='حتما ویدیو را لایک کرده و مارا سابسکرایب کنید', icon_url='https://hr-arsha.github.io/static-site/assets/img/logo.png')
    philolearn_embed.set_author(name=ctx.author.name)
    philolearn_embed.set_thumbnail(url='https://hr-arsha.github.io/static-site/assets/img/portfolio/fullsize/1.jpg')

    await ctx.send('سلام این بات آزمایشی فیلولرن است.', embed=philolearn_embed)


client.run(TOKEN)