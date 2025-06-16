#将变量和标签这些symbols转换为地址

import predefinedSymbolTable

class SymbolHandler:
    def __init__(self,commands):
        self.commands = commands
        self.symbolTable = predefinedSymbolTable.symbolTable

    def islabel(self,command):
        if "(" in command:
            return True
        else:
            return False
        
    def storeLabel(self):
        labelCount = 0
        for (index,command) in enumerate(self.commands):
            if self.islabel(command):
                start_index = command.find("(")+1
                end_index = command.find(")")
                label = command[start_index:end_index]
                self.symbolTable[label] = (index-labelCount) #比如：第二个lable需要减一，因为第一个label会被忽略掉，不能把它算在内
                labelCount += 1

    def isSymbol(self,command):
        if (command[0] == "@"):
            try:
                int(command[1:])
                return False
            except:
                return True
        else:
            return False
        
    def storeVariables(self):
        RAMLocation = 16
        for command in self.commands:
            if self.isSymbol(command):
                symbol = command[1:]
                try:
                    self.symbolTable[symbol]
                except:
                    self.symbolTable[symbol] = RAMLocation
                    RAMLocation += 1

    def getConvertedCommands(self):
        self.storeLabel()
        self.storeVariables()

        convertedCommands = []
        for command in self.commands:
            if self.isSymbol(command):
                symbol = command[1:]
                convertedCommands.append("@" + str(self.symbolTable[symbol]))
            elif self.islabel(command):
                pass
            else:
                convertedCommands.append(command)
            
        return convertedCommands
                
