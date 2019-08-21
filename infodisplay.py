import discord
import asyncio
from discord.ext import commands

class Infodisplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def postembed(self, ctx, content):
        for x in range(0, len(content)):
            embed = discord.Embed(description=content[x][0], colour=content[x][3])
            embed.set_author(name=content[x][1])
            embed.set_thumbnail(url=content[x][2])
            await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        if ctx.message.author.id == 183457916114698241:
            content = [
["""Lonely Nerds is a welcoming and friendly community server to hang out, chat, and make friends. Please take a moment to read the rules and general information about the server below. 

Permanent invite link: `http://discord.gg/Hfjq8nU`""", "Welcome to Lonely Nerds!", "https://cdn.discordapp.com/attachments/372188609425702915/498973052445523983/lonelynerds.png", 0xFFC961],

["""`1`: Keep your posts in the appropriate channels.

`2`: Do not abuse mentionable roles.

`3`: Refrain from text and/or emoji spam.

`4`: Server advertisements are forbidden in chat, DMs, and nicknames.

`5`: No racism, hatred, personal attacks, harassment, or general hostility towards others.

`6`: Glitched blank nicknames, blank transparent profile pictures, and default profile pictures are forbidden.

`7`: Do not DM any users with the `DMs Closed` role.

`8`: As a Discord user, you are responsible for knowledge of and abiding by the Discord ToS and community guidelines.
ToS: https://discordapp.com/terms
Community Guildelines: https://discordapp.com/guidelines
Treat the content of each document as an extension of this server's rule listing.""", "Rules", "https://cdn.discordapp.com/attachments/372188609425702915/498962400171786250/clipboard.png", 0xFFFFFF],

["""Lonely Nerds uses MEE6 for level progression. You earn between 15 and 25 experience with each message. To prevent spam, you only gain experience once per minute.

Roles are rewarded based on level.
``` Level   Role
-----------------------------
  2:     Acquaintance
 10:     Buddy
 20:     Friend
 30:     Best Friend
 40:     Family
 50:     Loyal Family```

The self-assignable role channels, """ + self.bot.get_channel(581270202986266644).mention + """ and """ + self.bot.get_channel(580183333510709258).mention + """, are unlocked upon reaching level 2.

To view ranking information, use the """ + self.bot.get_channel(455400008246624257).mention + """ channel to issue any of the following commands.

`!rank`
View your ranking card.

`!levels`
View the server's leaderboard.

`e!top`
View an embedded version of the server's leaderboard.""", "Leveling", "https://cdn.discordapp.com/attachments/372188609425702915/498966600288960538/mee6.png", 0x60D1F6],

["""We have a wide variety of color roles to choose from! Head over to """ + self.bot.get_channel(455400008246624257).mention + """ and issue any of the following commands.

`e!colors`
View the availible colors.

`e!addcolor color`
Apply a color role.

`e!removecolor`
Remove your current color role.""", "Color Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498958897499865088/color-wheel.png", 0xFF0000],

["""Is there anything you would like to get off your chest with the comfort of anonymity?

Feel free to submit a confession to the Google form provided below. Your submission is anonymous and the confession will be displayed in """ + self.bot.get_channel(508109297385734144).mention + """.

Confessions must be **safe for work** and do ***not*** submit insulting remarks regarding another member on the server.

https://goo.gl/forms/CmugvdeHEU9rpuE52""", "Confessions", "https://cdn.discordapp.com/attachments/372188609425702915/511346995600818187/speaking-ICON.png", 0x000000],

["""Now that you are caught up on what you need to know, stop by """ + self.bot.get_channel(455399951258746902).mention + """ to say hi!""", "Thanks for reading!", "https://cdn.discordapp.com/attachments/372188609425702915/498988413966352384/wave.png", 0xFFDC5D] ]
            await self.postembed(ctx, content)
            await ctx.message.delete()

    @commands.command()
    async def photocontest(self, ctx, theme: str, deadline: str, *, description: str):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            content = [ ["""**Theme: ** """ + theme + """
 **Deadline: **""" + deadline + """

**Description:**\n""" +
description, "Photo Contest", "https://cdn.discordapp.com/attachments/372188609425702915/500029451250302976/1f4f7.png", 0x3C88C2],

["""- You must have the `Photographer` role to participate. Visit """ + self.bot.get_channel(581270202986266644).mention + """ to apply the role.
- Subit one photo to """ + self.bot.get_channel(487634576253124609).mention + """ by the specified deadline.
- Submissions must be original content and follow the specified theme.

__**How does it work?**__
Once the submission period ends, """ + self.bot.get_channel(487634576253124609).mention + """ will have emoji reactions enabled. Each server member may vote on up to 3 photographs by adding an emoji reaction to respective submissions.

The winner will receive the `Photo Contest Winner` role, bragging rights, and have their picture pinned to the channel.

Good luck!""", "Rules", "https://cdn.discordapp.com/attachments/372188609425702915/498962400171786250/clipboard.png", 0xFFFFFF] ]
            await self.postembed(ctx, content)
            await ctx.message.delete()

    @commands.command()
    async def voting(self, ctx, votes: str=None):
        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await ctx.send(":no_entry_sign: You do not have permission to use this command.")
            return
        if votes is None:
            await ctx.send(":no_entry_sign: Please specify the allotted number of votes. `e!voting number`")
            return
        content = [ ["""The submission period for this contest has ended and voting will begin!

__**Rules**__
Each server member is allotted **""" + votes + """** votes for this contest. All voting must be done in the form of an emoji reaction on the respective submission you wish to vote for.

- Do not vote for your own submission.
- Do not use more than **""" + votes + """** votes.
- Do not use more than one vote on a single submission.
- Do not vote with bias towards a specific submitter.
- Use *all* of your allotted votes. **If you do not use all *""" + votes + """* of your votes, your votes will be dismissed.**
- Contestants are expected to participate in voting! Failure to do so will result in a penalty to your submission's vote count.""", "Voting", "https://cdn.discordapp.com/attachments/372188609425702915/538543875648913411/2118-white-heavy-check-mark.png", 0x4bd37b] ]
        await self.postembed(ctx, content)
        await ctx.message.delete()

    @commands.command()
    async def drawingcontest(self, ctx, theme: str, deadline: str, *, description: str):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            msg = """**Theme: ** """ + theme + """
 **Deadline: **""" + deadline + """

 """ + description + """

 **Rules: **
You must have the `Artist` role to participate. Visit """ + self.bot.get_channel(487029031888486424).mention + """ to apply the role.
All drawings must be submitted to """ + self.bot.get_channel(508819194792378369).mention + """ by the specified deadline.
- Submissions must be original content and follow the specified theme.
- A maximum of two drawings may be submitted.
- Do **not** vote for your own photos during the voting period.

**How does it work?**
Once the submission period ends, """ + self.bot.get_channel(508819194792378369).mention + """ will have emoji reactions enabled.
Each user may vote on up to 3 drawings by adding an emoji reaction to respective submissions. Users are limited to one vote per picture. Multiple emoji reactions on a post by the same user will not be counted.

The winner will receive a special role, bragging rights, have their drawing pinned, and choose the theme for the next contest.

Good luck!"""
            embed = discord.Embed(title="Art Contest", description=msg, colour=0x3C88C2)
            embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " has an announcement!")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/510862808255037451/1f58c.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def confess(self, ctx):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            msg = """Is there anything you would like to get off your chest with the comfort of anonymity?

Feel free to submit a confession to the Google form provided below. Your submission is anonymous and the confession will be displayed in """ + self.bot.get_channel(508109297385734144).mention + """.

Confessions must be **safe for work** and do ***not*** submit insulting remarks regarding another member on the server.

https://goo.gl/forms/CmugvdeHEU9rpuE52"""
            embed = discord.Embed(title="Confessions", description=msg, colour=0x000000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/511346995600818187/speaking-ICON.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def helper(self, ctx):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            helper_role = discord.utils.get(ctx.message.guild.roles, name="Helper")
            msg = """We have a group of volunteers who chose to opt-in for the """ + helper_role.mention + """ role. Feel free to mention """ + helper_role.mention + """ if you are in need of someone to speak to.

Please do not mention the role as soon as you post. Give people some time to read and respond first."""
            embed = discord.Embed(title="Helpers", description=msg, colour=0x292f33)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/527640560421306388/10582-busts-in-silhouette.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()

def setup(bot):
  bot.add_cog(Infodisplay(bot))
