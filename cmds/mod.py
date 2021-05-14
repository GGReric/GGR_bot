import discord
from discord.ext import commands
from core.classes import Cog_Extension, Global_Func
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Mod(Cog_Extension):

    @commands.command(aliases=['cc'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)
        await ctx.send(Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\n此訊息將會在5秒鐘後刪除.'), delete_after=5.0)

def setup(bot):
   bot.add_cog(Mod(bot))