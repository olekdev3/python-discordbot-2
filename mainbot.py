import discord
from discord.ext import commands 
from commands.moderation import moderation
from commands.leagueranking import leaguerankings
from commands.funcommands import eightball, afk

client = commands.Bot(command_prefix = '#')
command_file = open('command_log.txt','a')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    command_file.write(f'{ctx.author.name} : "ping"')
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Latency: {round(client.latency * 1000)} ms')

@client.command()
async def join(ctx):
    command_file.write(f'{ctx.author.name} : "join"')
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f'Joined {ctx.author.voice.channel}')



@client.command()
async def disconnect(ctx):
    command_file.write(f'{ctx.author.name} : "disconnect"')
    await ctx.voice_client.disconnect()



@client.command()
async def suggestion(ctx, *, suggest):
    command_file.write(f'{ctx.author.name} : "suggestion"')
    add_suggestion(suggest)
    await ctx.send('Suggestion added.')



def add_suggestion(suggestion):
    f = open("suggestions.txt", "a")
    f.write(f'\n{suggestion}')
    f.close()



@client.command()
async def show_suggestions(ctx):
    command_file.write(f'{ctx.author.name} : "show_suggestions"')
    f = open("suggestions.txt", "r")
    lines = f.readlines()
    all_suggestions = ""
    for line in lines:
        all_suggestions = f"{all_suggestions}\n{line}"
    await ctx.send(all_suggestions)


moderation(client)
leaguerankings(client)
eightball(client)
afk(client)

token_file = open('D:/token.txt','r')
token = token_file.readline()
token_file.close()

client.run(token)