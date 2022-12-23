
from tika import parser

class File_Parser:
    def __init__(self,fileName = None) -> None:
        self.fileName = fileName
        self.parsed = None 
    

    def OpenFile(self) -> None:
        try:
            if self.fileName:
                self.parsed = parser.from_file(self.fileName)
        except:
            pass
    
    def ParseContent(self) -> str:
        try:
            if self.parsed:
                return self.parsed['content']
        except:
            pass
    
    def ParseMetaData(self) -> str:
        try:
            if self.parsed:
                return self.parsed['metadata']
        except:
            pass



