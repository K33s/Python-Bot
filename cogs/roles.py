import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events


    # Commands
    
    # Adds the requested role to every member in a server
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def addrole(self, ctx, reqrole):
        members = ctx.guild.members
        roles = ctx.guild.roles
        role = ''
        for r in roles:
            if r.name.lower() == reqrole.lower():
                role = r

        if role == '':
            await ctx.channel.send("Could not find the requested role.")
            return

        for member in members:
            if member.bot != True:
                await member.add_roles(role)
        await ctx.channel.send("Done")

        
    # removes the requested role from every member in a server
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def rmrole(self, ctx, reqrole):
        members = ctx.guild.members
        roles = ctx.guild.roles

        role = ''
        for r in roles:
            if r.name.lower() == reqrole.lower():
                role = r

        if role == '':
            await ctx.channel.send("Could not find the requested role.")
            return

        for member in members:
            await member.remove_roles(role)
        await ctx.channel.send("Done")


def setup(client):
    client.add_cog(Roles(client))