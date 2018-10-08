from tkinter import *
root = Tk()
#creating a label name
label_1 = Label(root, text="NAME:")

#creating a label password

label_2 = Label(root, text="PASSWORD")
#creating a button to log in
button =Button(root, text="Log In")
entry_1 = Entry(root)
entry_2 = Entry(root)

# placing the labels and button in the window using grid
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
button.grid(row = 2, column = 1)
#creating a checkbox to ask user whether he want to keep logged in or not
check=Checkbutton(root, text="Keep me Logged in")
check.grid(columnspan= 2)


root.mainloop()