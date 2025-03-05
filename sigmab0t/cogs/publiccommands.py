import discord
from discord.ext import commands

imagefileext = ".png"
memedir = "sigmab0t/images/memes"

def GetMemeAmount():
    import os
    imagecount = 0
    for filename in os.listdir(memedir):
        if filename.endswith(imagefileext):
            imagecount += 1

    return imagecount

class PublicCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} cog loaded")

    @commands.command(
        help="Gets the bots current latency.",
        description="Latency is the time between the message being sent and the message being received.",
    )
    async def ping(self, ctx):
        await ctx.send(f"Pong! `{round(self.bot.latency*1000)}` ms.")


    @commands.command(
        help="Takes the average of the given numbers.",
        description="The average is the sum of the numbers divided by the amount of numbers.",
    )
    async def average(self, ctx, *numbers: float):
        if not numbers:
            await ctx.send("Please provide numbers to average.")
            return

        average = sum(numbers) / len(numbers)
        average = round(average, 4)
        await ctx.send(f"The average is **{average}**")

    @commands.command(
        help="Generates a random programming meme.",
        description=f"Currently there are `{GetMemeAmount()}` possible memes."
    )
    async def randommeme(self, ctx):
        import random
        import os
        filename = ""

        while not filename.endswith(imagefileext):
            filename = random.choice(os.listdir(memedir))

        with open(f"sigmab0t/images/memes/{filename}", "rb") as f:
            memefile = discord.File(f)

        await ctx.send(file=memefile)

    @commands.command(help="Tips on how to stop pollution", description="You can do these to help clean the environment.")
    async def stoppollution(self, ctx):
        tips = ["Plant trees aroung bare areas.", "Clean the trash on the beach.", "Organize an event/fundraiser to help the environment.", "Recycle plastic, grass and paper."]
        message = "Here are some things you can do in order to stop pollution and global warming.\nEven if these are small things they can still help.\n\n"

        for tip in tips:
            message += f"* {tip}\n"

        await ctx.send(message)
        
        @commands.command(help="A game where you do various action and get points.", description="You can:")
        async def game(self, ctx, action: str, *specs):
            user = ctx.author.name
            points =
            if action == "score":
                
            elif action == "duel":
                pass
            elif action == "opencrate":
                pass

async def setup(bot):
    await bot.add_cog(PublicCommands(bot))
