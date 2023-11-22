import tkinter as tk
from excel import ExcelOperator


def show_index():
    
    excel = ExcelOperator("./english_project_only_use.xlsx")
    
    count = excel.get_row_count()

    global index

    index += 1
    
    if index-1 <= count-1:
        index_label.config(text=f"{index-1}/{count-1}")
        index1_label.config(text=excel.getvoc(index))
        index2_label.config(text=excel.getspeak(index))
        index3_label.config(text=excel.getjap(index))
        index4_label.config(text=excel.getexa(index))


index = 1

root = tk.Tk()
root.geometry("200x100")

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

button = tk.Button(root, text="Show Index", command=show_index)
button.pack()

root.mainloop()
