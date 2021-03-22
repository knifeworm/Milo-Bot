import discord
from discord.ext import commands

class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        channel_count = len([x for x in ctx.guild.channels if type(x) == discord.channel.TextChannel])
        voice_channels = len([c for c in ctx.guild.channels if type(c) == discord.channel.VoiceChannel])
        cat = len([cc for cc in ctx.guild.categories if type(cc) == discord.channel.CategoryChannel])
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)
        embed = discord.Embed(title="ServerInfo")
        embed.add_field(name="Name", value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name="Id", value=f"{ctx.guild.id}", inline=False)
        embed.add_field(name="Users", value=f"{ctx.guild.member_count}", inline=False)
        embed.add_field(name="Owner :crown:", value=f"{ctx.guild.owner}", inline=False)
        embed.add_field(name="Region", value=f"{ctx.guild.region}", inline=False)
        embed.add_field(name="Role count", value=str(role_count), inline=False)
        embed.add_field(name="Emoji Count", value=str(emoji_count), inline=False)
        embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Text channels", value=str(channel_count), inline=False)  
        embed.add_field(name="Voice Channels", value=str(voice_channels), inline=False)
        embed.add_field(name="Categories", value=str(cat), inline=False)
        await ctx.send(embed = embed)

    @commands.command()
    async def userinfo(self, ctx, member : discord.Member=None):
        if member is None:
            embed = discord.Embed(title="UserInfo")
            embed.add_field(name="Name", value=f"{ctx.author.name}", inline=False)
            embed.add_field(name="Id", value=f"{ctx.author.id}", inline=False)
            embed.add_field(name="Hashtag", value=f"{ctx.author.discriminator}", inline=False)
            embed.add_field(name="Nickname", value=f"{ctx.author.nick}", inline=False)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title="UserInfo")
            embed.add_field(name="Name", value=f"{member.name}", inline=False)
            embed.add_field(name="Id", value=f"{member.id}", inline=False)
            embed.add_field(name="Hashtag", value=f"{member.discriminator}", inline=False)
            embed.add_field(name="Nickname", value=f"{member.nick}", inline=False)
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(information(bot))