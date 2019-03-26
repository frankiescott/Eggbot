import discord
import asyncio
from discord.ext import commands

class Infodisplay():
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
["""We are a community server to hang out, chat, and make friends. Don't be shy! We love meeting and talking to new people. Please take a moment to read the rules and general information about the server below.

If you have any questions, feel free to ask in """ + self.bot.get_channel(473964680004763659).mention + """!

Permanent invite link: `http://discord.gg/VnAjMgy`""", "Welcome to Lonely Nerds!", "https://cdn.discordapp.com/attachments/372188609425702915/498973052445523983/lonelynerds.png", 0xFFC961],

["""`1`: Follow the Discord TOS.

`2`: Keep your posts in the appropriate channels.

`3`: Do not DM any users with the `DMs closed` role.

`4`: Advertisements are forbidden in chat, DMs, and nicknames.

`5`: We encourage free speech and open discussion, but racism, hatred, personal attacks, harassment, or general hostility towards others will *not* be tolerated.

`6`: Refrain from posting irrelevant links and/or images in """ + self.bot.get_channel(455399951258746902).mention + """.""", "Server Rules", "https://cdn.discordapp.com/attachments/372188609425702915/498962400171786250/clipboard.png", 0xFFFFFF],

["""This server uses MEE6's leveling system. Every time you send a message, you earn an amount of experience between 15 and 25. To prevent spam, you can only gain experience once per minute.

Roles are rewarded based on level.
``` Level   Role
-----------------------------
  3:     Newbie
  6:     Acquaintance
  9:     Familiar
 12:     Buddy
 15:     Casual Friend
 18:     Friend
 21:     Good Friend
 24:     Close Friend
 27:     Best Friend
 30:     Best Friend Forever
 35:     Family
 40:     Loyal Family```

To view ranking information, use the """ + self.bot.get_channel(455400008246624257).mention + """ channel to issue any of the following commands.

`!rank`
View your ranking card.

`!levels`
View the server's leaderboard.

`e!top`
View an embedded version of the server's leaderboard.""", "Leveling", "https://cdn.discordapp.com/attachments/372188609425702915/498966600288960538/mee6.png", 0x60D1F6],

["""We have self-assignable roles you can obtain in """ + self.bot.get_channel(487029031888486424).mention + """

We also have award based roles that can be obtained.

`Verified Nerd`
Awarded to those who post a selfie in """ + self.bot.get_channel(465697566571364352).mention + """.

`Fully Verified Nerd`
Awarded to those who post a selfie in """ + self.bot.get_channel(465697566571364352).mention + """ holding a piece of paper with your Discord tag written on it.

`Supporter`
Awarded to those who make a suggestion in """ + self.bot.get_channel(473964680004763659).mention + """ that gets implemented.

`Champion`
Awarded to those who win server events or contests.""", "Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498980224197722123/shield.png", 0x55ACEE],

["""To use the color role system, use the """ + self.bot.get_channel(455400008246624257).mention + """ channel to issue any of the following commands.

`e!colors`
View the availible colors.

`e!addcolor color`
Apply a color role.

`e!removecolor`
Remove your current color role.""", "Color Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498958897499865088/color-wheel.png", 0xFF0000],

["""Check out our contests!

We host weekly photography and drawing contests.
Head over to """ + self.bot.get_channel(487029031888486424).mention + """ and grab the `Artist` role if you are interested in participating in art contests, and grab the `Photographer` role if you are interested in participating in photography contests.

Check """ + self.bot.get_channel(508819194792378369).mention + """ for the latest art contest and """ + self.bot.get_channel(487634576253124609).mention + """ for the latest photography contest.

We also host other unique contests you should look out for!""", "Contests", "https://cdn.discordapp.com/attachments/372188609425702915/510934259121520661/1f3c6.png", 0xffcc4d],

["""Is there anything you would like to get off your chest with the comfort of anonymity?

Feel free to submit a confession to the Google form provided below. Your submission is anonymous and the confession will be displayed in """ + self.bot.get_channel(508109297385734144).mention + """.

Confessions must be **safe for work** and do ***not*** submit insulting remarks regarding another member on the server.

https://goo.gl/forms/CmugvdeHEU9rpuE52""", "Confessions", "https://cdn.discordapp.com/attachments/372188609425702915/511346995600818187/speaking-ICON.png", 0x000000],

["""Now that you are all caught up on what you need to know, stop by """ + self.bot.get_channel(455399951258746902).mention + """ to say hi!""", "Thanks for reading!", "https://cdn.discordapp.com/attachments/372188609425702915/498988413966352384/wave.png", 0xFFDC5D] ]
            await self.postembed(ctx, content)
            await ctx.message.delete()

    @commands.command()
    async def photocontest(self, ctx, theme: str, deadline: str, *, description: str):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            content = [ ["""**Theme: ** """ + theme + """
 **Deadline: **""" + deadline + """

__**Description**__\n""" +
description, "Photo Contest", "https://cdn.discordapp.com/attachments/372188609425702915/500029451250302976/1f4f7.png", 0x3C88C2],

["""- You must have the `Photographer` role to participate. Visit """ + self.bot.get_channel(487029031888486424).mention + """ to apply the role.
- Subit one photo to """ + self.bot.get_channel(487634576253124609).mention + """ by the specified deadline.
- Submissions must be original content and follow the specified theme.

__**How does it work?**__
Once the submission period ends, """ + self.bot.get_channel(487634576253124609).mention + """ will have emoji reactions enabled. Each server member may vote on up to 3 photographs by adding an emoji reaction to respective submissions.

The winner will receive the `Photo Contest Winner` role, bragging rights, and have their picture pinned to the channel.

Good luck!""", "Rules", "https://cdn.discordapp.com/attachments/372188609425702915/498962400171786250/clipboard.png", 0xFFFFFF] ]
            await self.postembed(ctx, content)
            await ctx.message.delete()
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
