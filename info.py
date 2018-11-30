information = [
["""We are a community server to hang out, chat, and make friends. Don't be shy! We love meeting and talking to new people. Please take a moment to read the rules and general information about the server below.

If you have any questions, feel free to ask in """ + self.get_channel("473964680004763659").mention + """!

Permanent invite link: `http://discord.gg/VnAjMgy`""", "Welcome to Lonely Nerds!", "https://cdn.discordapp.com/attachments/372188609425702915/498973052445523983/lonelynerds.png", 0xFFC961],

["""`1`: Follow the Discord TOS.
`2`: Keep your posts in the appropriate channels.
`3`: Do not DM any users with the `DMs closed` role.
`4`: Invites to other servers are forbidden and automatically deleted.
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

To view ranking information, use the """ + self.get_channel("455400008246624257").mention + """ channel to issue any of the following commands.

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

`Nitro Flexer`
Awarded to those who have Discord Nitro.

`Supporter`
Awarded to those who make a suggestion in """ + suggestions.mention + """ that gets implemented.

`Champion`
Awarded to those who win server events or contests.""", "Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498980224197722123/shield.png", 0x55ACEE],

["""To use the color role system, use the """ + self.get_channel("455400008246624257").mention + """ channel to issue any of the following commands.

`e!colors`
View the availible colors.

`e!addcolor color`
Apply a color role.

`e!removecolor`
Remove your current color role.""", "Color Roles", "https://cdn.discordapp.com/attachments/372188609425702915/498958897499865088/color-wheel.png", 0xFF0000],

["""Now that you are all caught up on what you need to know, feel free to introduce yourself in """ + self.get_channel("473551440514646026").mention + """ and then stop by """ + self.get_channel("455399951258746902").mention + """ to say hi!""", "Thanks for reading!", "https://cdn.discordapp.com/attachments/372188609425702915/498988413966352384/wave.png", 0xFFDC5D]
]

tools = [
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
Applies the `Fully Verified Nerd` role to the tagged user. If the user already has the `Verified Nerd` role, it will be removed and replaced with `Fully Verified Nerd`.

If a user has Discord Nitro, they get the `Nitro Flexer` role.

`e!nitro @user`
Applies the `Nitro Flexer` role to the tagged user.

`e!denitro @user`
Removes the `Nitro Flexer` role from the tagged user.""", "Verification", "https://cdn.discordapp.com/attachments/372188609425702915/499023938157019156/verified.png", 0x5D93FE],

["""The following commands can be issued to provide a quick response to a user who asks a frequently asked question.

`e!invite`
Posts the server's permanent invite link.

`e!verification`
Explains what the verified roles mean.

`e!generations`
Explains what the generation roles mean.""", "Frequently Asked Questions", "https://cdn.discordapp.com/attachments/372188609425702915/499024476630024193/faq.png", 0xBE1931]
]
