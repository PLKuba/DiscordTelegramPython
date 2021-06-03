import discord
from testClasses import info

client=discord.Client()

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
    text=message.content
    text2=callALL(text)
    try:
        channel = client.get_channel(831265671345602560)
        await channel.send(text2)
    except:
        print("ERROR")



# Hi, is there a way I could specify the channel I want to send a message to by an ID or smth?
#
# I want the text2 to be sent to the specified channel.





def callALL(message):
    newObject = info(message)
    condition=newObject.checkMessage()
    if condition:
        tradeType=newObject.findTradeType()
        # print(tradeType)
        tradeSymbol=newObject.findSymbol()
        # print(tradeSymbol)
        tradeEntry=newObject.findEntry()
        # print(tradeEntry)
        tradeTPs=newObject.findTPs()
        # print(tradeTPs)
        tradeSL=newObject.findSL()
        # print(tradeSL)

        trade=f"""{tradeType} #{tradeSymbol}
        
Entry range:{tradeEntry}

Targets:
{tradeTPs[0]}
{tradeTPs[1]}
{tradeTPs[2]}
{tradeTPs[3]}

SL: {tradeSL}

⚠️NOT FINANCIAL ADVICE"""

        return trade
#ODQ4OTc0ODI2NTM3MzUzMjc3.YLUbaw.7LqUMngVyx19LyfUiTYOcdqZkNI - processmessages
# ODQ4OTUyMTA4MTA3Njk0MTYy.YLUGQw.jKN7P1a6NMVwQuw1DW1Mc5-03DE - discordTelegram
# NzcwNTYxNzM0NzQ1MzkxMTM0.X5fXiQ.sMfVteJo-ABfiEctdP7C3e3jWR4 - HOST (don't touch)

client.run('ODQ4OTUyMTA4MTA3Njk0MTYy.YLUGQw.jKN7P1a6NMVwQuw1DW1Mc5-03DE')