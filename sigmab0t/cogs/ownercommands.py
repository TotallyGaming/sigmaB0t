import discord
from discord.ext import commands


class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} cog loaded")

        async def cog_check(self, ctx):
            return ctx.author == ctx.guild.owner

    @commands.command(
        help="Deletes a specified number of messages, or all if no number is given.",
        description="Deletes only the messages in the chat the command was sent in.",
    )
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            deleted = await ctx.channel.purge()
            await ctx.send("Deleted all messages.", delete_after=3)
        else:
            if amount <= 0:
                await ctx.send(
                    "Please specify a number greater than 0.", delete_after=3
                )
                return

            deleted = await ctx.channel.purge(limit=amount)
            await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=3)


async def setup(bot):
    await bot.add_cog(OwnerCommands(bot))
