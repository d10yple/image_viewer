from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from glob import glob

class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Image viewer")
        self.resizable(0, 0)
        self.current_image_position = 0
        self.all_images = [img for img in glob('images/*.jpg') if img != 'images\\error.jpg']
        self.set_image(self.current_image_position)
        self.set_status_label()

        #widgets
        self.before_button = Button(text="<",command=lambda: self.change_image("<"),width=8,height=2)
        self.after_button = Button(text=">",command=lambda: self.change_image(">"),width=8,height=2)
        self.first_image_button = Button(text="<<",command=lambda: self.change_image("<<"),width=8,height=2)
        self.last_image_button = Button(text=">>",command=lambda: self.change_image(">>"),width=8,height=2)

        #place all widgets
        self.after_button.grid(row=1, column=2, padx=5, pady=5)
        self.before_button.grid(row=1, column=1, padx=5, pady=5)
        self.first_image_button.grid(row=1, column=0, padx=5, pady=5)
        self.last_image_button.grid(row=1, column=3, padx=5, pady=5)

    def set_status_label(self) -> None:
        """Setting the status of the viewer x of x images
        """
        self.status_label = Label(text=f"{self.current_image_position+1}/{len(self.all_images)}")
        self.status_label.grid(row=2, columnspan=4)

    def set_image(self, position: int) -> None:
        """Set the image to view it

        Args:
            position (int): position of the image in the image list
        """
        try:
            self.image = ImageTk.PhotoImage(Image.open(self.all_images[position]))
        except FileNotFoundError:
            self.image = ImageTk.PhotoImage(Image.open('images/error.jpg'))
        finally:
            self.label_image = Label(image=self.image)
            self.label_image.grid(row=0, columnspan=4)

    def change_image(self, to: str) -> None:
        """Change the image in terms of direction

        Args:
            to (str): < or > to simple slide, << or >> to go to the beginning or the last img
        """
        image_max_range = len(self.all_images)-1
        if to == ">" or to == "<":        
            wanted_image_position = self.current_image_position+1 if to == ">" else self.current_image_position-1

            if 0 <= wanted_image_position <= image_max_range:
                self.set_image(wanted_image_position)
                if to == ">":
                    self.current_image_position+=1
                else:
                    self.current_image_position-=1
        else:
            self.current_image_position = 0 if to == "<<" else image_max_range
            self.set_image(self.current_image_position)

        self.set_status_label()
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
        