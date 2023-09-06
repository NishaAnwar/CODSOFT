import tkinter as tk
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x380")
        self.root.title("Password Generator")

        self.title_var = tk.StringVar()
        self.title_label = tk.Label(self.root, textvariable=self.title_var,font=18)
        self.title_label.pack()
        self.title_var.set("Password Strength")

        self.choice = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.root, text="POOR",font=20, variable=self.choice,bg="Light Pink", value=1, command=self.select)
        self.radio1.pack(anchor=tk.CENTER)
        self.radio2 = tk.Radiobutton(self.root, text="AVERAGE",font=20, variable=self.choice,bg="Teal", value=2, command=self.select)
        self.radio2.pack(anchor=tk.CENTER)
        self.radio3 = tk.Radiobutton(self.root, text="ADVANCED",font=20, variable=self.choice,bg="Light Green", value=3, command=self.select)
        self.radio3.pack(anchor=tk.CENTER)

        self.label_choice = tk.Label(self.root)
        self.label_choice.pack()

        self.length_var = tk.StringVar()
        self.length_var.set("Password Length")
        self.length_title = tk.Label(self.root, textvariable=self.length_var,font=18)
        self.length_title.pack()

        self.value = tk.IntVar()
        self.spin_len = tk.Spinbox(self.root, from_=8, to=24, textvariable=self.value, width=20)
        self.spin_len.pack()

        self.passgen_button = tk.Button(self.root, text="Generate Password",font=25, bd=5,bg="Orange", height=2, command=self.call_back,
                                        pady=3)
        self.passgen_button.pack()

        self.isum = tk.Label(self.root, text="")
        self.isum.pack(side=tk.BOTTOM,anchor=tk.CENTER)
        self.isum.place(x=160,y=300)

        self.poor = string.ascii_lowercase + string.ascii_uppercase
        self.average = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.symbols = "$%#^&*(@!~!#$_<>?/\|,;:{][}+_*"
        self.advance = string.ascii_lowercase + string.ascii_uppercase + string.digits + self.symbols

    def select(self):
        self.label_choice.config(text=self.choice.get())

    def passgen(self):
        if self.choice.get() == 1:
            return "".join(random.sample(self.poor, self.value.get()))
        elif self.choice.get() == 2:
            return "".join(random.sample(self.average, self.value.get()))
        elif self.choice.get() == 3:
            return "".join(random.sample(self.advance, self.value.get()))

    def call_back(self):
        self.isum.config(text=self.passgen(),bg="Lavender",font=22)



if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
