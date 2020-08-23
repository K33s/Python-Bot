import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events


    # Commands

    # Sends a message anonymously to a selected member of the server
    @commands.command()
    async def anonmsg (self, ctx, username, msg):
        
        await ctx.message.delete()

        memberList = ctx.guild.members
        splitId = username.split('#')
        name = splitId[0]
        desc = splitId[1]
        condition = False

        for member in memberList:
            if member.name == name and member.discriminator == desc:
                condition = True
                await member.send(f'**You have received an anonymous message.** Click to reveal.\n||{msg}||')
                await ctx.author.send(f"Message has been successfully sent to {username}.")

        if not condition:
            await ctx.author.send("Message not sent. User was not found. `Usage: .anonmsg <username> <message>`")

    # Sends a message to the bot creator
    @commands.command()
    async def msgcreator (self, ctx, msg):
        userList = self.client.users

		# Replace 12345 with the user id
        for person in userList:
            if person.id == 12345:
                await person.send(f'Message sent from **{ctx.author.name}#{ctx.author.discriminator}**, id = **{ctx.author.id}**, from guild  **{ctx.guild.name}** [{ctx.guild.description}, {ctx.guild.id}, {ctx.guild.region}, {ctx.guild.max_members}] \n\n {msg}')
            
def setup(client):
    client.add_cog(Messages(client))