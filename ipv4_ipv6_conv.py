import tkinter as tk


HEIGHT=700
WIDTH=800

def main():

    interface=gui()
    #interface.runner()


def convert(v4):
    gui.converted(v4)


class gui():

    def __init__(self):

        self.root = tk.Tk()

        self.canvas = tk.Canvas(self.root,  height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        self.frame = tk.Frame(self.root, bg="#80c1ff", bd=5)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        self.entry = tk.Entry(self.frame, font=40, bg='green')
        self.entry.place(relwidth=0.65, relheight=1)

        self.button = tk.Button(self.frame, text="Convert", font=40, command=lambda: convert(self.entry.get()))
        self.button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        self.lower_frame=tk.Frame(self.root, bg='#80c1ff', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        self.label = tk.Label(self.lower_frame)
        self.label.place( relwidth=1, relheight=1)

        #self.label['text'] = "v4"

        self.root.mainloop()

    def converted(self, v4):
        self.lower_frame = tk.Frame(self.root, bg='#80c1ff', bd=10)
        self.lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        self.label = tk.Label(self.lower_frame, text=str(v4))
        self.label.place(relx=0.7, rely=0, relwidth=1, relheight=1)



main()




