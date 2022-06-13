from tkinter import Tk, Label

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Image viewer app")
        self.resizable(0, 0)

        self.hello_label = Label(text="Hello world")
        self.hello_label.pack()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
        