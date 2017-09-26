from tkinter import *
import csv
from AccountTransaction import AccountTransaction

class MainForm:
    root = Tk()

    def __init__(self):
        self.root.geometry("1000x800")
        self.root.title("My Money")
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

    def donothing(self):
        with open(r"C:\Users\Chris\Documents\Finances\2017\April 2017.csv", 'r') as f:
            reader = csv.reader(f)
            listOfTransactions = []
            for row in reader:
                newObject = AccountTransaction(row[0], row[1], row[2], row[3], row[4])
                listOfTransactions.append(newObject)

    def load(self):
        self.root.mainloop()