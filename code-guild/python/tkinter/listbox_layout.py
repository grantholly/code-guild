from ttk import Frame, Label, Style
from Tkinter import Tk, BOTH, Listbox, StringVar, END


class Test(object):
    def __init__(self):
        self.name = "test"
        self.age = 28
        self.fav_color = "green"

test = Test()

data = ["one", 2, test.name, test.age, test.fav_color]


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Listbox") 
        
        self.pack(fill=BOTH, expand=1)

        # put our data in from our global data object
        lb = Listbox(self)
        for i in data:
            lb.insert(END, i)
            
        # add event listener with call back to show
        # when the list object is selected, show visual feedback
        lb.bind("<<ListboxSelect>>", self.onSelect)    
            
        # absolute positioning
        lb.place(x=20, y=20)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)        
        self.label.place(x=20, y=210)

    def onSelect(self, val):
      
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)   

        self.var.set(value)
         

def main():
  
    root = Tk()
    ex = Example(root)
    root.geometry("300x250+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  

