import discord
from discord.ext import commands

clips = {}

class Clips(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events


    # Commands
    
    # adds information to the clipboard
    @commands.command()
    async def addclip(self, ctx, name, link):
        condition = False

        if not name or not link:
            await ctx.channel.send("Usage: .addclip <name> <link>")

        for title, value in clips.items():
            if value == link or title == name:
                condition = True
                await ctx.channel.send(f'The name or link already exists.')

        if not condition:
            clips[name.lower()] = link.lower()
            await ctx.channel.send(f'{name} has been added to the list of saved clips.')

    # removes information form the clipboard
    @commands.command()
    async def rmclip(self, ctx, name):
        if not name:
            await ctx.channel.send("Usage: .rmclip <name>")
        else:
            if name in clips:
                clips.pop(name.lower())
                await ctx.channel.send(f'{name} has been removed.')
            else:
                await ctx.channel.send(f'{name} was not found.')

    # Displays clipboard contents
    @commands.command()
    async def listclips(self, ctx):

        if len(clips) > 0:
            embed = discord.Embed(title="Clips", color=0xC712EB)
            for clipName, link in clips.items():
                embed.add_field(name=clipName, value=link)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(f'There are no clips to display.')

def setup(client):
    client.add_cog(Clips(client))