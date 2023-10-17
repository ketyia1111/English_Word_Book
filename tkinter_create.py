import os, sys, time
import tkinter as tk


class mainframe(tk.Frame):
    def __init__(self,master):
        self.master = master
        super().__init__(master,width=500,height=500,bg="chocolate")
        
        self.master.title("English vocabulary book management")
        self.pack()

        # メインフレームの作成と設置
        self.topframe = tk.Frame(self)
        self.topframe.pack(padx=5,pady=20)

        #formフレームの作成
        self.formframe = tk.Frame(self, pady=5, padx=5, relief=tk.RAISED, bd=2, bg="brown")
        self.formframe.pack(fill=tk.Y)

        #テスト実施フレーム
        self.testframe = tk.Frame(self, pady=5, padx=5, relief=tk.RAISED, bg="chocolate")
        self.testframe.pack(fill=tk.Y)

        #値を取得する配列を用意
        self.value = []

    def label_set(self,val1,color,id,val2="center",font1="MSゴシック",font2="20",font3="bold"):

        self.text=val1
        self.justify=val2
        self.fontfamily=font1
        self.fontsize=font2
        self.fontstyle=font3
        self.bg = color
        self.id = id
    
    def create_label_top(self):
        self.label = tk.Label(
            self.topframe, 
            text=self.text,
            justify=self.justify,
            font=(self.fontfamily, self.fontsize, self.fontstyle),
            bg=self.bg
        )
        self.label.grid()


    def create_label_form(self):
        self.label = tk.Label(
            self.formframe, 
            text=self.text,
            justify=self.justify,
            font=(self.fontfamily, self.fontsize, self.fontstyle),
            bg=self.bg
        )
        self.label.grid(row=self.id-1, column=0)

    def entry_set(self,id,height=5,width=20,font1="MSゴシック",font2="20",font3="bold",bd=3):

        self.id=id
        self.height = height
        self.width=width
        self.fontfamily=font1
        self.fontsize=font2
        self.fontstyle=font3
        self.bd = bd
    
    def create_entry(self):

        if self.id == 1:
            self.vocabulary = tk.StringVar()
            self.text = self.vocabulary
        elif self.id == 2:
            self.speak = tk.StringVar()
            self.text = self.speak
        elif self.id == 3:
            self.japanese = tk.StringVar()
            self.text = self.japanese

        
        entry = tk.Entry(
            self.formframe,
            textvariable=self.text,
            width=self.width,
            font=(self.fontfamily, self.fontsize, self.fontstyle),
            bd=self.bd
        )

        entry.grid(row=self.id-1, column=1,padx=10)

    

    def create_textarea(self):

        entry = tk.Text(
            
            self.formframe,
            height=self.height,
            width=self.width,
            font=(self.fontfamily, self.fontsize, self.fontstyle),
            bd=self.bd
        )

        entry.grid(row=self.id-1, column=1,padx=10)

    def button_set(self,id,lorr,text,width,height,font1="MSゴシック", font2="10", font3="bold",bd=3):
        
        self.id=id
        self.lorr=lorr
        self.text=text
        self.height = height
        self.width=width
        self.fontfamily=font1
        self.fontsize=font2
        self.fontstyle=font3
        self.bd = bd

    def create_button_form(self):
        
        button = tk.Button(
                self.formframe,
                text=self.text,
                height=self.height,
                width=self.width,
                font=(self.fontfamily, self.fontsize, self.fontstyle),
                bd=self.bd)

        button.grid(row=self.id-1, column=self.lorr,pady=10)

    def create_button_test(self):
        
        button = tk.Button(
                self.testframe,
                text=self.text,
                height=self.height,
                width=self.width,
                font=(self.fontfamily, self.fontsize, self.fontstyle),
                bd=self.bd)

        button.pack(pady=15)

class mainframe2(tk.Frame):
    def __init__(self,master):
        super().__init__(master,width=300,height=300)
        self.master.title("English vocabulary research")
        self.pack()

        # メインフレームの作成と設置
        self.topframe = tk.Frame(self)
        self.topframe.pack(padx=5,pady=20)


class mainframe3(tk.Frame):
    def __init__(self,master):
        super().__init__(master,width=500,height=300)
        self.master.title("English vocabulary test")
        self.pack()

