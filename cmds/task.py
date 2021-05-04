import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        #async def interval():
        #    await self.bot.wait_until_ready()
        #    self.channel = self.bot.get_channel(838370690109407242)
        #   while not self.bot.is_closed():
        #        await self.channel.send("Hi I'm running!")
        #        await asyncio.sleep(5) #單位:秒
    
        #self.bg_task = self.bot.loop.create_task(interval())


        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(838370690109407242)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter == 0:
                    await self.channel.send('Task Working!')
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
             json.dump(jdata, jfile, indent=4)
        await ctx.send(f"時間已設置完畢!")


def setup(bot):
    bot.add_cog(Task(bot))