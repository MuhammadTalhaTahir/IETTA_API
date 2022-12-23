from tika import parser
import datetime, os, json

class pdfToTextConverter:
    def __init__(self,fileName = None) -> None:
        self.fileName = fileName
        self.parsed = None 
        self.__storingLocation = "./userFiles/"
        self.__OpenFile()
        if not os.path.isdir(self.__storingLocation):
            os.makedirs(self.__storingLocation)
        self.fileName = self.fileName[:len(self.fileName)-4]

    
    def __OpenFile(self) -> None:
        try:
            if self.fileName:
                self.parsed = parser.from_file(self.fileName)
        except Exception as e:
            print(e)
    
    def ParseContent(self) -> str:
        try:
            if self.parsed:
                return self.parsed['content']
        except Exception as e:
            print(e)
    
    def ParseMetaData(self) -> str:
        try:
            if self.parsed:
                return self.parsed['metadata']
        except Exception as e:
            print(e)

    def convertToText(self):
        try:
            with open(self.__storingLocation+self.fileName+".txt",'w', encoding="utf-8") as file:
                file.write(self.ParseContent().lstrip())
            with open(self.__storingLocation+'metaData-'+self.fileName+".json",'w', encoding="utf-8") as file:
                file.write(json.dumps(self.ParseMetaData()))
            os.remove(self.fileName+".pdf")
        except Exception as e:
            print(e)



pdfToTextConverter("testFile.pdf").convertToText()