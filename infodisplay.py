import discord
import asyncio
from discord.ext import commands

class Infodisplay():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tools(self, ctx):
        if ctx.message.author.id == 183457916114698241:
            content = [
["""`?warn mention/userid`
Warns a user.

`?warnlist mention/userid`
Lists a user's warnings.

`?purgewarn warnID`
Roles: Nerd/Geek
Deletes a warning from the user's record.

`?pardon warnID`
Roles: Nerd/Geek
Crosses out the specified warning but does not delete it from the user's record.""", "Warning", "https://cdn.discordapp.com/attachments/372188609425702915/499017587464863784/caution.png", 0xFFCC4D],

["""`?mute mention/userID time reason`
Mutes a user for a certain amount of minutes. The reason is an optional field.

`?unmute mention/userID`
Unmutes a user""", "Muting", "https://cdn.discordapp.com/attachments/372188609425702915/499018104752308265/quiet.png", 0xFFC961],

["""All mods have the ability to delete messages individually through the Discord interface. The purge command is typically used for bulk deletion.

`?purge amount`
Deletes the last specified amount of messages in a channel.

`?purge amount @user`
Deletes the last specified amount of messages from a specific user in a channel.""", "Purging", "https://cdn.discordapp.com/attachments/372188609425702915/499024141265928242/fire.png", 0xF4900C],

["""All commands below are restricted to the Nerd and Geek roles.

`?panic`
Enables or disables panic mode which mutes all new users who join the server.

`?lock`
Disables everyone's permissions to talk in a channel.

`?unlock`
Enables everyone's permissions to talk in a channel.

`?freeze`
Freezes the entire server. *USE SPARRINGLY!*

`?thaw`
Thaws the server from a freeze.""", "Raid Prevention", "https://cdn.discordapp.com/attachments/372188609425702915/499018946180284417/noentry.png", 0xBE1931],

["""When users post a selfie in #selfies, they get the `Verified Nerd` role. When users post a selfie with visible proof that it is them, they get the `Fully Verified Nerd` role. Visible proof involves a piece of paper with their display name or discord tag written on it, or a selfie with the server visible in the background.

`e!verify @user`
Applies the `Verified Nerd` role to the tagged user.

`e!fullyverify @user`
Applies the `Fully Verified Nerd` role to the tagged user. If the user already has the `Verified Nerd` role, it will be removed and replaced with `Fully Verified Nerd`.""", "Verification", "https://cdn.discordapp.com/attachments/372188609425702915/499023938157019156/verified.png", 0x5D93FE],

["""The following commands can be issued to provide a quick response to a user who asks a frequently asked question.

`e!invite`
Posts the server's permanent invite link.

`e!verification`
Explains what the verified roles mean.

`e!generations`
Explains what the generation roles mean.""", "Frequently Asked Questions", "https://cdn.discordapp.com/attachments/372188609425702915/499024476630024193/faq.png", 0xBE1931] ]
            for x in range(0, len(content)):
                embed = discord.Embed(description=content[x][0], colour=content[x][3])
                embed.set_author(name=content[x][1])
                embed.set_thumbnail(url=content[x][2])
                await ctx.send(embed=embed)


    @commands.command()
    async def games(self, ctx):
        if ctx.message.author.id == 183457916114698241:
            content = [

["""Let out your frustration with an 'oof'

'Oofs' can be varied in any capital letter and lower case letter sequence.
Ex: 'ooF', 'OOf', 'OOF'

'Oofs' can contain spaces between each letter.
Ex: 'o o f'

These two rules can be combined.
Ex: 'O O F', 'o o F', 'o O F'""", "Oofs", "https://cdn.discordapp.com/attachments/372188609425702915/509811678896979989/OOF.png", 0xbb3434],

["""Participate in the count to 10,000!

Post the next **integer** value in the sequence by incrementing the previous poster's number by 1.
Ex: 1, 2, 3, 4, . . ., 5678, 5679, 5680, 5681, . . .""", "10,000 numbers", "https://cdn.discordapp.com/attachments/372188609425702915/509813447786102808/11192-input-symbol-for-numbers.png", 0x3a88c3],

["""Chain words together!

Post a word that starts with a letter that the previous poster's word ends with.
Ex: Airplane, Exceptional, Liquid, Dinosaur

Do not use acronyms or made up words. Use words that can typically be found in a dictionary.""", "Wordie", "https://cdn.discordapp.com/attachments/372188609425702915/509815635598114816/kisspng-emoji-monster-hunter-world-speech-language-meanin-5ae36fbe1117a6.51433403152485471807.png", 0xbdddf4],

["""Get to know your fellow server members!

Provide an answer to the previous poster's question, then ask a question of your own for the next person.

Questions must be meaningful and thoughtful, something you would typically ask to learn more about an individual. Avoid **would you rather** type questions that are meant to be comical and illicit a controversial response.

Examples of **acceptable** questions:
'Do you prefer pinapple on pizza?'
'Coffee or tea?'
'If you could travel to any country in the world, where would you go?'

Examples of **unacceptable** questions:
'Does my girlfriend love me?'
'Should I go to school today?'
'Would you rather eat a handful of worms or lay in a tub of snakes?'""", "Question and Answer", "https://cdn.discordapp.com/attachments/372188609425702915/509817219438477314/f05.png", 0xffcc4d] ]

            for x in range(0, len(content)):
                embed = discord.Embed(description=content[x][0], colour=content[x][3])
                embed.set_author(name=content[x][1])
                embed.set_thumbnail(url=content[x][2])
                await ctx.send(embed=embed)


    @commands.command()
    async def info(self, ctx):
        if ctx.message.author.id == 183457916114698241:
            selfies = self.bot.get_channel(465697566571364352)
            roles = self.bot.get_channel(487029031888486424)
            suggestions = self.bot.get_channel(473964680004763659)
            content = [
["""We are a community server to hang out, chat, and make friends. Don't be shy! We love meeting and talking to new people. Please take a moment to read the rules and general information about the server below.

If you have any questions, feel free to ask in """ + self.bot.get_channel(473964680004763659).mention + """!

Permanent invite link: `http://discord.gg/VnAjMgy`""", "Welcome to Lonely Nerds!", "https://cdn.discordapp.com/attachments/372188609425702915/498973052445523983/lonelynerds.png", 0xFFC961],

["""`1`: Follow the Discord TOS.

`2`: Keep your posts in the appropriate channels.

`3`: Do not DM any users with the `DMs closed` role.

`4`: Advertisements are forbidden in chat, DMs, and nicknames.

`5`: We encourage free speech and open discussion, but racism, hatred, personal attacks, harassment, or general hostility towards others will *not* be tolerated.

`6`: Do not abuse mentionable roles.""", "Server Rules", "https://cdn.discordapp.com/attachments/372188609425702915/498962400171786250/clipboard.png", 0xFFFFFF],

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

["""We have self-assignable roles you can obtain in """ + roles.mention + """

We also have award based roles that can be obtained.

`Verified Nerd`
Awarded to those who post a selfie in """ + selfies.mention + """.

`Fully Verified Nerd`
Awarded to those who post a selfie in """ + selfies.mention + """ holding a piece of paper with your Discord tag written on it.

`Supporter`
Awarded to those who make a suggestion in """ + suggestions.mention + """ that gets implemented.

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
Head over to """ + roles.mention + """ and grab the `Artist` role if you are interested in participating in art contests, and grab the `Photographer` role if you are interested in participating in photography contests.

Check """ + self.bot.get_channel(508819194792378369).mention + """ for the latest art contest and """ + self.bot.get_channel(487634576253124609).mention + """ for the latest photography contest.

We also host other unique contests you should look out for!""", "Contests", "https://cdn.discordapp.com/attachments/372188609425702915/510934259121520661/1f3c6.png", 0xffcc4d],

["""Now that you are all caught up on what you need to know, stop by """ + self.bot.get_channel(455399951258746902).mention + """ to say hi!""", "Thanks for reading!", "https://cdn.discordapp.com/attachments/372188609425702915/498988413966352384/wave.png", 0xFFDC5D] ]
            for x in range(0, len(content)):
                embed = discord.Embed(description=content[x][0], colour=content[x][3])
                embed.set_author(name=content[x][1])
                embed.set_thumbnail(url=content[x][2])
                await ctx.send(embed=embed)

    @commands.command()
    async def photocontest(self, ctx, theme: str, deadline: str, *, description: str):
        if ctx.message.author.id == 183457916114698241 or ctx.message.author.id == 324678737377492993:
            msg = """**Theme: ** """ + theme + """
 **Deadline: **""" + deadline + """

 """ + description + """

 **Rules: **
- You must have the `Photographer` role to participate. Visit """ + self.bot.get_channel(487029031888486424).mention + """ to apply the role.
- All photos must be submitted to """ + self.bot.get_channel(487634576253124609).mention + """ by the specified deadline.
- Submissions must be original content and follow the specified theme.
- A maximum of two photos may be submitted.
- Do **not** vote for your own photos during the voting period.

**How does it work?**
Once the submission period ends, """ + self.bot.get_channel(487634576253124609).mention + """ will have emoji reactions enabled.
Each user may vote on up to 3 photographs by adding an emoji reaction to respective submissions. Users are limited to one vote per picture. Multiple emoji reactions on a post by a single user will not be counted.

The winner will receive a special role, bragging rights, have their picture pinned, and choose the theme for the next contest.

Good luck!"""
            embed = discord.Embed(title="Photo Contest", description=msg, colour=0x3C88C2)
            embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " has an announcement!")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/500029451250302976/1f4f7.png")
            await ctx.send(embed=embed)
            await ctx.message.delete(ctx.message)

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
