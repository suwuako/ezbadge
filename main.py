import discord

from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

token = input("Enter your token here:")

@tree.command(name = "claim", description = "badge")
async def claim(interaction):
    await interaction.response.send_message("claimed! You might have to wait ~24 Hours before the avaliability of the badge is accessible here (https://discord.com/developers/active-developer)")

@client.event
async def on_ready():
    await tree.sync()
    print("Done! now run /claim in chat and wait 24 hours to get your badge.")
client.run(token)
