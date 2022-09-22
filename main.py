from tkinter import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
import json

root = Tk()
root.config(bg="#e7e2a7")
root.title("Nomenclature")
common_name = StringVar()
bi_name = StringVar()

with open(r"nomenclature.json") as f:
    d = json.load(f)

com = list(d.keys())
bin = list(d.values())

Label(root, text="Binomial Nomenclature", font=("Comic Sans MS", 25, "bold"), bg="#e7e2a7").pack()

tree_frame = Frame(root).pack(pady=10)
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
tree.pack(fill=X)
tree_scroll.config(command=tree.yview)

tree["columns"] = ["S_No", "Common Name", "Binomial Nomenclature"]

tree.column("#0", width=0, stretch=NO)
tree.heading("#0", text="", anchor=W)

for i in ["S_No", "Common Name", "Binomial Nomenclature"]:
    tree.column(f"{i}", anchor=W, width=140)
    tree.heading(f"{i}", text=f"{i}", anchor=W)

for index, val in enumerate(d.items()):
    tree.insert(
        parent="", index="end", iid=index, text="", values=(index + 1, val[0], val[1])
    )

fr = Frame(root, bg="#e7e2a7")
fr.pack(padx=20)


def get_val(_):
    res.current(com.index(common_name.get()))
    tree.see(com.index(common_name.get()))
    tree.selection_set(com.index(common_name.get()))


def get_key(_):
    c.current(bin.index(bi_name.get()))
    tree.see(com.index(common_name.get()))
    tree.selection_set(com.index(common_name.get()))


c = AutocompleteCombobox(fr, width=27, textvariable=common_name, completevalues=com)
c.grid(row=0, column=0, padx=20)

res = AutocompleteCombobox(fr, width=27, textvariable=bi_name, completevalues=bin)
res.grid(row=0, column=1, pady=30, padx=20)

c["values"] = com
res["values"] = bin

c.bind("<<ComboboxSelected>>", get_val)
res.bind("<<ComboboxSelected>>", get_key)
c.bind("<Return>",get_val)
res.bind("<Return>",get_key)
mainloop()