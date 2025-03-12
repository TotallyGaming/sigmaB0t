import discord
from discord.ext import commands
import os
import asyncio

print("Starting...")

intents = discord.Intents.default()
intents.message_content = True


class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        string = (
            "Here are all the commands and what they do:\nDon't forget to use"
            f" `{bot.command_prefix}` at the start of each command.\n\n"
        )
        for cog in mapping:
            for command in mapping[cog]:
                string += f"`{command.name}` -  {command.help}\n"
        await self.get_destination().send(string)

    async def send_cog_help(self, cog):
        await self.get_destination().send(
            f"{cog.qualified_name}: {[command.name for command in cog.get_commands()]}"
        )

    async def send_group_help(self, group):
        await self.get_destination().send(
            f"{group.name}: {[command.name for command in group.commands]}"
        )

    async def send_command_help(self, command):
        extdesc = command.description or "-extended description not found-"
        await self.get_destination().send(f"`{command.name}:` {command.help} {extdesc}")


bot = commands.Bot(
    command_prefix="!", intents=intents, help_command=CustomHelpCommand()
)


@bot.event
async def on_ready():
    print("Logged in as " f"{bot.user}")


async def load_cogs():
    for filename in os.listdir("sigmab0t/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load_cogs()
    await bot.start(
        "bot token"
    )


asyncio.run(main())
