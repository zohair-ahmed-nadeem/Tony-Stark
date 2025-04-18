import discord
from discord.ext import commands
import config
import asyncio
import traceback

owner_id = 1103690895997538435

footer = "Developed BY ZAN ✨"
prefix = ">"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print("-----------------------------------")
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="with Discord"))
    print("Connected to the following servers:")
    for guild in bot.guilds:
        print(f"- {guild.name}")
    await bot.tree.sync()
    print("App commands synced!")
    print("-----------------------------------")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        await ctx.send(f"An error occurred: {error}")
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user in message.mentions:
        try:
            embed = discord.Embed(title="Bot Info", color=discord.Color.blue())
            embed.add_field(name="Prefix", value=f"My prefix is `{bot.command_prefix}`", inline=False)
            embed.add_field(name="Help", value=f"Use `/help` or `{bot.command_prefix}help` for a list of commands", inline=False)
            embed.add_field(name="Report", value=f"Use `/report` or `{bot.command_prefix}report` for reporting us", inline=False)
            embed.set_footer(text=footer)
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Invite Me", url="https://discord.com/oauth2/authorize?client_id=1184035274037137478&permissions=8&integration_type=0&scope=bot"))
            view.add_item(discord.ui.Button(label="Support Server", url="https://discord.gg/GXuZVF4573"))
            await message.channel.send(embed=embed, view=view)
        except Exception as e:
            print(f"Error in on_message: {e}")
    await bot.process_commands(message)

# bot.remove_command('help')
@bot.command(name='h')
async def help_command(ctx):
    embed = discord.Embed(
        title="SHAPATER#0017",
        description="Hey! I am shapater!\nThanks for choosing me!\nFacing any problem? Send a report using `/report`.",
        color=discord.Color.blue()
    )
    embed.add_field(name="commands",value="")    
    embed.add_field(
        name="Links",
        value=f"[Invite Me]({config.inv}) | [Support Server]({config.srv})",
        inline=False
    )
    embed.set_footer(text=config.footer)
    
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Invite", style=discord.ButtonStyle.success, url=config.inv))
    view.add_item(discord.ui.Button(label="Website", style=discord.ButtonStyle.secondary, url=config.srv))

    await ctx.send(embed=embed, view=view)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    if extension is None:
        await ctx.send("Please provide an extension to reload.\n`reload <extension>`")
        return 
    try:
        await bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded {extension} extension!")
    except Exception as e:
        await ctx.send(f"Failed to reload {extension}: {e}")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    if extension is None:
        await ctx.send("Please provide an extension to reload.\n`load <extension>`")
        return 
    try:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension} extension!")
    except Exception as e:
        await ctx.send(f"Failed to load {extension}: {e}")
        
async def load_extensions():
    # extensions = ['ban', 'kick', 'mute', 'imp', 'on_msg', 'prefix', 'prvt', 'auto', 'channel', 'antispam','wiki', 'ai', 'yt', 'guild_info','trans']
    extensions = ['on_msg', 'soundboard']
    for ext in extensions:
        try:
            await bot.load_extension(f'cogs.{ext}')
            print(f"Loaded extension {ext}")
        except Exception as e:
            print(f"Failed to load extension {ext}. Error: {e}")
            traceback.print_exc()

async def main():
    await load_extensions()
    await bot.start(config.test_sec)

asyncio.run(main())