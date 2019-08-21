import discord
import asyncio
from discord.ext import commands

class Colors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_ids = {
            476625775718694922: "Red", 479391249170956309: "Mint", 476914831744827392: "Blue", 475637467370881027: "Pink", 480098398461231104: "Orchid",
            480099403416469525: "Purple", 480100032373325824: "Yellow", 480100441162645525: "White", 480101544981692442: "Orange", 480102271133417504: "Lime Green",
            480103088145825793: "Green", 480103452408807424: "Black", 480104711748583455: "Cyan", 480105715877543936: "Beige", 480106440460337155: "Sky Blue",
            480106946427355136: "Coral", 480107033203441675: "Teal", 480107825050288131: "Violet", 480108741186813952: "Magenta", 480108169977266178: "Gold",
            480109574813253683: "Turquoise", 480108741019172864: "Silver", 480126003704889349: "Crimson", 480127634961858570: "Eggshell", 480189683842809865: "Royal Blue",
            480100032427589632: "Navy", 479889427074908161: "Salmon", 480106945911586818: "Sea Green", 480238460523773953: "Dark Red", 480239814768197643: "Slate",
            480124829085859840: "Dark Green", 511980949270036490: "Brown", 577311808927301643: "Lavendar", 577311805592829962: "Lemon"
        }

    @commands.command(aliases=['colours'])
    async def colors(self, ctx):
        with open('colors.png', 'rb') as f:
            await ctx.send(file=discord.File(f, 'colors.png'))

    @commands.command(aliases=['addcolour', 'color', 'c', 'ac'])
    async def addcolor(self, ctx, *, color: str=None):
        if color is None:
            await ctx.send(":no_entry_sign: Try supplying a color.")
            with open('colors.png', 'rb') as f:
                await ctx.send(file=discord.File(f, 'colors.png'))
            return
        if len(ctx.message.author.roles) <= 1:
            await ctx.send(":no_entry_sign: You must reach level 2 before you can have a color role.")
            return
        entered_color = color.title()
        role = discord.utils.get(ctx.message.guild.roles, name=entered_color)
        has_role = False
        for r in ctx.message.author.roles:
            if r.id in self.role_ids:
                has_role = True
        if role is None or role.name not in self.role_ids.values():
            await ctx.send(":no_entry_sign: That color was not found. Please refer to the color listing below.")
            with open('colors.png', 'rb') as f:
                await ctx.send(file=discord.File(f, 'colors.png'))
            return
        elif role in ctx.message.author.roles:
            await ctx.send(":no_entry_sign: You already have that color.")
            return
        else:
            try:
                if has_role is True:
                    await ctx.message.author.remove_roles(r)
                await ctx.message.author.add_roles(role)
                await ctx.send(":white_check_mark: Color added!")
            except discord.Forbidden:
                await ctx.send("I don't have perms to add roles.")

    @commands.command(aliases=['removecolour'])
    async def removecolor(self, ctx):
        for r in ctx.message.author.roles:
            if r.id in self.role_ids:
                try:
                    await ctx.message.author.remove_roles(r)
                    await ctx.send(":white_check_mark: Color removed!")
                except discord.Forbidden:
                    await ctx.send("I don't have perms to add roles.")
                return

def setup(bot):
  bot.add_cog(Colors(bot))
