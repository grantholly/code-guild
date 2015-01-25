from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.center_window()

    def center_window(self):
        width = 290
        height = 150
        # figure out the device screen size
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        # calculate the midpoints
        x = (screen_width - width) / 2
        y = (screen_height - height) / 2
        # set the window in a centered fashion
        self.parent.geometry("%dx%d+%d+%d" % (width, height, x, y))        

    def initUI(self):
        self.parent.title("window")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        # use hte OS theme for the window
        self.style.theme_use("default")
        # add quit button instance
        quit_button = Button(self, text="quit here", command=self.quit)
        # position button absolutely in window
        quit_button.place(x=100, y=100)

def main():
    root = Tk()
    root.geometry("300x300+100+100")
    # create an instance of our window
    app = Example(root)
    # the main loop is running in the background
    # this will listen for events inside the window
    # this will also dispatch event handers
    root.mainloop()

if __name__ == '__main__':
    main()


