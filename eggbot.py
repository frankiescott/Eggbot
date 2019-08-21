import discord
import asyncio
import platform
import requests
import time
import datetime
import random
from keys import API_KEY
from discord.ext import commands
import io

bot = commands.Bot(command_prefix='e!')
bot.remove_command("help")
startup_extensions = ['verification', 'colors', 'faq', 'leaderboard', 'infodisplay', 'moderation', 'votecount', 'roledisplay', 'customroles']

#async def countdown(message):
#    self.gaming_timer = 3600
#    gaming_role = discord.utils.get(message.guild.roles, name="Gaming")
#    await gaming_role.edit(mentionable=False)
#    while self.gaming_timer > 0:
#        self.gaming_timer -= 1
#        await asyncio.sleep(1)
#    await gaming_role.edit(mentionable=True)

#@commands.command()
#async def gaming(self, ctx, option: str=None):
#    gaming_role = discord.utils.get(ctx.message.guild.roles, name="Gaming")
#    if option == "reset":
#        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
#        if mod_role not in ctx.message.author.roles:
#            return
#        else:
#            time_left = str(datetime.timedelta(seconds=(self.gaming_timer)))
#            await ctx.send(":video_game: The timer has been reset to zero from " + time_left)
#            self.gaming_timer = 0
#            gaming_role = discord.utils.get(ctx.message.guild.roles, name="Gaming")
#            await gaming_role.edit(mentionable=True)
#            return
#    if option == "apply":
#        mod_role = discord.utils.get(ctx.message.guild.roles, name="Mod")
#        if mod_role not in ctx.message.author.roles:
#            return
#        else:
#            await ctx.send(":video_game: The timer has been set to an hour.")
#            await self.countdown(ctx.message)
#            return
#    if gaming_role.mentionable:
#        await ctx.send(":video_game: The `Gaming` role is pingable.")
#    else:
#        time_left = str(datetime.timedelta(seconds=(self.gaming_timer)))
#        await ctx.send(":video_game: " + time_left + " until the `Gaming` role can be pinged.")

@bot.command()
async def yao(ctx, *, input: str):
    msg = ""
    for c in input:
        msg = msg + c.upper() + ' '
    msg = msg[:-1]
    newmsg = "***" + msg + "***"
    await ctx.send(newmsg)

@bot.command()
async def poll(ctx, *, input: str):
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

@bot.command()
async def publishpoll(ctx, *, input: str):
    mod = discord.utils.get(ctx.guild.roles, name="Mod")
    family = discord.utils.get(ctx.guild.roles, name="Family")
    loyalfamily = discord.utils.get(ctx.guild.roles, name="Loyal Family")
    if mod in ctx.author.roles or family in ctx.author.roles or loyalfamily in ctx.author.roles:
        tokens = input.split(",")
        question = tokens[0]
        options = tokens[1:]
        optioncount = len(options)
        if optioncount == 1:
            await ctx.send(":no_entry_sign: Please provide at least two options for your poll.")
            return
        if optioncount > 10:
            await ctx.send(":no_entry_sign: The poll option limit is ten. Please remove " + optioncount - 10 + " options.")
            return
        reactions = ['😝', '😎', '😁', '😍', '😂', '😚', '😮', '😇', '🤗', '😌']
        msg = ""
        for x, option in enumerate(options):
            msg = msg + "\n{} {}".format(reactions[x], option)
        embed = discord.Embed(title=question, description=msg, colour=0xffcc4d)
        embed.set_author(icon_url=ctx.message.author.avatar_url, name=ctx.message.author.display_name + " asks,")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/372188609425702915/446747780157931542/thinking.png")
        message = await bot.get_channel(558726347086626826).send(embed=embed)
        for reaction in reactions[:optioncount]:
            await message.add_reaction(reaction)
        await bot.get_channel(455399951258746902).send(":bar_chart: " + ctx.message.author.display_name + " has published a new poll in " + bot.get_channel(558726347086626826).mention + "!")
    else:
        await ctx.send(":no_entry_sign: You must be ranked Family, Loyal Family, or Mod to publish a poll.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    #'''GAMING PING TIMER'''
    #if "<@&465699200362086410>" in message.content:
    #    await bot.countdown(message)

    '''CONFESSIONS'''
    if message.channel.id == 508109297385734144:
        if message.author.bot == True:
            return
        if message.content.startswith("~"):
            return
        else:
            confessions = bot.get_channel(id=508109297385734144)
            color = random.randint(000000, 16777215)
            embed = discord.Embed(description="A user wrote,\n\n*" + message.content + "*\n ", colour=int(color), title="Submit your own to https://goo.gl/forms/CmugvdeHEU9rpuE52")
            embed.set_author(icon_url="https://cdn.discordapp.com/attachments/372188609425702915/530714183323615243/1f4e5.png", name="Confession Box")
            embed.set_footer(icon_url=message.author.avatar_url, text="Confession published by " + message.author.display_name + ". All confessions are anonymous.")
            await confessions.send(embed=embed)
            await message.delete()

    '''GAME MODERATION'''
    if message.channel.id == 475730288648126494:
        bots = bot.get_channel(id=455400008246624257)
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
        bots = bot.get_channel(id=455400008246624257)
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
        bots = bot.get_channel(id=455400008246624257)
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

@bot.command()
async def help(ctx):
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

@bot.command()
async def status(ctx,  *, stat: str):
    if ctx.message.author.id == 183457916114698241:
        game = discord.Game(stat)
        await bot.change_presence(activity=game)
        await ctx.send(":white_check_mark: Status set to '" + stat + "'")

@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+str(bot.user.id)+') | Connected to '+str(len(bot.guilds))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(str(bot.user.id)))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(API_KEY)
