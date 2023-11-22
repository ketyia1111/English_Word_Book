import openpyxl
from datetime import datetime

class ExcelOperator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.wb = openpyxl.load_workbook(file_name)
        self.sheet = self.wb["words"]
        


    def write_cell(self, value1,value2,value3,value4):
        
        now = datetime.now()

        value5 = now.strftime("%Y/%m/%d")

        value4 = value4.replace("\n", "")

        value4 = value4.strip()

        self.row = 2

        self.id = 1

        flag = True

        while(flag):
            if self.sheet[f'A{self.row}'].value == None:
                flag = False
            else:
                self.row += 1
                self.id += 1

        

        self.sheet[f'A{self.row}'] = value=self.id
        self.sheet[f'B{self.row}'] = value1
        self.sheet[f'C{self.row}'] = value2
        self.sheet[f'D{self.row}'] = value3
        self.sheet[f'E{self.row}'] = value4
        self.sheet[f'F{self.row}'] = value5
        

        self.wb.save(self.file_name)

    def get_row_count(self):

        row_count = self.sheet.max_row

        return row_count


    def getvoc(self,id):

        return self.sheet[f'B{id}'].value

    def getspeak(self,id):
        return self.sheet[f'C{id}'].value


    def getjap(self,id):
        return self.sheet[f'D{id}'].value
    
    def getexa(self,id):
        return self.sheet[f'E{id}'].value