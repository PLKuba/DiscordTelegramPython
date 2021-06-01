import discord

client=discord.Client()

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong!")


client.run('NzcwNTYxNzM0NzQ1MzkxMTM0.X5fXiQ.sMfVteJo-ABfiEctdP7C3e3jWR4')