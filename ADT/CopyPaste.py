


import csv
from logging import root

import pandas as pd
import tkinter as tk
from tkinter import filedialog

root=tk.Tk()
root.withdraw()
filepath=filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
columns = ['organization name'] # replace with the actual column names
data=[]
with open(filepath, 'r') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)
        print(row)

with open('new_file.csv', 'w', newline='') as newfile:
    writer = csv.writer(newfile)
    writer.writerow(columns)
    for _, row in data:
        writer.writerow(row)

f.close()
