from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("window")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1) 
        frame.pack(fill=BOTH, expand=1)

        self.pack(fill=BOTH, expand=1)
    
        # make two buttons that don't do anything yet
        # set the butons using a style manager class
        close_button = Button(self, text="Close")
        # add 5px of padding on the x and y
        # set the buttons on the RIGHT side
        close_button.pack(side=RIGHT, padx=5, pady=5)
        ok_button = Button(self, text="OK")
        ok_button.pack(side=RIGHT)

def main():
    root = Tk()
    root.geometry("300x300+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == "__main__":
    main()

