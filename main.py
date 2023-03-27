import tkinter as tk
from tkinter import ttk

class Main:
    def __init__(self, root):
        mainframe = ttk.Frame(root, padding="10")
        mainframe.grid(column=0, row=0, sticky="nesw")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text="name:").grid(column=0, row=0)

        self.name = tk.StringVar()
        ttk.Entry(mainframe, textvariable=self.name).grid(column=0, row=1)
        self.name.trace_add("write", self.change_greeting)

        self.greeting = tk.StringVar()
        ttk.Label(mainframe, textvariable=self.greeting).grid(column=2, row=1)

        ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=2, columnspan=3, sticky="ew", pady=10)

        self.value_one = tk.IntVar()
        self.value_two = tk.IntVar()
        self.value_three = tk.IntVar()
        self.combined = tk.StringVar(value="0")
        ttk.Checkbutton(mainframe, text="one", variable=self.value_one, command=self.update).grid(column=0, row=3, sticky="w")
        ttk.Checkbutton(mainframe, text="two", variable=self.value_two, command=self.update).grid(column=0, row=4, sticky="w")
        ttk.Checkbutton(mainframe, text="three", variable=self.value_three, command=self.update).grid(column=0, row=5, sticky="w")

        ttk.Label(mainframe, text="=").grid(column=1, row=4)

        ttk.Label(mainframe, textvariable=self.combined).grid(column=2, row=4)

        ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=6, columnspan=3, sticky="ew", pady=10)

        ttk.Separator(mainframe, orient="vertical").grid(column=1, row=7, rowspan=3, sticky="ns", padx=10)

        ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=0, row=7)

        self.click_amount = 0
        ttk.Button(mainframe, text="binary count", command=self.set_num_to_binary).grid(column=0, row=8)
        self.binary_count = tk.StringVar(value="binary value will\nappear here")
        ttk.Label(mainframe, textvariable=self.binary_count).grid(column=0, row=9, sticky="n")

        self.sentence = tk.StringVar()
        sentence_entry = ttk.Entry(mainframe, foreground="grey", textvariable=self.sentence)
        sentence_entry.grid(column=2, row=7)
        self.sentence.set("Enter a sentence")
        sentence_entry.bind('<FocusIn>', lambda e: self.on_entry_click(entry=sentence_entry))
        sentence_entry.bind('<FocusOut>', lambda e: self.on_entry_focusout(entry=sentence_entry))

        ttk.Button(mainframe, text="List the words!", command=self.sentence_to_wordlist).grid(column=2, row=8)
        self.word_list = tk.StringVar()
        ttk.Label(mainframe, textvariable=self.word_list).grid(column=2, row=9)

        for column in range(mainframe.grid_size()[0]):
            mainframe.columnconfigure(column, weight=1)
        for row in range(mainframe.grid_size()[1]):
            mainframe.rowconfigure(row, weight=1)
        
    def sentence_to_wordlist(self):
        self.word_list.set("\n".join(self.sentence.get().split(" ")))
    
    def on_entry_click(self, entry):
        if self.sentence.get() == "Enter a sentence":
            self.sentence.set("")
            entry.config(foreground='black')

    def on_entry_focusout(self, entry):
        if self.sentence.get() == '':
            self.sentence.set("Enter a sentence")
            entry.config(foreground='grey')

    def set_num_to_binary(self):
        self.click_amount += 1
        self.binary_count.set(f"{self.click_amount}: {bin(self.click_amount).replace('0b', '')}")

    def update(self):
        self.combined.set(str(self.value_one.get() + self.value_two.get() + self.value_three.get()))

    def change_greeting(self, name, index, mode):
        self.greeting.set(f"Hello, {self.name.get()}!")

root = tk.Tk()
root.title("Practice Project")
Main(root)
root.mainloop()