import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    async def activiy_task():
      await self.bot.wait_until_ready()
      while not self.bot.is_closed():
        activity = ['SD快開服', '運作平台: Eri24816 租的 server', '現在改用 slash command (/)', 'ROW 網站: https://greenslime1024.github.io/posts/row/', 'Made By GreenSlime1024']
        for i in range(len(activity)-1):
          await self.bot.change_presence(activity=discord.Game(name=activity[i]))
          await asyncio.sleep(15)
        
    self.bg_task = self.bot.loop.create_task(activiy_task())

def setup(bot):
  bot.add_cog(Task(bot))