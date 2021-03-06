import discord
import inspect
from discord.ext import commands

class Secret(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """ - Command which Loads a Module."""
        try:
            self.client.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully loaded the cog: `{cog}`')


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """ - Command which Unloads a Module."""
        try:
            self.client.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully unloaded the cog: `{cog}`')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """ - Command which Reloads a Module."""
        try:
            self.client.reload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'{type(e).__name__} - {e}')
        else:
            await ctx.send(f'You have successfully reloaded the cog: `{cog}`')
    
    
    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, command):
        """ - Evaluates code."""
        res = eval(command)
        if inspect.isawaitable(res):
            await ctx.send(await res)
        else:
            await ctx.send(f'```py\n{res}```')




    @load.error
    async def load_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="Please provide a cog to load.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)
    @unload.error
    async def unload_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="Please provide a cog to unload.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)
    @reload.error
    async def reload_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="Please provide a cog to reload.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)
    @eval.error
    async def eval_error(self, ctx, error):
        embed = discord.Embed(color=0xafdfeb, description="Please provide some code to evaluate")
        embed2 = discord.Embed(color=0xafdfeb, description=f'{error}')
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(embed = embed)
        if isinstance(error, commands.CommandInvokeError):
            return await ctx.send(embed = embed2)


def setup(client):
    client.add_cog(Secret(client))