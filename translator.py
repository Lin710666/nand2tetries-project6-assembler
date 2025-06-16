#把ASM代码翻译成机器码

import CInstructionTables

#CLASSES
class translator():
    def __init__(self,commands):
        self.commands = commands

    def getCommandCotegories(self):
        #获取命令的类型
        command_categories = []
        for command in self.commands:
            if "@" in command:
                #添加A-Instruction对象
                command_categories.append(ACommand(command))
            else:
                #添加C-Instruction对象
                command_categories.append(CCommand(command))
        return command_categories

    def translate(self):
        #翻译成机器码
        command_categories = self.getCommandCotegories()
        machine_code = []
        for command in command_categories:
            machine_code.append(command.translate())
        return machine_code

class ACommand():
    def __init__(self,line):
        self.line = line
        self.type = "A"
        self.address = self.line[1:]

    def translate(self):
        #把地址翻译成机器码
        address_binary = get15bitsBinary(int(self.address))
        binary = "0"+address_binary
        return binary

class CCommand():
    def __init__(self,line):
        self.line = line
        self.type = "C"
        if "=" in self.line:
            self.jump = "null"
            split_line = self.line.split("=")
            self.dest = split_line[0]
            self.comp = split_line[1]
        else:
            self.dest = "null"
            split_line = self.line.split(";")
            self.comp = split_line[0]
            self.jump = split_line[1]

    def translate(self):
        #把命令翻译成机器码
        comp_binary = CInstructionTables.comp[self.comp]
        dest_binary = CInstructionTables.dest[self.dest]
        jump_binary = CInstructionTables.jump[self.jump]
        binary = "111" + comp_binary + dest_binary + jump_binary
        return binary

#FUNCTIONS
def get15bitsBinary(decimal):
    required_bits = 15
    binary = bin(decimal)[2:].zfill(required_bits)
    return binary
    #TESTING
    #print(get15bitsBinary(12345))


