
import tkinter as tk
LIGHT_GRAY="#DDDDDD"
LABEL_COLOUR="#25265E"
WHITE="#FFFFFF"
FONT_A=("Arial",16)
FONT_B=("Arial",40,"bold")
DIGIT_FONT_STYLE=("Arial",24,"bold")
DEFALUT_FONT_STYLE=("Arial",20)
OFF_WHITE="#F8FAFF"
LIGHT_BLUE="#CCEDEF"


class Calculator:
    def __init__(self):

        self.root=tk.Tk()
        self.root.geometry("375x667")
        self.root.resizable(False,False)
        self.root.title("Calculator")
        self.total_value=""
        self.current_value=""
        self.display_frame=self.first_frame()
        self.button_frame=self.second_frame()
        self.Total_Label, self.Current_Label=self.Display_Labels()
        #self.Current_Label=self.Display_Labels()


        self.digits={7:(1,1),8:(1,2),9:(1,3),
                     4: (2, 1), 5: (2, 2), 6: (2, 3),
                     1: (3, 1), 2: (3, 2), 3: (3, 3),
                     0:(4,2),".":(4,1)
                     }
        self.Buttons()

        self.Operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.Oeprator_Buttons()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.clear_button()
        self.equal_button()
        self.square_button()
        self.square_root_button()
        self.bind_keys()
                                      ##################FRAMES#########################
    def first_frame(self):
        frame=tk.Frame(self.root,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame




    def second_frame(self):
        frame=tk.Frame(self.root)
        frame.pack(expand=True,fill="both")
        return frame


                                     #######################LABELS#######################

    def Display_Labels(self):
        Total_Label=tk.Label(self.display_frame,text=self.total_value,anchor=tk.E,bg=LIGHT_GRAY,fg=LABEL_COLOUR,padx=24,font=FONT_A)
        Total_Label.pack(expand=True,fill="both")

        Current_Label = tk.Label(self.display_frame, text=self.current_value, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOUR,
                               padx=24, font=FONT_B)
        Current_Label.pack(expand=True, fill="both")
        return Total_Label,Current_Label
                                   ######################## DIGIT BUTTONS#########################

    def Buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.button_frame,text=str(digit),bg=WHITE,fg=LABEL_COLOUR,font=DIGIT_FONT_STYLE,borderwidth=0,command=lambda x=digit:self.adding_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


                                  ########################OPERATOR BUTTONS#################

    def Oeprator_Buttons(self):
        i=0
        for operator,symbol in self.Operations.items():
             Button_Operators=tk.Button(self.button_frame,text=symbol,bg=OFF_WHITE,fg=LABEL_COLOUR,font=DEFALUT_FONT_STYLE,borderwidth=0,command=lambda x=operator:self.append_operators(x))

             Button_Operators.grid(row=i,column=4,sticky=tk.NSEW)

             i+=1

    def append_operators(self,operators):
        self.current_value+=operators
        self.total_value+=self.current_value
        self.current_value=""
        self.update_current_label()
        self.update_total_value()




    def clear(self):
        self.current_value=""
        self.total_value=""
        self.update_total_value()
        self.update_current_label()

    def clear_button(self):
        Button_Operators = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOUR,
                                     font=DEFALUT_FONT_STYLE, borderwidth=0,command=self.clear)

        Button_Operators.grid(row=0, column=1, sticky=tk.NSEW)




    def square(self):
        self.current_value=str(eval(f"{self.current_value}**2"))
        self.update_current_label()

    def square_button(self):
        Button_Operators = tk.Button(self.button_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOUR,
                                     font=DEFALUT_FONT_STYLE, borderwidth=0,command=self.square)

        Button_Operators.grid(row=0, column=2, sticky=tk.NSEW)





    def square_root(self):
        self.current_value = str(eval(f"{self.current_value}**0.5"))
        self.update_current_label()

    def square_root_button(self):
        Button_Operators = tk.Button(self.button_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOUR,
                                     font=DEFALUT_FONT_STYLE, borderwidth=0, command=self.square_root)

        Button_Operators.grid(row=0, column=3, sticky=tk.NSEW)




    def evaluate(self):
        self.total_value+=self.current_value
        self.update_total_value()
        try:
            self.current_value=str(eval(self.total_value))
            self.total_value=""
        except Exception as e:
            self.current_value="ERROR"
        finally:
            self.update_current_label()

    def equal_button(self):
        Button_Operators = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOUR,
                                     font=DEFALUT_FONT_STYLE, borderwidth=0,command=self.evaluate)

        Button_Operators.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)
                              #####################Functionality of Buttons#####################


    def update_total_value(self):
        value=self.total_value
        for operator,symbol in self.Operations.items():
            value=value.replace(operator,f"{symbol}")
        self.Total_Label.config(text=value)



    def update_current_label(self):
        self.Current_Label.config(text=self.current_value[:11])


    def adding_expression(self,value):
        self.current_value+=str(value)
        self.update_current_label()



                                         ################# Special Keys ##########################

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())  # Fixed "<Reyurn>" to "<Return>"
        for key in self.digits:
            self.root.bind(key, lambda event, digit=key: self.adding_expression(digit))

        for key in self.Operations:
            self.root.bind(key, lambda event, operator=key: self.append_operators(operator))

    def run(self):
        self.root.mainloop()







if __name__ == "__main__":
      obj=Calculator()
      obj.run()