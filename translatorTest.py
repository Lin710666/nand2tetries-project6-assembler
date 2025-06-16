import parser
import symbolHandler
import translator

no_whitespace_file = parser.get_commands("./asm_files/Pong.asm")
no_symbol_file = symbolHandler.SymbolHandler(no_whitespace_file).getConvertedCommands()
machine_code = translator.translator(no_symbol_file).translate()
print(machine_code)
