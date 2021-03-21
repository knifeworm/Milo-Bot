import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title = "Ban", color = 0xFF0000)
        embed.add_field(name = "Member Banned", value = f"{member}", inline = False)
        embed.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
        embed.add_field(name = "Reason", value = f'{reason}', inline = False)
        await ctx.send(embed = embed)
        mem = discord.Embed(title = "Ban", color = 0xFF0000)
        mem.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
        mem.add_field(name = "Reason", value = f"{reason}", inline = False)
        mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline = False)
        await member.send(embed = mem)
        await member.ban(reason = reason)

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title = "Kick", color = 0xFF0000)
        embed.add_field(name = "Member Kicked", value = f"{member}", inline = False)
        embed.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
        embed.add_field(name = "Reason", value = f"{reason}", inline = False)
        await ctx.send(embed = embed)
        mem = discord.Embed(title = "Kick", color = 0xFF0000)
        mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        mem.add_field(name = "Reason", value = f'{reason}', inline=False)
        mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
        await member.send(embed = mem)
        await member.kick(reason = reason)

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name = "Muted")

        if role is None:

            await ctx.send("Woof woof - Creating role!")
            create_role = await ctx.guild.create_role(name = "Muted", reason = "Woof woof - For the Milo-bot mute command!")
            await ctx.send("Woof woof - Successfully created role!")
            await ctx.send("Woof woof - Setting permissions for channels!")

            for channel in ctx.guild.channels:
                role_channel = discord.utils.get(ctx.guild.roles, name = "Muted")
                await channel.set_permissions(role_channel, speak = False, send_messages = False, read_message_history = True, read_messages = True)
                await ctx.send("Woof woof - Successfully set permissions!")
                await ctx.send("Woof woof - Muteing user!")
                if role in member.roles:
                    await ctx.send("Woof woof - This member is already muted!")
                else:
                    embed = discord.Embed(title = "Mute", color = 0xFF0000)
                    embed.add_field(name = "Member Muted", value = f"{member}", inline = False)
                    embed.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
                    embed.add_field(name = "Reason", value = f"{reason}", inline = False)
                    await ctx.send(embed = embed)
                    mem = discord.Embed(title = "Mute", color = 0xFF0000)
                    mem.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
                    mem.add_field(name = "Reason", value = f"{reason}", inline = False)
                    mem.add_field(name = "Server", value = f"{ctx.guild.name}", inline = False)
                    muted = discord.utils.get(ctx.guild.roles, name = "Muted")
                    await member.send(embed = mem)
                    await member.add_roles(muted)

        else:
            if role in member.roles:
                await ctx.send("Woof woof - This member is already muted!")
            else:
                embed = discord.Embed(title = "Mute", color = 0xFF0000)
                embed.add_field(name = "Member Muted", value = f"{member}", inline = False)
                embed.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
                embed.add_field(name = "Reason", value = f"{reason}", inline = False)
                await ctx.send(embed = embed)
                mem = discord.Embed(title = "Mute", color = 0xFF0000)
                mem.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
                mem.add_field(name = "Reason", value = f"{reason}", inline = False)
                mem.add_field(name = "Server", value = f"{ctx.guild.name}", inline = False)
                muted = discord.utils.get(ctx.guild.roles, name = "Muted")
                await member.send(embed = mem)
                await member.add_roles(muted)
    
    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name = "Muted")
        if role in member.roles:
            embed = discord.Embed(title = "Unmute", color = 0xFF0000)
            embed.add_field(name = "Member Unmuted", value = f"{member}", inline = False)
            embed.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
            await ctx.send(embed = embed)
            mem = discord.Embed(title = "Unmute", color = 0xFF0000)
            mem.add_field(name = "Staff Member", value = f"{ctx.author}", inline = False)
            mem.add_field(name = "Server", value = f"{ctx.guild.name}", inline = False)
            await member.send(embed = mem)
            await member.remove_roles(role)
        else:
            await ctx.send(f"Woof woof - {member} is not muted!")
            
def setup(bot):
    bot.add_cog(moderation(bot))