import discord
import asyncio
import platform
import requests
import time
import datetime
from keys import API_KEY
from discord.ext.commands import Bot
from discord.ext import commands

async def run():
    bot = Bot()
    try:
        await bot.start(API_KEY)
    except KeyboardInterrupt:
        await bot.logout()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="e!")
        self.remove_command("help")
        self.add_command(self.help)
        self.add_command(self.status)
        self.add_command(self.mily)
        self.add_command(self.poll)
        self.add_command(self.yao)
        self.add_command(self.gaming)

        self.gaming_timer = 0

    async def countdown(self, message):
        self.gaming_timer = 3600
        gaming_role = discord.utils.get(message.guild.roles, name="Gaming")
        await gaming_role.edit(mentionable=False)
        while self.gaming_timer > 0:
            self.gaming_timer -= 1
            await asyncio.sleep(1)
        await gaming_role.edit(mentionable=True)

    @commands.command()
    async def gaming(self, ctx, option: str=None):
        gaming_role = discord.utils.get(ctx.message.guild.roles, name="Gaming")
        if option == "reset":
            mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
            if mod_role not in ctx.message.author.roles:
                return
            else:
                time_left = str(datetime.timedelta(seconds=(self.gaming_timer)))
                await ctx.send(":video_game: The timer has been reset to zero from " + time_left)
                self.gaming_timer = 0
                gaming_role = discord.utils.get(ctx.message.guild.roles, name="Gaming")
                await gaming_role.edit(mentionable=True)
                return
        if option == "apply":
            mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
            if mod_role not in ctx.message.author.roles:
                return
            else:
                await ctx.send(":video_game: The timer has been set to an hour.")
                await self.countdown(ctx.message)
                return
        if gaming_role.mentionable:
            await ctx.send(":video_game: The `Gaming` role is pingable.")
        else:
            time_left = str(datetime.timedelta(seconds=(self.gaming_timer)))
            await ctx.send(":video_game: " + time_left + " until the `Gaming` role can be pinged.")

    @commands.command()
    async def yao(self, ctx, *, input: str):
        msg = ""
        for c in input:
            msg = msg + c.upper() + ' '
        msg = msg[:-1]
        newmsg = "***" + msg + "***"
        await ctx.send(newmsg)

    @commands.command()
    async def poll(self, ctx, *, input: str):
        tokens = input.split(",")
        question = tokens[0]
        options = tokens[1:]
        optioncount = len(options)
        if optioncount == 1:
            await ctx.send(":no_entry_sign: It's not really a poll if there's only one option.")
            return
        if optioncount > 10:
            await ctx.send(":no_entry_sign: Poll option limit is 10! Try simplifying your question.")
            return
        reactions = ['😝', '😎', '😁', '😍', '😂', '😚', '😮', '😇', '🤗', '😌']
        msg = ""
        for x, option in enumerate(options):
            msg = msg + "\n{} {}".format(reactions[x], option)
        embed = discord.Embed(title=question, description=msg, colour=0xffcc4d)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " asks,")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/446747780157931542/thinking.png")
        message = await ctx.send(embed=embed)
        for reaction in reactions[:optioncount]:
            await message.add_reaction(reaction)

    @commands.command()
    async def mily(self, ctx):
        await ctx.send("Is the best ever :heart:")

    async def on_message(self, message):
        await self.process_commands(message)

        '''GAMING PING TIMER'''
        if "<@&465699200362086410>" in message.content:
            await self.countdown(message)

        '''GAME MODERATION'''
        if message.channel.id == 475730288648126494:
            bots = self.get_channel(id=455400008246624257)
            messages = []
            async for m in message.channel.history(limit=2):
                messages.append(m)
            if message.author == messages[1].author:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you cannot double post.")
                return
            if ' ' in message.content:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you can only use a single word.")
                return
            if not message.content[-1:].isalpha():
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because your word did not end with a letter.")
                return
            last_letter = messages[1].content[-1:].lower()
            first_letter = messages[0].content[0].lower()
            if last_letter != first_letter:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because the first letter of your word did not match the last letter of the previous word.")
                return
        if message.channel.id == 475720467559481354:
            bots = self.get_channel(id=455400008246624257)
            try:
                int(message.content)
            except ValueError:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you did not post a number.")
                return
            messages = []
            async for m in message.channel.history(limit=2):
                messages.append(m)
            if message.author == messages[1].author:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you cannot double post.")
                return
            previous_number = messages[1].content
            posted_number = messages[0].content
            print(previous_number + " " + posted_number)
            if (int(previous_number) + 1) != int(posted_number):
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you did not post the next number in succession.")
        if message.channel.id == 501582077662068736:
            bots = self.get_channel(id=455400008246624257)
            oofs = ["oof", "o o f"]
            check = message.content.lower()
            if check not in oofs:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because it was not an acceptable oof. Please oof by saying 'oof' or 'o o f' (any combination of lowercase/uppercase accepted)")
                return
            messages = []
            async for m in message.channel.history(limit=2):
                messages.append(m)
            if message.author == messages[1].author:
                await message.delete()
                await bots.send(":no_entry_sign: " + message.author.mention + ", Your message was deleted in " + message.channel.mention + " because you cannot double post.")
                return

    @commands.command()
    async def help(self, ctx):
        message = """Hello! I am Egg Bot. I am a custom bot written specifically for the Lonely Nerds server!

        Prefix: **e!**

        Commands:
        `e!top`
        Displays the MEE6 server leaderboard.

        `e!addcolor color`
        Assigns a color role. Refer to #information for a list of colors to choose from.

        `e!removecolor`
        Clears your color role.

        `e!colors`
        View a list of availible color roles."""
        embed = discord.Embed(description=message)
        embed.set_footer(text="Written by Frankup")
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " needs help!")
        embed.colour = ctx.message.author.colour if hasattr(ctx.message.author, "colour") else discord.Colour.default()
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx,  *, stat: str):
        if str(ctx.message.author.id) == 183457916114698241:
            await self.change_presence(game=discord.Game(name=(stat)))

    async def on_ready(self):
        print('Logged in as '+self.user.name+' (ID:'+str(self.user.id)+') | Connected to '+str(len(self.guilds))+' servers | Connected to '+str(len(set(self.get_all_members())))+' users')
        print('--------')
        print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
        print('--------')
        print('Use this link to invite {}:'.format(self.user.name))
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(str(self.user.id)))
        print('--------')

        cogs = ['verification', 'colors', 'faq', 'leaderboard', 'infodisplay', 'teams', 'moderation']
        for cog in cogs:
            self.load_extension(cog)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
