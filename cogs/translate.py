from aiogoogletrans import Translator
from discord import Color, Embed
from discord.ext.commands import Cog, Context, command

class TranslateCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def translate(self,ctx: Context,source_language: str = "en",destination_language: str = "en",*,sentence: str = "Hello World",) -> None:
        """Translate a sentence."""
        translator = Translator()
        translation = await translator.translate(
            sentence, dest=destination_language, src=source_language
        )
        embed = Embed(
            title="Translation",
            description=f"Sentence : **{sentence}**\n\nTranslation : **{translation.text}**\n\nType : **{translation.src} > {translation.dest}**",
            color=Color.dark_purple(),
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(TranslateCog(bot))