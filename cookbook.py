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


# Textbox
text = Text(width=30, height=5)
# Put cursor in texbox
text.focus()
text.insert(END, "Some text")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox

def spinbox_used():
    # gets the current value of spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value

def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if button is checked, else 0
    print(checked_state.get())


# Variable to hold on to checked state, 1 is on 0 is off
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", command=checkbutton_used, variable=checked_state)
# checked_state.get()
checkbutton.pack()


# Radio button
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", command=radio_used, variable=radio_state, value=1)
radiobutton2 = Radiobutton(text="Option 2", command=radio_used, variable=radio_state, value=2)
radiobutton1.pack()
radiobutton2.pack()


# List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Pear", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()