import discord
import asyncio
from discord.ext import commands

class Moderation():
    def __init__(self, bot):
        self.bot = bot
        self.muted = 523256295260946433

    @commands.command()
    async def ban(self, ctx, member: discord.Member=None, *, reason: str=None):
        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await ctx.send(":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await ctx.send(":no_entry_sign: Please tag the user you want to ban.")
            return
        elif ctx.message.author.id == member.id:
            await ctx.send(":no_entry_sign: You cannot ban yourself.")
            return
        banreason = ""
        if reason is None:
            banreason = "No reason specified"
        else:
            banreason = reason
        embed = discord.Embed(title="Has unleashed the ban hammer for,", description=banreason + "\n\nSay goodbye to")
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name)
        embed.set_footer(icon_url=member.avatar_url, text=member.display_name)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/524356833222328340/banhammer.gif")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await ctx.send(embed=embed)
        await ctx.message.guild.ban(member, reason=reason, delete_message_days=1)

    @commands.command()
    async def mute(self, ctx, member: discord.Member=None, *, reason: str=None):
        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await ctx.send(":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await ctx.send(":no_entry_sign: Please tag the user you want to mute.")
            return
        elif ctx.message.author == member:
            await ctx.send(":no_entry_sign: You cannot mute yourself.")
            return
        else:
            for r in member.roles:
                if r.id == self.muted:
                    await ctx.send(":no_entry_sign: That user is already muted!")
                    return
        mutereason = ""
        if reason is None:
            mutereason = "No reason specified"
        else:
            mutereason = reason
        embed = discord.Embed(title="Unleashes silence for,", description=mutereason + "\n\nDo not try to speak to")
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name)
        embed.set_footer(icon_url=member.avatar_url, text=member.display_name)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/499018104752308265/quiet.png")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        role = discord.utils.get(ctx.message.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def unmute(self, ctx, member: discord.Member=None):
        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await ctx.send(":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await ctx.send(":no_entry_sign: Please tag the user you want to mute.")
            return
        else:
            for r in member.roles:
                if r.id == self.muted:
                    role = discord.utils.get(ctx.message.guild.roles, name="Muted")
                    await member.remove_roles(role)
                    await ctx.send(":white_check_mark: " + member.mention + " has been unmuted by " + ctx.message.author.mention + "!")
                    await ctx.message.delete()

def setup(bot):
  bot.add_cog(Moderation(bot))
