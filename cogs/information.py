import discord

from discord.ext import commands

from discord import app_commands

from base import OMOBOT


class Information(commands.Cog):
    def __init__(self, bot: OMOBOT):
        self.bot = bot

    @app_commands.command(name="info", description="Shows information about the bot")
    async def information_interaction(self, inter: discord.Interaction):
        embed = discord.Embed(
            title="Project OMOBOT",
            url="https://discord.gg/47vGg2zwPu",
            description="Coming soon...",
            color=discord.Color.from_rgb(255, 255, 255)
        )

        embed.set_thumbnail(
            url=self.bot.user.display_avatar.url
        )

        embed.add_field(name="Lead Developer", value="LetsChill#2889", inline=True)
        embed.add_field(name="Library", value="Discord.py", inline=True)
        embed.add_field(name="Date of creation", value="23rd of May, 2023", inline=True)
        embed.add_field(name="Number of Shards", value=len(self.bot.shards), inline=False)
        embed.add_field(name="Number of Servers", value=len(self.bot.guilds), inline=True)

        await inter.response.send_message(embed=embed)


async def setup(bot: OMOBOT):
    await bot.add_cog(Information(bot))
