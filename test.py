from tkinter_create import mainframe
from tkinter_create import mainframe2
from tkinter_create import mainframe3
import tkinter as tk

#メインの画面
win = tk.Tk()

app = mainframe(win)

#タイトル作成-----------

#値セット
app.label_set(
    val1 = "English vocabulary book management",
    color = "chocolate",
    id = 1
    )
#作成
app.create_label_top()

#---------------------

#フォーム作成① 単語-----------

#ラベル値セット
app.label_set(
    val1 = "単語",
    color = "brown",
    id = 1)
#ラベル作成
app.create_label_form()

#エントリー値セット
app.entry_set(1)

#エントリー作成
app.create_entry()

#---------------------

#フォーム作成②　発音記号-----------

#ラベル値セット
app.label_set(
    val1 = "発音記号",
    color = "brown",
    id = 2)
#ラベル作成
app.create_label_form()

#エントリー値セット
app.entry_set(2)

#エントリー作成
app.create_entry()

#---------------------

#フォーム作成③　日本語訳-----------

#ラベル値セット
app.label_set(
    val1 = "日本語訳",
    color = "brown",
    id = 3)
#ラベル作成
app.create_label_form()

#エントリー値セット
app.entry_set(3)

#エントリー作成
app.create_entry()

#---------------------

#フォーム作成④　例文-----------

#ラベル値セット
app.label_set(
    val1 = "例文",
    color = "brown",
    id = 4)
#ラベル作成
app.create_label_form()

#エントリー値セット
app.entry_set(4)

#エントリー作成
app.create_textarea()

#---------------------

#ボタン作成　クリア-----------
app.button_set(
    id = 5,
    lorr = 0,
    text = "クリア",
    width=10,
    height=3,
)

app.create_button_form()

#---------------------

#ボタン作成　OK-----------
app.button_set(
    id = 5,
    lorr = 1,
    text = "書き込む",
    width=30,
    height=3,
)

app.create_button_form()

#---------------------

#テストボタン作成
app.button_set(
    id = 0,
    lorr = 0,
    text = "テスト実施",
    width=50,
    height=3,
)
app.create_button_test()

#---------------------

#ブラウザ画面
#root = tk.Tk()
#good = mainframe2(root)

#テスト画面
#test = tk.Tk()
#tests = mainframe3(test)


app.mainloop()
# good.mainloop()