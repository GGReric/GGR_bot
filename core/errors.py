import discord
from discord.ext import commands
from core.classes import Cog_Extension, Logger
from cmds.main import Main #導入 Main Cog
import json, asyncio

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Errors():

	# 自訂 Error Handler
	@Main.sayd.error
	async def sayd_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			err = str(error).split(" ")[0]
			await ctx.send(f"遺失必要參數： <`{err}`>")
			await ctx.send_help(ctx.command)
			Logger.log(self, ctx, error)
			
	
	# 預設 Error Handler
	async def default_error(self, ctx, error):
		
		# 比對觸發的error是否為 MissingRequiredArgument 的實例
		if isinstance(error, commands.MissingRequiredArgument):
			err = str(error).split(" ")[0]
			await ctx.send(f"遺失必要參數： <`{err}`>")
			await ctx.send_help(ctx.command)
			Logger.log(self, ctx, error)
		
		# error 內容是否為 403 Forbiddden
		elif "403 Forbidden" in str(error): 
			await ctx.send("403 Forbidden，請檢查 Bot 權限")
			Logger.log(self, ctx, error)
		
		# 皆不符合
		else:
			await ctx.send(f'未知錯誤: {error}')
			Logger.log(self, ctx, error)

	

