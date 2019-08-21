import discord
import asyncio
from discord.ext import commands

class FAQ(commands.Cog):
    rules = ["`1`: Keep your posts in the appropriate channels.",

"`2`: Do not abuse mentionable roles.",

"`3`: Refrain from text and/or emoji spam.",

"`4`: Server advertisements are forbidden in chat, DMs, and nicknames.",

"`5`: No racism, hatred, personal attacks, harassment, or general hostility towards others.",

"`6`: Glitched blank nicknames, blank transparent profile pictures, and default profile pictures are forbidden.",

"`7`: Do not DM any users with the `DMs Closed` role.",

"""`8`: As a Discord user, you are responsible for knowledge of and abiding by the Discord ToS and community guidelines.
ToS: https://discordapp.com/terms
Community Guildelines: https://discordapp.com/guidelines
Treat the content of each document as an extension of this server's rule listing."""]

    def __init__(self, bot):
        self.bot = bot

    async def faq(self, ctx, message, question):
        embed = discord.Embed(description=message)
        embed.set_footer(text="Further questions or issues can be directed to Frankup")
        embed.set_author(name=question)
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await ctx.send(embed=embed)
        
    @commands.command()
    async def verification(self, ctx):
        helpmsg = """`Verified Nerd`
For users who post a selfie in """ + self.bot.get_channel(465697566571364352).mention + """

`Fully Verified Nerd`
For users who post a selfie in """ + self.bot.get_channel(465697566571364352).mention + """ holding a piece of paper with their Discord tag written on it.

These are aesthetic roles and hold no real value. We do not require users to verify themselves to participate on the server."""
        await self.faq(ctx, helpmsg, "Verification")
        await ctx.message.delete()
    @commands.command()
    async def roles(self, ctx):
        helpmsg = """Our self-assignable role channels, """ + self.bot.get_channel(581270202986266644).mention + """ and """ + self.bot.get_channel(580183333510709258).mention + """, unlock at level 2 which involves around 10 - 15 minutes of chatting to reach."""
        await self.faq(ctx, helpmsg, "Roles")
        await ctx.message.delete()
    @commands.command()
    async def colorroles(self, ctx):
        helpmsg = """Use """ + self.bot.get_channel(455400008246624257).mention + """ to issue any of the following commands.

`e!colors`
View the availible colors.

`e!addcolor color`
Apply a color role.

`e!removecolor`
Remove your current color role."""
        await self.faq(ctx, helpmsg, "Color Roles")
        await ctx.message.delete()
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("http://discord.gg/Hfjq8nU")
        await ctx.message.delete()

    @commands.command()
    async def birthday(self, ctx):
        msg = """Don't forget to register your birthday!

If you register your birthday with the bot, you will be given a special 'Birthday' role on your birthday. The role is placed above all other member roles in the hierarchy which will place you in a unique spot on the member list for the day.

Once your birthday is registered, you will be ***unable to change it*** in the future. If you abuse the bot to give yourself the birthday role early, then you will not have the role during your actual birthday. If I find out you abused the bot, you will be banned from the server.

To register your birthday, go into """ + self.bot.get_channel(455400008246624257).mention + """ and issue the following command:
`bday set [day], [month], [year], [gmt offset]`
Example input: `bday set 21, 9, 1991, -5`
Output: `Successfully set your birthday to September 21, 1991 GMT-5!`

For the bot to give you the 'Birthday' role at midnight with respect to your timezone, you must supply your timezone's GMT offset. [Click here](https://www.timeanddate.com/time/map/) and hover over your timezone. The number on the bottom of the timezone column is your GMT offset. If you're located within the 'UTC' offset, then your offset is 0."""
        embed = discord.Embed(description=msg, colour=0xffac33)
        embed.set_author(name="Birthday Registration")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/372188609425702915/517893082474348544/10812-birthday-cake.png')
        embed.set_footer(text="Further questions or issues can be directed to Frankup")
        await ctx.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(FAQ(bot))
