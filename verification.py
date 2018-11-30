import discord
import asyncio
from discord.ext import commands

class Verification():
    def __init__(self, bot):
        self.bot = bot
        self.verified_ids = ["473649456043261953", "473649831328481282"]

    @commands.command(pass_context=True)
    async def verify(self, ctx, member: discord.Member=None):
        mod_role = discord.utils.get(ctx.message.server.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Please tag the user you want to verify.")
            return
        else:
            for r in member.roles:
                if r.id in self.verified_ids:
                    await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That user is already verified!")
                    return
            role = discord.utils.get(ctx.message.server.roles, name="Verified Nerd🤓")
            await self.bot.add_roles(member, role)
            msg = "The `Verified Nerd` role is rewarded to users who post a selfie in " + self.bot.get_channel("465697566571364352").mention + ".\n\nThe `Fully Verified Nerd` role is rewarded to users who post a selfie in " + self.bot.get_channel("465697566571364352").mention + " holding a piece of paper with their Discord tag written on it.\n\nThese are aesthetic roles and have no real value, nor is there any requirement for users to verify themselves."
            embed = discord.Embed(description=msg, colour=0x5D93FE)
            embed.set_author(icon_url=member.avatar_url, name=member.display_name + " has been verified!")
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text="Verified by " + ctx.message.author.display_name)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/499023938157019156/verified.png")
            await self.bot.send_message(ctx.message.channel, embed=embed)
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def fullyverify(self, ctx, member: discord.Member=None):
        mod_role = discord.utils.get(ctx.message.server.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Please tag the user you want to verify.")
            return
        else:
            for r in member.roles:
                if r.id == "473649831328481282":
                    await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That user is already fully verified!")
                    return
            try:
                role = discord.utils.get(ctx.message.server.roles, name="Verified Nerd🤓")
                member.roles.remove(role)
            except:
                pass
            role = discord.utils.get(ctx.message.server.roles, name="Fully Verified Nerd🤓")
            member.roles.append(role)
            await self.bot.replace_roles(member, *member.roles)
            msg = "The `Verified Nerd` role is rewarded to users who post a selfie in " + self.bot.get_channel("465697566571364352").mention + ".\n\nThe `Fully Verified Nerd` role is rewarded to users who post a selfie in " + self.bot.get_channel("465697566571364352").mention + " holding a piece of paper with their Discord tag written on it.\n\nThese are aesthetic roles and have no real value, nor is there any requirement for users to verify themselves."
            embed = discord.Embed(description=msg, colour=0x5D93FE)
            embed.set_author(icon_url=member.avatar_url, name=member.display_name + " has been fully verified!")
            embed.set_footer(icon_url=ctx.message.author.avatar_url, text="Verified by " + ctx.message.author.display_name)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/499023938157019156/verified.png")
            await self.bot.send_message(ctx.message.channel, embed=embed)
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def nitro(self, ctx, member: discord.Member=None):
        mod_role = discord.utils.get(ctx.message.server.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Please tag the user.")
            return
        else:
            for r in member.roles:
                if r.id == "484369794897018930":
                    await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That user can already nitro flex!")
                    return
            role = discord.utils.get(ctx.message.server.roles, name="Nitro Flexer💰")
            await self.bot.add_roles(member, role)
            await self.bot.send_message(ctx.message.channel, ":white_check_mark: " + member.mention + " can now flex in " + self.bot.get_channel("484369598196482049").mention)

    @commands.command(pass_context=True)
    async def denitro(self, ctx, member: discord.Member=None):
        mod_role = discord.utils.get(ctx.message.server.roles, name="Mod")
        if mod_role not in ctx.message.author.roles:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: You do not have permission to use this command.")
            return
        elif member is None:
            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: Please tag the user.")
            return
        else:
            for r in member.roles:
                if r.id == "484369794897018930":
                    role = discord.utils.get(ctx.message.server.roles, name="Nitro Flexer💰")
                    await self.bot.remove_roles(member, role)
                    await self.bot.send_message(ctx.message.channel, ":white_check_mark: " + member.mention + " can no longer flex in " + self.bot.get_channel("484369598196482049").mention)
                    return

            await self.bot.send_message(ctx.message.channel, ":no_entry_sign: That user cannot nitro flex!")
            return

def setup(bot):
    bot.add_cog(Verification(bot))
