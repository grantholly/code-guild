from Tkinter import Tk, Label, Button, Entry, StringVar, Menu, Radiobutton, IntVar, Checkbutton, Spinbox
from Tkinter import W, E, S, N, ACTIVE
import tkMessageBox
import tkFileDialog
import tkColorChooser

# parent GUI element
gui = Tk()

"""
labels
"""

gui.geometry("500x500+250+250")
gui.title("this is my window")
first_label = Label(text="this is my first label", fg="white", bg="green")
second_label = Label(text="this is my second label", fg="white", bg="blue")
third_label = Label(text="this is my third label", fg="white", bg="orange")
# all coordinates start at the top left (0, 0)
first_label.place(x="100", y="100")
# grid height and width is dependent on the geometry of the parent window
second_label.grid(row=1, column=2)
third_label.grid(row=0, column=0)
# you cannot mix grid and pack layout elements

"""
buttons and command callbacks
"""

def test_function():
    hello_label = Label(text="hi there user", fg="white", bg="red")
    # hello_label.place(x="250", y="250")
    hello_label.pack()

first_button = Button(text="ok", bg="red", command=test_function)
first_button.grid(row=2, column=2)

"""
entry boxes
"""

# global variable to collect the text from the entry field
my_text = StringVar()

def show_me_the_text():
    # the StringVar class in Tkinter has a get method to
    # to access the value from the field
    input_text = my_text.get()
    # the configure method is used to change any attribute
    second_label.config(text=input_text)

# submit button for text field
text_field_submit = Button(text="submit", command= show_me_the_text)
text_field_submit.grid(row=2, column=1)

# textvariable captures the text entered into the field
first_entry = Entry(gui, textvariable=my_text)
first_entry.grid(row=3, column=3)

"""
window menus
"""

def say_bye():
    second_label.config(text="goodbye")

menu_bar = Menu(gui)

# tearoff = 0 prevents the box from being detachable from parent
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="new item")
file_menu.add_command(label="edit")
file_menu.add_command(label="close", command=say_bye)

menu_bar.add_cascade(label="file", menu=file_menu)

# setup the parent gui object
gui.config(menu=menu_bar)

"""
creating dialogs
"""

def show_alert():
    # can also show error and warning level boxes
    # use showerror or showwarning
    # there are also ask functions like askyesno
    tkMessageBox.showinfo(title="this is an alert", message="whoa there chief")


help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="whoa", command=show_alert)

menu_bar.add_cascade(label="help", menu=help_menu)


"""
file dialogs
"""

def file_picker():
    choosen_file = tkFileDialog.askopenfile()

open_file = Menu(gui, tearoff=0)
open_file.add_command(label="open file", command=file_picker)

menu_bar.add_cascade(label="open", menu=open_file)

"""
radio buttons
"""
# global num variable to store the radio selection value as an int
# using multiple variables allows sets of radios to work together
num = IntVar()

# the value specifies the index of the button
Radiobutton(gui, text="choice 1", variable=num, value=1).grid(row=4, column=4)
Radiobutton(gui, text="choice 2", variable=num, value=2).grid(row=5, column=4)

"""
check boxes
"""
check = IntVar()

# ACTIVE / DISABLED determines is something is interactable
Checkbutton(gui, state=ACTIVE, variable=check, onvalue="1", offvalue="0")

"""
spinboxes
"""

selection_box = Spinbox(gui, from_=0, to=10)
selection_box.grid(row=1, column=0)

"""
main function
"""

def main():
    gui.mainloop()

if __name__ == "__main__":
    main()

