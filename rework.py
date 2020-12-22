import discord
import random
import time
import aiohttp
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext

bot = commands.Bot(command_prefix='4!', description='')
slash = SlashCommand(bot)

with open("resources/do-not-share", "r") as read:
    token = read.read()


@bot.event
async def on_ready():
    print('started')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="prefix '4!'"))


@bot.command(pass_context=True, description='Kicks a member from the server', category='Moderation Utilities')
async def kick(ctx, member: discord.Member, reason):
    await ctx.send("<:kick:779462980001464381> Kicking member")
    await member.kick(reason=reason)
    await ctx.send("<:successdark:783806540721291304> Kicked!")


@bot.command(pass_context=True, description='Bans a member from the server', category='Moderation Utilities')
async def ban(ctx, member: discord.Member, reason):
    await ctx.send("<:kick:779462980001464381> Banning member")
    await member.ban(reason=reason)
    await ctx.send("<:successdark:783806540721291304> Banned!")


@bot.command(description='Rolls the dice', category='Utilities')
async def roll(ctx):
    result = random.randrange(1, 6)
    await ctx.send("<:dice:779456584384380968> Rolling...")
    time.sleep(1)
    await ctx.send("<:successdark:783806540721291304> Rolled: " + str(result))


@bot.command(description='Sends a cat in the chat <3 (facts about cats included!)', category='Animals')
async def cat(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://some-random-api.ml/animal/cat") as r:
            data = await r.json()
            embed = discord.Embed(title="Here's your cat! <3", color=0xffff00)
            embed.set_author(name="Powered by some-random-api.ml", url="https://some-random-api.ml/")
            embed.set_image(url=data['image'])
            embed.set_footer(text="Fact:" + data['fact'])
            await ctx.send(embed=embed)


@bot.command(description='Sends a doggo in the chat <3 (facts about dogs included!)', category='Animals')
async def dog(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://some-random-api.ml/animal/dog") as r:
            data = await r.json()
            embed = discord.Embed(title="Doggo!!!! <3", color=0xffff00)
            embed.set_author(name="Powered by some-random-api.ml", url="https://some-random-api.ml/")
            embed.set_image(url=data['image'])
            embed.set_footer(text="Fact: " + data['fact'])
            await ctx.send(embed=embed)


@bot.command(description='You can talk to a chat bot on Discord!', category='Misc')
async def chat(ctx, message):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://some-random-api.ml/chatbot?message=" + message) as r:
            data = await r.json()
            embed = discord.Embed(title="Powered by some-random-api.ml", url="https://some-random-api.ml/",
                                  color=0x00ff00)
            embed.add_field(name="Response", value=data['response'], inline=False)
            await ctx.send(embed=embed)


@bot.command(description='Says hello', category='Utilities')
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command(description='Checks the latency between Discord and the bot')
async def ping(ctx):
    await ctx.send("Pong! `" + str(bot.latency*500) + "ms`")


@bot.command(description='Obvious thing (says what you say into the bot)')
async def say(ctx, message):
    await ctx.send(message)


@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

bot.run(token)
