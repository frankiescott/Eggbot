import discord
import asyncio
from discord.ext import commands

class Customroles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.id_map = { 
            "183457916114698241": 611236575841615872, #frank
            "227898945915846656": 611249888839073832, #deb
            "468268312900403200": 611249892135927810, #rachel
            "212767167848906752": 611249886775738388, #gabe
            "169256252453421057": 611249890030256141, #sarah
            "259589515021123585": 611250245778669583, #andrew
            "104712945413447680": 611249891305455617, #chrizzer
            "491399864505335822": 611250247049412628, #kim
            "325083160406917129": 611250239126372354, #keatzee
            "337119543350788098": 611249893628968976, #solessa
            "230471814860505088": 611249882572783658, #jeff
            "222921229001162752": 611249884669935616, #chuck
            "324678737377492993": 611249892601626644, #emily
            "430717577195421696": 611250236190621697, #jon
            "252394224337682434": 611250243853615124, #miko
            "298580634228490243": 611249893713117193, #tony
            "409865234786811916": 611250242024898600  #nate
        }
        self.not_allowed = ["admin", "mod", "frank", "deb", "bot", "nerd", "geek", "egg bot", "eggbot", "birthdaybot", "zira", "mee6", "tatsumaki", "gaius cicereius+"]

    @commands.command()
    async def setrolename(self, ctx, *, name: str=None):
        if name.lower() in self.not_allowed:
            await ctx.send(":no_entry_sign: You cannot have that role name, sorry!")
            return
        if name is None:
            await ctx.send(":no_entry_sign: Please provide a name to apply to your role.")
            return
        if str(ctx.author.id) not in self.id_map:
            await ctx.send(":no_entry_sign: Only members ranked Loyal Family or Family have access to this command.")
            return
        role_id = self.id_map[str(ctx.author.id)]
        role = discord.utils.get(ctx.guild.roles, id=role_id)
        if role_id not in ctx.author.roles:
            await ctx.author.add_roles(role)
        await role.edit(name=name)
        await ctx.send(":white_check_mark: Your role name has been changed to " + name + "!")

    @commands.command()
    async def setrolecolor(self, ctx, color: str=None):
        if color is None:
            await ctx.send(":no_entry_sign: Please provide a color to apply to your role.")
            return
        if len(color) != 6:
            await ctx.send(":no_entry_sign: Role colors must be provided as a six digit hexadecimal code.")
            return
        if str(ctx.author.id) not in self.id_map:
            await ctx.send(":no_entry_sign: Only members ranked Loyal Family or Family have access to this command.")
            return
        role_id = self.id_map[str(ctx.author.id)]
        role = discord.utils.get(ctx.guild.roles, id=role_id)
        if role_id not in ctx.author.roles:
            await ctx.author.add_roles(role)
        hex_str = "0x" + color
        try:
            await role.edit(colour=discord.Colour(int(hex_str, 16)))
            await ctx.send(":white_check_mark: Your role color has been changed to #" + color + "!")
        except ValueError:
            await ctx.send(":no_entry_sign: An error has been raised with the provided hexadecimal code.\n-Hexadecimal numbers should only contain digits 0-9 and/or letters A-F.\n-If your input has a pound sign (#) remove it and try again.\n-Use https://htmlcolorcodes.com/color-picker to find the correct hexadecimal number for your desired color.")

def setup(bot):
    bot.add_cog(Customroles(bot))