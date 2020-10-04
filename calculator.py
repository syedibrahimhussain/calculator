from tkinter import *





if __name__=="__main__":
    #creating TK
    top = Tk()
    top.title("Calculator")
    ans=None

    # creating Entry
    e=Entry(top, width=45, bd=50, borderwidth=15)
    e.grid(row=0, column=0, columnspan=5)

    #Method to display button text when clicked
    def button_method(num):
        curr=e.get()
        e.delete(0,END)
        e.insert(0,str(curr)+str(num))
  
    #Method to display the previous calculated Answer
    def button_Ans():
        index=len(e.get())
        e.insert(index,str(ans))

    #Method to clear the screen
    def AC():
        e.delete(0,END)        

    #method to del the digit
    def button_del():
        e.delete(len(e.get())-1)


    #Method to add numbers
    def button_add():
        curr=e.get()
        e.delete(0,END)
        e.insert(0,str(curr)+"+")

    #Method to subtract numbers
    def button_sub():
        curr=e.get()
        e.delete(0,END)
        e.insert(0,str(curr)+"-") 

    #Method to multiply numbers
    def button_mul():
        curr=e.get()
        e.delete(0,END)
        e.insert(0,str(curr)+"*") 

    ##Method to divide numbers
    def button_div():
        curr=e.get()
        e.delete(0,END)
        e.insert(0,str(curr)+"/")

    #method to calculate the input and display the calculated result.
    def button_eql():
        curr=e.get()
        e.delete(0,END)
        cal=eval(curr)
        e.insert(0,str(cal))
        global ans
        ans=cal
          

    button_7 = Button(top, text="7",  padx="22", pady="15",activebackground= "gray75" ,  command=lambda :button_method("7"))
    button_7.grid(row=1,column=0)

    button_8 = Button(top, text="8",   padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("8"))
    button_8.grid(row=1,column=1)

    button_9 = Button(top, text="9",   padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("9"))
    button_9.grid(row=1,column=2)

    button_del = Button(top, text="Del",  padx="20", pady="15",activebackground= "gray75", command=button_del)
    button_del.grid(row=1,column=3)

    button_ac = Button(top, text="AC", padx="20", pady="15",activebackground= "gray75", command=AC)
    button_ac.grid(row=1,column=4)


    button_4 = Button(top, text="4",  padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("4"))
    button_4.grid(row=2,column=0)

    button_5 = Button(top, text="5",   padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("5"))
    button_5.grid(row=2,column=1)

    button_6 = Button(top, text="6",   padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("6"))
    button_6.grid(row=2,column=2)

    button_x= Button(top, text="X",   padx="25", pady="15",activebackground= "gray75", command=button_mul)
    button_x.grid(row=2,column=3)

    button_div= Button(top, text="/",   padx="23", pady="15",activebackground= "gray75", command=button_div)
    button_div.grid(row=2,column=4)

    button_1 = Button(top, text="1",   padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("1"))
    button_1.grid(row=3,column=0)

    button_2 = Button(top, text="2",  padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("2"))
    button_2.grid(row=3,column=1)

    button_3 = Button(top, text="3",  padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("3"))
    button_3.grid(row=3,column=2)

    button_add= Button(top, text="+",  padx="25", pady="15",activebackground= "gray75", command=button_add)
    button_add.grid(row=3,column=3)

    button_sub= Button(top, text="-",  padx="23", pady="15",activebackground= "gray75", command=button_sub)
    button_sub.grid(row=3,column=4)

    button_0 = Button(top, text="0",  padx="22", pady="15",activebackground= "gray75", command=lambda :button_method("0"))
    button_0.grid(row=4,column=0)

    button_dot = Button(top, text=".",  padx="23", pady="15",activebackground= "gray75", command=lambda :button_method("."))
    button_dot.grid(row=4,column=1)

    button_x10 = Button(top, text="X10",  padx="15", pady="15",activebackground= "gray75", command=lambda :button_method("7"))
    button_x10.grid(row=4,column=2)

    button_Ans= Button(top, text="Ans",   padx="18", pady="15",activebackground= "gray75", command=button_Ans)
    button_Ans.grid(row=4,column=3)

    button_eql= Button(top, text="=",  padx="22", pady="15",activebackground= "gray75", command=button_eql)
    button_eql.grid(row=4,column=4)

    top.mainloop()

