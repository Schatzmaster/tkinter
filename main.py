from tkinter import *

# Creating a new window
# Creates a window but closes it immediately (like screen in turtle)
window = Tk()
# Adding a title to window
window.title("My first GUI Program")
# Size can be adjusted by window.minsize(width, height)
window.minsize(width=500, height=200)

# Labels
my_label = Label(text="I am a Label", font=("Arial", 10, "italic"))
# This creates a label/component but doesn't apply it directly. Therefore, I have to tell tkinter what to do with the
# label. The pack method. Centers it to the window.
my_label.pack(expand=False)

# The packer is a useful tool for tkinter. It specifies the widgets' geometry. https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

# To access settings/arguments of my object (my_label in this case) there are multiple ways of doing this. One would be:

my_label["text"] = "New text"  # Like a dictionary accessing value
my_label.config(text="More new text",
                font=("Times New Roman", 12, "bold"))  # config is used for changing multiple values


def button_clicked():
    # new_label = Label(text="I got clicked. Yeah")
    # new_label.pack()
    my_label["text"] = input.get()


# I can also create buttons

button = Button(text="Click me", command=button_clicked)  # Command tells the button what should happen if clicked
button.pack()

# Entry. Kind of input. Documentation is https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

input = Entry(width=10)
input.pack()
# the get method of entry returns the input


window.mainloop()
