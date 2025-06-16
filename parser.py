# 删掉.asm文件中，所有的空格，空行和注释

#Class
class lineParser():
    def __init__(self, line):
        self.line = line
    
    def rmspaces(self):
        self.line = self.line.replace(" ", "")

    def rmcomments(self):
        split_line = self.line.split("//",1)
        self.line = split_line[0]

    def rmnewlinechar(self):
        split_line = self.line.split("\n",1)
        self.line = split_line[0]

    def is_blank(self):
        if self.line == "":
            return True
        else:
            return False
        
#Function
def get_commands(file_path):

    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    parsed_file = []
    for line in lines:
        line_parser=lineParser(line)
        line_parser.rmcomments()  
        line_parser.rmspaces()  
        line_parser.rmnewlinechar()

        if not line_parser.is_blank():
            parsed_file.append(line_parser.line)


    return parsed_file

    
    