
class info:
    def __init__(self,messageGiven):
        self.message=messageGiven
        self.symbols_to_check = ["TRADE AT YOUR OWN RISK","Targets","Entry"]
        self.typeoftrade = ""  # DONE
        self.symbol = ""  # DONE
        self.entryRange = ""  # DONE
        self.TP = []  # DONE
        self.SL = ""

    def checkMessage(self):
        if self.message.find("Long") == -1 and self.message.find("Short")==-1 and self.message.find("Buy") == -1 and self.message.find("Sell")==-1:
            return False
        else:
            for symbol in self.symbols_to_check:
                if self.message.find(symbol) == -1:
                    return False
        return True

    def findTradeType(self):
        for letter in self.message:
            self.typeoftrade += letter.lower()
            if self.typeoftrade == "long" or self.typeoftrade == "short" or self.typeoftrade == "buy" or self.typeoftrade == "sell":
                return self.typeoftrade

    def findSymbol(self):
        i=0
        for letter in self.message:
            if i>0:
                self.symbol+=letter
                if letter == ' ':
                    return self.symbol
            elif letter==' ':
                i+=1
        return "SymbolNotFound"
        #
        #
        #
        # # symbolIndex = self.message.find('#')
        # # for i in range(symbolIndex + 1, symbolIndex + 10):
        # #     self.symbol += self.message[i].lower()
        # #     if self.message[i] == ' ' or self.message[i] == '\n':
        # #         break
        # return self.symbol

    def findEntry(self):
        symbolIndex = self.message.find(':')
        for i in range(symbolIndex + 2, symbolIndex + 100):
            self.entryRange += self.message[i]
            if self.message[i] == '\n':
                break
        return self.entryRange

    def findTPs(self):
        keywordLen = len("Targets:")
        startingIndex = self.message.find("Targets:") + keywordLen + 1
        holder = ""
        dupa = True
        for i in range(startingIndex, startingIndex + len(self.message)):
            dupa = True
            if self.message[i] == '\n':
                self.TP.append(holder)
                holder = ""
                dupa = False
            if self.message[i] == '\n' and self.message[i + 1] == '\n':
                break
            if dupa == True:
                holder += self.message[i]
        for element in self.TP:
            if element == '' or element == ' ' or element == '\n':
                self.TP.pop(self.TP.index(element))
        return self.TP

    def findSL(self):
        index = self.message.find("SL:")
        if index == -1:
            return None
        else:
            for i in range(index + 3, index + 10):
                if self.message[i] == ' ':
                    continue
                self.SL += self.message[i]
        return self.SL