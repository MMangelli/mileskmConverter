import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# window
window = ttk.Window(themename ='journal')
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()   #It is important to store the entry in an entry_int in order to call this variable in my function
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 5)    # The purpose pf packing is to take the Entry and button and put them inside of the frame
button.pack(side = 'left')
input_frame.pack(pady = 10) # This is to pack the input_frame into window
 
#output
output_string = tk.StringVar() #similar to entry int, its important to put make this label a string variable as the label itself will be changing
output_label = ttk.Label(
    master= window, 
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()