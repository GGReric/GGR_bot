import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, os

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Owner(Cog_Extension):
	@commands.command()
	@commands.is_owner()
	async def load(self, ctx, extension):
		self.bot.load_extension(f'cmds.{extension}')
		await ctx.send(f'Load {extension} done.')

	@commands.command()
	@commands.is_owner()
	async def unload(self, ctx, extension):
		self.bot.unload_extension(f'cmds.{extension}')
		await ctx.send(f'Unload {extension} done.')

	@commands.command()
	@commands.is_owner()
	async def reload(self, ctx, extension):
		if extension == '*':
			for filename in os.listdir('./cmds'):
				if filename.endswith('.py'):
					self.bot.reload_extension(f'cmds.{filename[:-3]}')
			await ctx.send(f'Reload All done.')
		else:
			self.bot.reload_extension(f'cmds.{extension}')
			await ctx.send(f'Reload {extension} done.')

	@commands.command()
	@commands.is_owner()
	async def shutdown(self, ctx):
		await ctx.send("Shutting down...")
		await asyncio.sleep(1)
		await self.bot.logout()

def setup(bot):
   bot.add_cog(Owner(bot))