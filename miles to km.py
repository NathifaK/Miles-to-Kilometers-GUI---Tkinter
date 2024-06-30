import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    mile_input = entryint.get()
    km_output = round(mile_input * 1.61,4)
    output_str.set((str(km_output)+" KMS"))


window = ttk.Window(themename= 'minty', minsize=[500,220])
window.title("Miles to Kilometer")
window.geometry("300x150")

title_label = ttk.Label(master = window, text =  "Miles to Kilometers", font = "Arial 20 bold") #master is the container

title_label.pack(pady=10)

input_frame = ttk.Frame(master=window)

entryint = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable= entryint)
button = ttk.Button(master=input_frame, text = "convert" , comman =convert)

entry.pack(side='left', padx=10)
button.pack(side = 'left')
input_frame.pack(pady=10)


#output label
output_str = tk.StringVar()
output_label =ttk.Label(master=window, text='Output', font="Arial 16", textvariable=output_str)
output_label.pack(pady=5)
window.mainloop()