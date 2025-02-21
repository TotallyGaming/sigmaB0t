import discord
from discord.ext import commands


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


async def setup(bot):
    await bot.add_cog(PublicCommands(bot))
