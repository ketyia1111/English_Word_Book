from tkinter import messagebox
from excel import ExcelOperator
import os, sys, time
import tkinter as tk 

def clear():
    vocabulary_entry.delete(0, 'end') 
    speake_entry.delete(0, 'end')
    japanese_entry.delete(0,'end')
    example_entry.delete(1.0,'end')

def write():
    if vocabulary.get() == "" or speake.get() == "" or japanese.get() == "" or example_entry.get('1.0', 'end') == "":
        messagebox.showwarning('エラー', '入力されていない項目があります')
    else:
        excel = ExcelOperator("./english_project_only_use.xlsx")

        excel.write_cell(vocabulary.get() , speake.get() , japanese.get() , example_entry.get('1.0', 'end'))

        clear()

        messagebox.showinfo('書き込み完了', '単語を追加しました!')



def test():

    root = tk.Tk()

    root.title("English vocabulary test")

    root.geometry("600x400")

    # メインフレームの作成と設置
    topframe = tk.Frame(root,relief=tk.RAISED)
    topframe.pack(padx=5,pady=20)

    

    def action():

        excel = ExcelOperator("./english_project_only_use.xlsx")
    
        count = excel.get_row_count()

        global index

        index += 1

        if index <= count:
            test_button.config(text="次へ")
        else:
            test_button.config(text="テストが終了しました")
    
        if index-1 <= count-1:
            index_label.config(text=f"{index-1}/{count-1}")
            index1_label.config(text=excel.getvoc(index))
            index2_label.config(text=excel.getspeak(index))
            index3_label.config(text=excel.getjap(index))
            index4_label.config(text=excel.getexa(index))

    label = tk.Label(topframe, text="英単語帳",justify="center",font=("MSゴシック", "20", "bold"))
    label.grid()

    index_label = tk.Label(root)
    index_label.pack(pady=10)

    index1_label = tk.Label(root)
    index1_label.pack(pady=10)

    index2_label = tk.Label(root)
    index2_label.pack(pady=10)

    index3_label = tk.Label(root)
    index3_label.pack(pady=10)

    index4_label = tk.Label(root)
    index4_label.pack(pady=10)

    test_button = tk.Button(
            topframe,
            text="テストスタート",
            width=20, 
            height=3,
            font=("MSゴシック", "10", "bold"),
            command=action
    )
    test_button.grid()
    
    root.mainloop()



index = 1


# メインウィンドウ作成
root = tk.Tk()

root.title("English vocabulary book management")

root.geometry("600x650")

# メインフレームの作成と設置
topframe = tk.Frame(root,relief=tk.RAISED)
topframe.pack(padx=5,pady=20)

#formフレームの作成
formframe = tk.Frame(root, pady=5, padx=5, relief=tk.RAISED, bd=2, bg="brown")
formframe.pack(fill=tk.Y)

#テスト実施ボタン
testframe = tk.Frame(root, pady=5, padx=5, relief=tk.RAISED)
testframe.pack(fill=tk.Y)

#タイトルを追加
label = tk.Label(topframe, text="English vocabulary book management",
                justify="center",
                font=("MSゴシック", "20", "bold")
        )
#タイトル表示
label.grid()



#フォーム要素を作成
#①
label1 = tk.Label(formframe,
                 text='単語',
                 font=("MSゴシック", "20", "bold"))

label1.grid(row=0, column=0)

vocabulary = tk.StringVar()
vocabulary_entry = tk.Entry(
    formframe,
    textvariable=vocabulary,
    width=20,
    font=("MSゴシック", "20", "bold"),
    bd=3)
vocabulary_entry.grid(row=0, column=1,padx=10)

#2　ラジオ

#3

label2 = tk.Label(formframe,
                 text='発音',
                 font=("MSゴシック", "20", "bold"))

label2.grid(row=1, column=0)

speake = tk.StringVar()
speake_entry = tk.Entry(
    formframe,
    textvariable=speake,
    width=20,
    font=("MSゴシック", "20", "bold"),
    bd=3)
speake_entry.grid(row=1, column=1,padx=10,pady=10)

#4
label3 = tk.Label(formframe,
                 text='日本語訳',
                 font=("MSゴシック", "20", "bold"))

label3.grid(row=2, column=0)

japanese = tk.StringVar()
japanese_entry = tk.Entry(
    formframe,
    textvariable=japanese,
    width=20,
    font=("MSゴシック", "20", "bold"),
    bd=3)
japanese_entry.grid(row=2, column=1,padx=10,pady=10)


#5
label4 = tk.Label(formframe,
                 text='例文',
                 font=("MSゴシック", "20", "bold"))

label4.grid(row=3, column=0)


example_entry = tk.Text(
    formframe,
    width=20,
    height=5,
    font=("MSゴシック", "20", "bold"),
    bd=3)
example_entry.grid(row=3, column=1,padx=10,pady=10)


#フォームコントロールボタン

clear_button = tk.Button(
                formframe,
                text="クリア",
                width=10, 
                height=3,
                font=("MSゴシック", "10", "bold"),
                command=clear
                )
clear_button.grid(row=4, column=0,pady=10)

ok_button = tk.Button(
                formframe,
                text="書き込む",
                width=30, 
                height=3,
                font=("MSゴシック", "10", "bold"),
                command=write,
                bd=3)

ok_button.grid(row=4, column=1,pady=10)

test_button = tk.Button(
                testframe,
                text="テスト実施",
                width=50, 
                height=3,
                font=("MSゴシック", "10", "bold"),
                bd=3,
                bg="chocolate",
                command=test
                )

test_button.pack(pady=20)


root.mainloop()

#https://camp.trainocate.co.jp/magazine/python-class/

# ↑をクラス化
# 値の取得
# エクセルに値を入力
# テストの実施
# 　別画面を作成
# 　ボタンを押すと回答と例文が出力できる
# WEB検索ができる画面を表示
