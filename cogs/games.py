import discord
from discord.ext import commands
from random import randint

computerChoices = ["rock", "paper", "scissors"]


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events

    # Commands
    
    # A simple Rock, Paper & Scissors game
    @commands.command()
    async def rps(self, ctx, choice):
        computerChoice = computerChoices[randint(0, 2)]

        if choice not in computerChoices:
            await ctx.channel.send("`Usage: .rps <rock | paper | scissors>`")
            return

        userChoice = choice.lower()

        embed = discord.Embed(title="Rock, Paper & Scissors", color=0x8E6CDE)
        embed.add_field(name="Your Choice", value=userChoice)
        embed.add_field(name="Bot's Choice", value=computerChoice)

        result = ""
        if userChoice == computerChoice:
            result = "It's a draw! 🤔"

        elif userChoice == "rock":
            if computerChoice == "paper":
                result = "Bot wins! 😉"
            else:
                result = "You win! 😮"

        elif userChoice == "paper":
            if computerChoice == "scissors":
                result = "Bot wins! 😉"
            else:
                result = "You win! 😮"

        elif userChoice == "scissors":
            if computerChoice == "rock":
                result = "Bot wins! 😉"
            else:
                result = "You win! 😮"

        embed.add_field(name="Match Result", value=result)
        await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Games(client))