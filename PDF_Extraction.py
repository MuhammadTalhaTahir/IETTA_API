from tika import parser
import datetime, os

class pdfToTextConverter:
    def __init__(self,fileName = None) -> None:
        self.fileName = fileName
        self.parsed = None 
        self.__OpenFile()
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
            with open(self.fileName+".txt",'w', encoding="utf-8") as file:
                file.write(self.ParseContent())
            with open('metaData-'+self.fileName+".txt",'w', encoding="utf-8") as file:
                file.write(str(self.ParseMetaData()))
            os.remove(self.fileName+".pdf")
        except Exception as e:
            print(e)



pdfToTextConverter("sampleFile.pdf").convertToText()