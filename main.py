from tkinter import *

# Creating a new window
# Creates a window but closes it immediately (like screen in turtle)
window = Tk()
# Adding a title to window
window.title("My first GUI Program")
# Size can be adjusted by window.minsize(width, height)
window.minsize(width=500, height=200)

# Functions

def button_clicked():
    # new_label = Label(text="I got clicked. Yeah")
    # new_label.pack()
    my_label["text"] = input.get()


# Labels
my_label = Label(text="I am a Label", font=("Arial", 10, "italic"))
# This creates a label/component but doesn't apply it directly. Therefore, I have to tell tkinter what to do with the
# label. The pack method. Centers it to the window.
my_label.grid(column=0, row=0)

# The packer is a useful tool for tkinter. It specifies the widgets' geometry. https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# To access settings/arguments of my object (my_label in this case) there are multiple ways of doing this. One would be:

my_label["text"] = "New text"  # Like a dictionary accessing value
my_label.config(text="More new text",
                font=("Times New Roman", 12, "bold"))  # config is used for changing multiple values





# Button

button = Button(text="Click me", command=button_clicked)  # Command tells the button what should happen if clicked
button.grid(column=1, row=1)

new_button = Button(text="Click also me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry. Kind of input. Documentation is https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

input = Entry(width=10)
input.grid(column=3, row=2)
# the get method of entry returns the input

# How to define layouts.The pack() is also a layout manager.
# Pack packs the widgets and kind of place the widgets in a loosely ordinary manner. By default it starts from top
# and put the next under the previous one. I can change the postion by the 'side' attribute.

# Also there is place() which provides x, and y coor.



# Puts it to the left upper corner

# And there is grid().Can be used to place the widgets to columns and rows. They are relative to other widgets so first
# widget has to be specified at 0, 0
new_label = Label(text="HEY")
new_label.grid(column= 0, row=0)


# Also I can create padding (Abstand vom rand des fensters) for a better look.

window.config(padx=20, pady=20)



window.mainloop()
