import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
import os, random, datetime, requests

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Main(Cog_Extension):
	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'{round(self.bot.latency*1000)} ms')


	@commands.command()
	@check.valid_user() #檢查權限, 是否存在於效人員清單中, 否則無法使用指令
	async def test(self, ctx):
		await ctx.send('Bee! Bo!')
		

	@commands.command()
	async def sayd(self, ctx, *, content: str):
		if "@everyone" in content:
			await ctx.send(f"{ctx.author.mention} Do not ping `everyone` !")
			await ctx.message.delete()
			return
		else: await ctx.message.delete()
		await ctx.send(content)
	

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, data):
		if data.message_id == (839110873011191814):
			if str(data.emoji) == '<:pogchamp:839098827427545118>':
				guild = self.bot.get_guild(data.guild_id)
				role = guild.get_role(839100920095965234)
				await data.member.add_roles(role)
				await data.member.send(f"You get {role} role!")

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, data):
		if data.message_id == (839110873011191814):
			if str(data.emoji) == '<:pogchamp:839098827427545118>':
				guild = self.bot.get_guild(data.guild_id)
				user = await guild.fetch_member(data.user_id)
				role = guild.get_role(839100920095965234)
				await user.remove_roles(role)
				await user.send(f"You remove {role} role!")


	@commands.Cog.listener()
	async def on_message_delete(self, msg):
		embed = discord.Embed(title="There is a member deleted the message!", description="", color= 0x28ddb0)
		embed.add_field(name="Message sender ", value= str(msg.author.mention), inline=False)
		embed.add_field(name="Deleted message", value= str(msg.content) , inline=True)
		await msg.channel.send(embed=embed)

	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="About GGR-bot", description="This bot is testing!", color= 0x28ddb0)
		embed.add_field(name="Developers", value="<@!538639229220028416>", inline=True)
		embed.add_field(name="Support Server", value="[Server Link](https://discord.gg/jgpqZpJ6QQ)" , inline=True)
		embed.add_field(name="Version", value="BETA 0.1.0", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=True)
		embed.add_field(name="Invite", value="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=837656833413873725&permissions=8&scope=bot)" , inline=False)
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/838370690109407242/839480933027282984/GGR.png")
		await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))