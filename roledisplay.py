import discord
import asyncio
from discord.ext import commands

class Roledisplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def postembed(self, ctx, content):
        for x in range(0, len(content)):
            embed = discord.Embed(description=content[x][0], colour=content[x][3])
            embed.set_author(name=content[x][1])
            embed.set_thumbnail(url=content[x][2])
            await ctx.send(embed=embed)

    @commands.command()
    async def personalroles(self, ctx):
        if ctx.message.author.id == 183457916114698241:
            content = [

["""Welcome to the self-assignable roles channel!

We have a variety of roles among different categories to help the community here learn about you. These roles are optional. Members are not required to apply self-assignable roles in order to participate in the server. 

React with the corresponding emoji for the role you want in each category.""", "Self-assignable Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498980224197722123/shield.png", 0x55ACEE],

["""Are you a guy, or a lady? We are also accepting to anyone who identifies as gender neutral.

:princess: Lady
:cowboy: Guy
:slight_smile: Gender Neutral""", "Gender", "https://cdn.discordapp.com/attachments/372188609425702915/579887988792754187/gender.png", 0xff7bac],

["""How old are you? Lonely Nerds is open to Discord members of all ages 13 and older.

:one: 13 - 14
:two: 15 - 17
:three: 18 - 20
:four: 21 - 23
:five: 24 - 26
:six: 27 - 29
:seven: 30+""", "Age", "https://cdn.discordapp.com/attachments/372188609425702915/517893082474348544/10812-birthday-cake.png", 0xffac33],

["""Where are you from? We have members from all different parts of the world!

:regional_indicator_n: North America
:regional_indicator_s: South America
:regional_indicator_e: Europe
:regional_indicator_a: Asia
:regional_indicator_f: Africa
:regional_indicator_o: Oceania""", "Location", "https://cdn.discordapp.com/attachments/372188609425702915/579888756388134912/world-emoji-by-twitter.png", 0x88c9f9],

["""Do you mind if people message you privately? We want to ensure you feel comfortable with your interactions with the community.

:white_check_mark: DMs open
:no_entry: DMs closed
:warning: Ask to DM""", "Privacy", "https://cdn.discordapp.com/attachments/372188609425702915/581203393578795048/11065-lock.png", 0xffac33],

["""Select your Zodiac sign which can be determined by your date of birth.

:aries: Aries: March 21 - April 19
:taurus: Taurus: April 20 - May 20
:gemini: Gemini: May 21 - June 20
:cancer: Cancer: June 21 - July 22
:leo: Leo: July 23 - August 22
:virgo: Virgo: August 23 - September 22
:libra: Libra: September 23 - October 22
:scorpius: Scorpio: October 23 - November 21
:sagittarius: Sagittarius: November 22 - December 21
:capricorn: Capricorn: December 22 - January 19
:aquarius: Aquarius: January 20 - February 18
:pisces: Pisces: February 19 - March 20""", "Zodiac Sign", "https://cdn.discordapp.com/attachments/372188609425702915/581204757902000130/42BStar2BHoroscope2BWheel2B-2B2.png", 0x9266cc],

["""Let us know what kind of hobbies you are into! Some roles are mentionable.

:video_game: Gamer
Mentionable once per hour for use in the gaming channel to find people to play games with

:camera: Photographer
Mentionable for photgraphy contests

:paintbrush: Artist
Mentionable for art contests

:books: Bookworm
:musical_note: Musician
:star: Content Creator""", "Hobbies", "https://cdn.discordapp.com/attachments/372188609425702915/580084619685134350/transparent-twitter-heart-emoji-3.png", 0xe75a70],

["""The following roles enable server meta functions.

:busts_in_silhouette: Helper
Mentionable for users who are looking for help and/or advice in the venting channels

:microphone2: DJ
Allows for control over Rythm bot in voice channels""", "Server Meta", "https://cdn.discordapp.com/attachments/372188609425702915/498973052445523983/lonelynerds.png", 0xFFC961]
]
            await self.postembed(ctx, content)
            await ctx.message.delete()

    @commands.command()
    async def alignment(self, ctx, index: int=-1):
        if ctx.message.author.id == 183457916114698241:
            content = [
["""Choose your side in the comic book rivalry: Do you prefer Marvel comics, or DC comics?

:heart: Marvel
:blue_heart: DC""", "Comic Book Alignment", "https://cdn.discordapp.com/attachments/372188609425702915/580115262724899038/lightning-emoji-by-twitter.png", 0xFFAC33],

["""If you were a student at Hogwarts, which house would you want to be in?

:heart: Gryffindor
:yellow_heart: Hufflepuff
:green_heart: Slytherin
:blue_heart: Ravenclaw""", "Harry Potter House Alignment", "https://cdn.discordapp.com/attachments/372188609425702915/580116991784779937/harry-potter-sorting-hat-clipart-clipartxtras-clipart-pKP8GS.png", 0x906641],

["""The Battle for Azeroth is underway, choose your side: Horde, or Alliance?

:heart: For the Horde!
:blue_heart: For the Alliance!""", "Faction Alignment", "https://cdn.discordapp.com/attachments/372188609425702915/511697788954869760/2694.png", 0xccd6dd],

["""You have been granted an elemental power, which one will you choose?

:cloud: Air
:ocean: Water
:fire: Fire
:leaves: Earth""", "Elemental Alignment", "https://cdn.discordapp.com/attachments/372188609425702915/580184832865468436/about-4-elements-plumbing-your-local-reliable-trusted-plumber-4-elements-png-600_600.png", 0xFFFFFF],

["""Professor Oak has offered to provide you with your first Pokémon! Who will you choose?

:fire: Charmander
:ocean: Squirtle
:leaves: Bulbasaur""", "Pokémon Alignment", "https://cdn.discordapp.com/attachments/372188609425702915/580462472087994399/pokeball_PNG13.png", 0xe54036],

["""How would you categorize your moral and ethical perspective based on the following alignment chart?

:one: Lawful Good    
:two: Neutral Good      
:three: Chaotic Good
:four: Lawful Neutral   
:five: True Neutral     
:six: Chaotic Neutral
:seven: Lawful Evil     
:eight: Neutral Evil    
:nine: Chaotic Evil""", "Dungeons & Dragons Alignment", "https://cdn.discordapp.com/attachments/594209715177914398/610121701786779669/2620.png", 0xccd6dd]
]
            if index >= 0:
                content = [content[index]]
                await self.postembed(ctx, content)
                await ctx.message.delete()
            else:
                await self.postembed(ctx, content)
                await ctx.message.delete()

def setup(bot):
  bot.add_cog(Roledisplay(bot))
