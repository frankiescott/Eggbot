import discord
import asyncio
import platform
import json
from discord.ext import commands
#import os
#os.chdir("C:\\Users\\hxcfr\\Desktop\\discord bot")
class Teams():
    def __init__(self, bot):
        self.bot = bot

    def getdata(self, flag: int=0):
        list = []
        #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'r') as fp:
        with open('teamdata.json', 'r') as fp:
            contents = json.load(fp)
            count = 0
            for c in contents:
                list.append([])
                list[count].extend([c, contents[c][0], contents[c][1]])
                count += 1
        if flag == 0:
            n = len(list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if list[j][2] < list[j+1][2]:
                        list[j], list[j+1] = list[j+1], list[j]
        return list

    @commands.command(pass_context=True)
    async def viewpoints(self, ctx):
        list = self.getdata()
        n = len(list)
        embed = discord.Embed(title="Team Leaderboard", colour=0xffcc4d)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/510934259121520661/1f3c6.png")
        emojis = ["🥇", "🥈", "🥉", ":four:"]
        for i in range(n):
            embed.add_field(name=emojis[i] + " __" + list[i][0] + "__", value="Leader: " + ctx.message.server.get_member(list[i][1]).mention + "\nScore: **" + str(list[i][2]) + "**", inline=True)
        await self.bot.send_message(ctx.message.channel, embed=embed)

    @commands.command(pass_context=True)
    async def setleader(self, ctx, team: str, id: str):
        if ctx.message.author.id != "183457916114698241":
            return
        if ctx.message.server.get_member(id) is None:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: User not found!")
            return
        else:
            #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'r') as fp:
            with open('teamdata.json', 'r') as fp:
                contents = json.load(fp)
                if team not in contents:
                    await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Invalid team name!")
                    return
                else:
                    contents[team][0] = id
                    await self.bot.send_message(ctx.message.channel, ":white_check_mark: " + ctx.message.server.get_member(id).mention + " is now the team leader for " + team + "!")
            #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'w') as fp:
            with open('teamdata.json', 'w') as fp:
                json.dump(contents, fp)

    @commands.command(pass_context=True)
    async def award(self, ctx, points: int, *, team: str):
        #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'r') as fp:
        with open('teamdata.json', 'r') as fp:
            contents = json.load(fp)
            if team not in contents:
                await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Team not found!")
                return
            else:
                contents[team][1] += points
                await self.bot.send_message(ctx.message.channel, ":white_check_mark: " + team + " has been awarded " + str(points) + " points!")
        #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'w') as fp:
        with open('teamdata.json', 'w') as fp:
            json.dump(contents, fp)

    @commands.command(pass_context=True)
    async def resetpoints(self, ctx):
        if str(ctx.message.author.id) != "183457916114698241":
            return

        #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'r') as fp:
        with open('teamdata.json', 'r') as fp:
            contents = json.load(fp)
            for c in contents:
                contents[c][1] = 0
            await self.bot.send_message(ctx.message.channel, ":white_check_mark: Team points have been reset!")
        #with open('C:\\Users\\hxcfr\\Desktop\\discord bot\\teamdata.json', 'w') as fp:
        with open('teamdata.json', 'w') as fp:
            json.dump(contents, fp)

    @commands.command(pass_context=True)
    async def teaminfo(self, ctx):
        if str(ctx.message.author.id) != "183457916114698241":
            return
        content = [

["""There are four teams modeled by the houses of Hogwarts. Join the house that you believe best suits your character. You will be given a role representing your house that will grant you access to a unique team channel which enables you to participate in team events. Click the emoji reaction beneath a house's description to join that house.""", "Server Teams", "https://cdn.discordapp.com/attachments/372188609425702915/511697788954869760/2694.png", 0xccd6dd],

["""The House of Gryffindor values courage, bravery, nerve, and chivalry. The Gryffindor mascot is a lion.""", "Gryffindor", "https://cdn.discordapp.com/attachments/372188609425702915/511727611227930624/main-qimg-44ac99d5412f2f8904b023a83a6a4929.png", 0xd1222d],

["""The House of Ravenclaw values intelligence, creativity, learning, and wit. The Ravenclaw mascot is an eagle.""", "Ravenclaw", "https://cdn.discordapp.com/attachments/372188609425702915/511727591976075264/main-qimg-7ce3c359881af177a2f719b972c59a66.png", 0x05a8cc],

["""The House of Hufflepuff values hard work, patience, justice, and loyalty. The Hufflepuff mascot is a badger.""", "Hufflepuff", "https://cdn.discordapp.com/attachments/372188609425702915/511727558895861760/main-qimg-6cde2f92a034c500874c57234a1a4d01.png", 0xf7dd20],

["""The House of Slytherin values ambition, cunning, leadership, and resourcefulness. The Slytherin mascot is a serpent.""", "Slytherin", "https://cdn.discordapp.com/attachments/372188609425702915/511727537513168924/main-qimg-2f3a2cd2364bcc038264f8f9ee6a5c60.png", 0x2ca84f],

["""React with the corresponding emoji on this post to join the specified house!

If you are unsure of which house to join, try taking the following quiz:
http://brainfall.com/quizzes/which-hogwarts-house-would-you-be-in/

React with ❤ to join Gryffindor.
React with 💙 to join Ravenclaw.
React with 💛 to join Hufflepuff.
React with 💚 to join Slytherin.""", "The choice is yours!", "https://cdn.discordapp.com/attachments/372188609425702915/511697788954869760/2694.png", 0xccd6dd] ]

        for x in range(0, len(content)):
            embed = discord.Embed(description=content[x][0], colour=content[x][3])
            embed.set_author(name=content[x][1])
            embed.set_thumbnail(url=content[x][2])
            await self.bot.send_message(ctx.message.channel, embed=embed)

def setup(bot):
  bot.add_cog(Teams(bot))