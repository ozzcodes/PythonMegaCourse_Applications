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
import tkinter.messagebox as mb
from PythonBasics.Object_Oriented_Programming.App5_Transformed.backend_data import MyDatabase

'''
Create the command options for each button
Also, for the delete function, you need to create ability to select a data item in the list-box
'''

database = MyDatabase('books.db')


def view_all_data():
    # Make sure list is empty (delete any previous populations)
    data_view.delete(0, END)
    for row in database.view():
        data_view.insert(END, row)


def search_item():
    data_view.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        data_view.insert(END, row)


def add_item():
    database.insert(title_text.get(), author_text.get(), year_text.get(), database.isbn_generator())
    data_view.delete(0, END)
    data_view.insert(END, (title_text.get(), author_text.get(), year_text.get(),
                           database.isbn_generator()))


# Uses helper function for selecting the data item in the listbox
def delete_item():
    database.delete(selected[0])


def update_item():
    database.update(selected[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def close_program():
    # Call to a textbox message alert
    if mb.askokcancel("Quit", 'Do you really want to quit?'):
        window.quit()


# noinspection PyUnusedLocal
def get_selected_row(event):
    # Since using bind function, need global variable for passed event(needed)
    # noinspection PyGlobalUndefined
    """
    Args:
        event:
    """
    global selected
    index = data_view.curselection()[0]
    selected = data_view.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected[1])
    entry2.delete(0, END)
    entry2.insert(END, selected[2])
    entry3.delete(0, END)
    entry3.insert(END, selected[3])
    entry4.delete(0, END)
    entry4.insert(END, selected[4])


'''
Create the initial window and then all the buttons, and views
'''
# Create the Window
window = Tk()

# Create program Title
window.wm_title('My Bookstore')

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
# Create a bind method (Tk function) for applying the id to an entry
data_view.bind('<<ListboxSelect>>', get_selected_row)

# Create buttons for user interaction
button1 = Button(window, text='View All', width=14, command=view_all_data)
button1.grid(row=2, column=3)

button2 = Button(window, text='Search Entry', width=14, command=search_item)
button2.grid(row=3, column=3)

button3 = Button(window, text='Add Entry', width=14, command=add_item)
button3.grid(row=4, column=3)
button3.bind()

button4 = Button(window, text='Update Selected', width=14, command=update_item)
button4.grid(row=5, column=3)

button5 = Button(window, text='Delete Selected', width=14, command=delete_item)
button5.grid(row=6, column=3)

button6 = Button(window, text='Close', width=14, command=close_program)
button6.grid(row=7, column=3)

# Loop through the application until close button if pressed
window.mainloop()
