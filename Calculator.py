from tkinter import *

#setting

root = Tk()
root.geometry("400x200")
root.title("Calculator")
root.resizable(width= False, height= False)
color = "gray"
root.configure(bg= color)


#frames

top_first = Frame(root, width= 400, height= 50, bg= color)
top_first.pack(side= TOP)

top_second = Frame(root, width= 400, height= 50, bg= color)
top_second.pack(side= TOP)

top_third = Frame(root, width= 400, height= 50, bg= color)
top_third.pack(side= TOP)

top_forth = Frame(root, width= 400, height= 50, bg= color)
top_forth.pack(side= TOP)


# buttons

btn_plus = Button(top_third, text= "+", width= 10,  highlightbackground=color)
btn_plus.pack(side= LEFT, padx= 10, pady= 10)

btn_minus = Button(top_third, text= "-", width= 10, highlightbackground=color)
btn_minus.pack(side= LEFT, padx= 10, pady= 10)

btn_mul = Button(top_third, text= "x", width= 10,highlightbackground=color)
btn_mul.pack(side= LEFT, padx= 10, pady= 10)

btn_div = Button(top_third, text= "/", width= 10,highlightbackground=color)
btn_div.pack(side= LEFT, padx= 10, pady= 10)


# entries and labels

label_first_num = Label(top_first, text= "input number 1 : ", bg= color)
label_first_num.pack(side= LEFT, padx= 10, pady= 10)

first_num = Entry(top_first, highlightbackground= color)
first_num.pack(side= LEFT)

label_second_num = Label(top_second, text= "input number 2 : ", bg= color)
label_second_num.pack(side= LEFT, padx= 10, pady= 10)

second_num = Entry(top_second, highlightbackground= color)
second_num.pack(side= LEFT)

res = Label(top_forth, text= "Result", bg= color)
res.pack(side= LEFT, padx= 10, pady= 10)

res_num = Entry(top_forth, highlightbackground= color)
res_num.pack(side= LEFT)


root.mainloop()
