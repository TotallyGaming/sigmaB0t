import discord
from discord.ext import commands
import os
import random

discord.utils.setup_logging()

imagefileext = ".png"
memedir = "sigmab0t/images/memes"

def getmemeamount():
    return len([f for f in os.listdir(memedir) if f.endswith(imagefileext)])


class PublicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{self.__class__.__name__} cog loaded")

    @commands.command(
        help="Gets the bot's current latency.",
        description="Latency is the time between the message being sent and received.",
    )
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.bot.latency * 1000)}` ms.")

    @commands.command(
        help="Takes the average of the given numbers.",
        description="The average is the sum of the numbers divided by the amount of numbers.",
    )
    async def average(self, ctx, *numbers: float):
        if not numbers:
            await ctx.send("Please provide numbers to average.")
            return
        avg = round(sum(numbers) / len(numbers), 4)
        await ctx.send(f"The average is **{avg}**")

    @commands.command(
        help="Generates a random programming meme.",
        description=f"Currently there are **{getmemeamount()}** possible memes.",
    )
    async def randommeme(self, ctx):
        memes = [f for f in os.listdir(memedir) if f.endswith(imagefileext)]
        if not memes:
            await ctx.send("No memes found!")
            return
        filename = random.choice(memes)
        with open(os.path.join(memedir, filename), "rb") as f:
            memefile = discord.File(f)
        await ctx.send(file=memefile)

    @commands.command(
        help="Tips on how to stop pollution",
        description="You can do these to help clean the environment.",
    )
    async def stoppollution(self, ctx):
        tips = [
            "Plant trees around bare areas.",
            "Clean the trash on the beach.",
            "Organize an event/fundraiser to help the environment.",
            "Recycle plastic, glass, and paper.",
        ]
        message = (
            "Here are some things you can do to stop pollution and global warming.\n\n"
        )
        message += "\n".join(f"* {tip}" for tip in tips)
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(PublicCommands(bot))
