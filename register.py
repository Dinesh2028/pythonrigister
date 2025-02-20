from tkinter import*

root = Tk()
root.title("Registering")
root.geometry("680x470")
root.resizable(False, False)

def register():
    print("Register")

Label(root, text="Python Registering Form", font="arial 25").pack(pady=50)

Label(text="Name", font=23).place(x=100, y=150)
Label(text="Phone", font=23).place(x=100, y=200)
Label(text="Gender", font=23).place(x=100, y=250)
Label(text="Email", font=23).place(x=100, y=320)  

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emailValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
phoneEntry = Entry(root, textvariable=phoneValue, width=30, bd=2, font=20)
emailEntry = Entry(root, textvariable=emailValue, width=30, bd=2, font=20)

nameEntry.place(x=200, y=150)
phoneEntry.place(x=200, y=200)
emailEntry.place(x=200, y=320)  

# Adding the RadioButtons for gender
genderValue.set("Male")  # Default value
genderMale = Radiobutton(root, text="Male", variable=genderValue, value="Male", font=20)
genderFemale = Radiobutton(root, text="Female", variable=genderValue, value="Female", font=20)

genderMale.place(x=200, y=250)
genderFemale.place(x=200, y=280)

checkValue = IntVar
checkbtn = Checkbutton(text="Remember me?", variable=checkValue)
checkbtn.place(x=200, y=370)  # Adjusted for spacing

Button(text="register", font=20, width=11, height=2, command=register).place(x=250, y=410)

root.mainloop()

