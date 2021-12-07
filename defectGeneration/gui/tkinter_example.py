import tkinter as tk

class Application(tk.Frame):
    def __init__(self):
        # Initialize toplevel tkinter widget
        self.master = tk.Tk()
        super().__init__(self.master)

        # Set window properties
        self.master.title("Defect Generation")
        self.master.geometry("1920x1080")

        self.master.grid_columnconfigure(0, weight=4)
        self.master.grid_columnconfigure(1, weight=5)
        self.master.grid_rowconfigure(0, weight=1)

        self.frame_left = tk.Frame(self.master, bg="red")
        self.frame_left.grid(row=0, column=0, sticky="nesw")
        self.frame_right = tk.Frame(self.master, bg="green")
        self.frame_right.grid(row=0, column=1, sticky="nesw")

        self.frame_left.grid_columnconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(0, weight=1)

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=1)


        self.image = tk.PhotoImage(file="./output/png/large_particle1.png")
        self.image_label = tk.Label(self.frame_right, image=self.image)
        self.image_label.grid(row=0, column=0, sticky="nesw")

        self.label1 = tk.Label(self.frame_left, text="Layer")
        self.label2 = tk.Label(self.frame_left, text="Size mean")
        self.label3 = tk.Label(self.frame_left, text="Size stddev")
        self.entry1 = tk.Entry(self.frame_left, width=30)
        self.entry2 = tk.Entry(self.frame_left)
        self.entry3 = tk.Entry(self.frame_left)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1, sticky="w")
        self.label2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1, sticky="ew")
        self.label3.grid(row=2, column=0)
        self.entry3.grid(row=2, column=1, sticky="ew")


    def main_loop(self):
        self.window.mainloop()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.window.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


app = Application()
app.mainloop()