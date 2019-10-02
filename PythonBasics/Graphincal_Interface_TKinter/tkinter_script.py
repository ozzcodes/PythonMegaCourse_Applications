from tkinter import *

# Create a window space (GUI)
window = Tk()


# Create a function to convert km to miles
def km_to_miles():
    # print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


# Create a title for the GUI
title = Tk.wm_title(window, 'My GUI Test')

# Create a button for the window
button1 = Button(window, text='Execute', command=km_to_miles)  # Use a defined value type for the button to execute
button1.grid(row=0, column=0, rowspan=2)

# Create an area with a value input
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Create a Text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Keep the window open with a mainloop
window.mainloop()
