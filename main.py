import discord
from discord.ext import commands
import os
from discord.flags import Intents
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('bot is ready.')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'hello {member.name}')
    print(f'{member} has join to the server')

@client.event
async def on_member_remove(member):
   print(f'{member} has left from the server')
   
# @client.event
# async def on_message(message):
#     print(message.clean_content)



client.run(TOKEN)