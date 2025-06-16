import sys
import parser
import symbolHandler
import translator

def main():
    #确保有2个输入参数
    if (len(sys.argv)!= 2):
        print("Usage: python Assembler.py <file.asm>")
        exit(1)
    
    #输入文件细节
    file_path = sys.argv[1]
    file_name = file_path.split(".")[0]
    file_extention = file_path.split(".")[1]

    #确保输入文件为.asm文件
    if (file_extention!= "asm"):
        print("Error: input file must be a.asm file")
        exit(1)

    #打开输出文件
    outputExtention = ".hack"
    output_file_path = file_name + outputExtention
    output_file = open(output_file_path, "w")

    #解析代码
    commands = parser.get_commands(file_path)

    SymbolHandler = symbolHandler.SymbolHandler(commands)
    commands = SymbolHandler.getConvertedCommands()

    Translator = translator.translator(commands)
    code = Translator.translate()

    #输出hack代码
    for line in code:
        output_file.write(line + "\n")

    #关闭输出文件
    output_file.close()

if __name__ == "__main__":
    main()