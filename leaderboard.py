import discord
import asyncio
import platform
import requests
import json
from datetime import datetime
from discord.ext import commands

class Leaderboard():
    def __init__(self, bot):
        self.bot = bot

    def find_longest_name(self, data):
        longest = 0
        for player in data:
            if len(player['username']) > longest:
                longest = len(player['username'])
        return longest + 2

    @commands.command(pass_context=True)
    async def top(self, ctx, param: int=0):
        if param < 0:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That page does not exist!")
            return
        apipage = "0"
        if param != 0:
            apipage = str(param - 1)
        session_requests = requests.session()
        url = "https://mee6.xyz/api/plugins/levels/leaderboard/455399951258746900?limit=10&page={}".format(apipage)
        page = session_requests.get(url)
        data = page.json()
        if len(data['players']) == 0:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That page does not exist!")
            return
        longest_name = self.find_longest_name(data['players'])
        message = "Server Leaderboard: Page {}\n\n{:<6}{:<{namelength}}{:<7}{:<6}\n".format(int(apipage) + 1, "Rank", "Name", "Level", "XP", namelength=longest_name) + ("-" * (19 + longest_name)) + "\n"
        count = 1 + (10 * int(apipage))
        for player in data['players']:
            message = message + "{:<6}{:<{namelength}}{:<7}{:<6}\n".format(count, player['username'], player['level'], player['xp'], namelength=longest_name) + ("-" * (19 + longest_name)) + "\n"
            count += 1
        nextpage = int(apipage) + 2
        message = message + "\nType e!top {} to see the next page.".format(nextpage)
        await self.bot.send_message(ctx.message.channel, "```python\n"+message+"```")

def setup(bot):
  bot.add_cog(Leaderboard(bot))
