import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

intents = discord.Intents.all()

with open('setting.json', 'r', encoding= 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= jdata['Prefix'], owner_ids= jdata['Owner_id'])
@bot.event
async def on_ready():
    print("Bot is online✅ you can use the bot now!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F"{member} left!")

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
	    bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])