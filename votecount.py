import discord
import asyncio
from discord.ext import commands

class Votecount(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def votecount(self, ctx, posts: int, max: int):
        globalvotecount = {}
        async for m in ctx.message.channel.history(limit=posts + 1):
            localvotecount = {}
            for reaction in m.reactions:
                users = await reaction.users().flatten()
                for u in users:
                    strid = str(u.id)

                    #if user reacted to their own submission
                    if u.id == m.author.id:
                        await ctx.message.channel.send(":no_entry_sign: " + u.name + " voted for their own submission: https://discordapp.com/channels/455399951258746900/" + str(ctx.message.channel.id) + "/" + str(m.id))

                    #keep a local count to check if a user reacted more than once on a single submission
                    if strid not in localvotecount:
                        localvotecount[strid] = 1
                    else:
                        if localvotecount[strid] != 2:
                            await ctx.message.channel.send(":no_entry_sign: " + u.name + " voted more than once on submission: https://discordapp.com/channels/455399951258746900/" + str(ctx.message.channel.id) + "/" + str(m.id))
                            localvotecount[strid] = 2

                    #keep track of global count to check if a user used more than the allotted votes
                    if strid not in globalvotecount:
                        globalvotecount[strid] = [1]
                        globalvotecount[strid].append([])
                        globalvotecount[strid][1].append("https://discordapp.com/channels/455399951258746900/" + str(ctx.message.channel.id) + "/" + str(m.id))
                    else:
                        globalvotecount[strid][0] = globalvotecount[strid][0] + 1
                        globalvotecount[strid][1].append("https://discordapp.com/channels/455399951258746900/" + str(ctx.message.channel.id) + "/" + str(m.id))

        for user in globalvotecount:
            if globalvotecount[user][0] > max:
                u = self.bot.get_user(int(user))
                message = ":no_entry_sign: " + u.name + " voted more than " + str(max) + " times!\n"
                for url in globalvotecount[user][1]:
                    message = message + url + "\n"
                await ctx.message.channel.send(message)
            elif globalvotecount[user][0] < max:
                u = self.bot.get_user(int(user))
                message = ":no_entry_sign: " + u.name + " did not use all " + str(max) + " of their votes!\n"
                for url in globalvotecount[user][1]:
                    message = message + url + "\n"
                await ctx.message.channel.send(message)
        await ctx.message.channel.send(":white_check_mark: Voting integrity check completed.")

def setup(bot):
  bot.add_cog(Votecount(bot))
