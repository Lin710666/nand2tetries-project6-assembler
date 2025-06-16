import symbolHandler
import parser

commands = parser.get_commands("./asm_files/Max.asm")
print(commands)

commands = symbolHandler.SymbolHandler(commands)
converted_commands = commands.getConvertedCommands()
print(converted_commands)

