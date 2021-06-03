from testClasses import info


messageShort2="""Short #ETH

Entry: 2675 - 2700

Targets:
2650
2620
2580
2550
2530
2400
2300

SL: 2750

⭕️ TRADE AT YOUR OWN RISK"""

messageShort ="""Short #BTC 

Entry: 36700 - 37000

Targets: 
36200
35800
35500
35000
34000
33300

SL: 37500 

⭕️ TRADE AT YOUR OWN RISK

@TheAnalyst100"""


def callALL(message):
    newObject = info(message)
    condition=newObject.checkMessage()
    if condition:
        tradeType=newObject.findTradeType()
        print(tradeType)
        tradeSymbol=newObject.findSymbol()
        print(tradeSymbol)
        tradeEntry=newObject.findEntry()
        print(tradeEntry)
        tradeTPs=newObject.findTPs()
        print(tradeTPs)
        tradeSL=newObject.findSL()
        print(tradeSL)

callALL(messageShort2)