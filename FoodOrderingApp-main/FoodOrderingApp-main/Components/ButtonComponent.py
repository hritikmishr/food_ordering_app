from tkinter import *

class GrayButton(Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(parent, text=text, width=20, height=2, activebackground="gray", activeforeground="white",
                         command=command)
        self.configure(**kwargs)

class WhiteButton(Button):
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(parent, text=text, width=25, height=2, bg="white", fg="black", activebackground="gray",
                         command=command)
        self.configure(**kwargs)

if __name__ == '__main__':
    root= Tk()

    g = GrayButton(root, "Gray button",command="")
    g.pack(padx=10,pady=10)

    w = WhiteButton(root, "White button",command="")
    w.pack(padx=10,pady=10)

    root.mainloop()
