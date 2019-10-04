"""
A program that has a database of books and information:
Title, Author
Year, ISBN

User's can:

View all records
Search for an Entry
Add an Entry
Update an Entry
Delete an Entry
Close the program
"""

from tkinter import *
from backend_data import db_connect

# Create the initial window
window = Tk()

# Create multiple labels in a grid
label1 = Label(window, text='Title')
label1.grid(row=0, column=0)
label1 = Label(window, text='Author')
label1.grid(row=0, column=2)
label1 = Label(window, text='Year')
label1.grid(row=1, column=0)
label1 = Label(window, text='ISBN')
label1.grid(row=1, column=2)

# Create entry space widget
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# Create a list of items in a visual box
data_view = Listbox(window, height=8, width=40)
data_view.grid(row=2, column=0, rowspan=8, columnspan=2)

# Create a scrollbar
scroll1 = Scrollbar(window)
scroll1.grid(row=2, column=2, rowspan=8)

# Apply configure method to scrollbox
data_view.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=data_view.yview)

# Create buttons for user interaction
button1 = Button(window, text='View All', width=14)
button1.grid(row=2, column=3)
button2 = Button(window, text='Search Entry', width=14)
button2.grid(row=3, column=3)
button3 = Button(window, text='Add Entry', width=14)
button3.grid(row=4, column=3)
button4 = Button(window, text='Update Selected', width=14)
button4.grid(row=5, column=3)
button5 = Button(window, text='Delete Selected', width=14)
button5.grid(row=6, column=3)
button6 = Button(window, text='Close', width=14)
button6.grid(row=7, column=3)

# Loop through the application until close button if pressed
window.mainloop()
