import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
import os, random, datetime

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
			await ctx.send(f"{ctx.author.mention} 請勿標註 `everyone` !")
			await ctx.message.delete()
			return
		else: await ctx.message.delete()
		await ctx.send(content)


	@commands.group()
	async def join_group(self, ctx):
		await ctx.send("Group")

	@join_group.command()
	async def Gaming(self, ctx):
		await ctx.send("Gaming")

	@join_group.command()
	async def Music(self, ctx):
		await ctx.send("Music")

	@join_group.command()
	async def Coding(self, ctx):
		await ctx.send("Coding")

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, data):
		if data.message_id == (839110873011191814):
			if str(data.emoji) == '<:pogchamp:839098827427545118>':
				guild = self.bot.get_guild(data.guild_id)
				role = guild.get_role(839100920095965234)
				await data.member.add_roles(role)
				await data.member.send(f"你已取得 {role} 身分組!")

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, data):
		if data.message_id == (839110873011191814):
			if str(data.emoji) == '<:pogchamp:839098827427545118>':
				guild = self.bot.get_guild(data.guild_id)
				user = await guild.fetch_member(data.user_id)
				role = guild.get_role(839100920095965234)
				await user.remove_roles(role)
				await user.send(f"你已移除 {role} 身分組!")


	@commands.Cog.listener()
	async def on_message_delete(self, msg):
		await msg.channel.send("刪除的訊息內容:"+ str(msg.content))
		await msg.channel.send("原訊息發送者:"+ str(msg.author.mention))


	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="About GGR-bot", description="", color= 0x28ddb0)
		embed.add_field(name="開發者 Developers", value="GGReric#2110 (<@!538639229220028416>)", inline=False)
		embed.add_field(name="協助 Support Server", value="[Server Link](https://discord.gg/jgpqZpJ6QQ)" , inline=True)
		embed.add_field(name="版本 Version", value="0.1.0 a", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
		embed.add_field(name="邀請 Invite", value="[Invite Link]()" , inline=False)
		embed.set_author(name="GGReric")
		embed.set_footer(text="")
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/838022033270898709/838355239476133938/pogchamp.png")
		await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))