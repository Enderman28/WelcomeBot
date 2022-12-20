import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def greet(ctx):
    await ctx.send('Welcome! Before we proceed, I need to confirm your identity. Can you please provide your full name?')
    def check(message):
        return message.author == ctx.message.author
    name = await client.wait_for('message', check=check)
    await ctx.send(f'Thank you, {name.content}. Do you have a valid ID?')
    response = await client.wait_for('message', check=check)
    if response.content.lower() == 'yes':
        role = get_role(ctx.guild)
        if role is not None:
            await ctx.message.author.add_roles(role)
            await ctx.send(f'Welcome, {name.content}! You have been added to the role.')
        else:
            await ctx.send('Sorry, I could not find the role. Please contact an administrator for assistance.')
    else:
        await ctx.send('Sorry, you cannot proceed without a valid ID. Please contact an administrator for assistance.')

def get_role(guild):
    for role in guild.roles:
        if role.name == 'member':
            return role
    return None

client.run('MTA1NDc2MDQ2MDAwOTg4MTY1MQ.Ghcspb.FSBxTFPnK7crqOh_oD8npcz_0C-FkuagJTrSSc')
