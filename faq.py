import discord
import asyncio
from discord.ext import commands

class FAQ():
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
        helpmsg = "The `Verified Nerd Role` is rewarded to users who post a selfie in #selfies.\nThe `Fully Verified Nerd` role is rewarded to users who post a selfie in #selfies holding a piece of paper with their Discord tag written on it.\nThese are aesthetic roles and have no real value, nor is there any requirement for users to verify themselves."
        await self.faq(ctx, helpmsg, "Verification")
    @commands.command()
    async def generations(self, ctx):
        helpmsg = "Generation roles are seniority roles based on join date.\n07/28 - 07/31: `Gen 0`\n08/01 - 08/31:\t`Gen 1`\n09/01 - 09/30:\t`Gen 2`\n. . . etc\nThe generation number increases on the 1st of every month."
        await self.faq(ctx, helpmsg, "Generations")
    @commands.command()
    async def partnership(self, ctx):
        helpmsg = "We only partner with people who are involved with our community. Anyone who joins this server with no other intention but to seek partnership will be denied."
        await self.faq(ctx, helpmsg, "Partnership")
    @commands.command()
    async def invite(self, ctx):
        await ctx.send("http://discord.gg/VnAjMgy")

    @commands.command()
    async def birthday(self, ctx):
        msg = """If you register your birthday with the bot, you will be given a special 'Birthday' role on your birthday. The role is placed above all other member roles in the hierarchy which will place you in a unique spot on the member list for the day.

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

def setup(bot):
    bot.add_cog(FAQ(bot))
