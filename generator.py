
'''
Writen by - Jordan Swebeck
'''


from tkinter import *
import random
from passlib.hash import pbkdf2_sha256

class main():
    secLevel = []
    passwd = ""

# password generator
def submit():
    password = entry.get()

    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v''w', 'x', 'y', 'z', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%']
    iconList = ['!', '@', '#', '$', '%']

# generator loop
    for char in main.secLevel:
        p = random.choice(iconList)
        p += password
        password = p
        password += str(random.randint(1, 9))
        password += random.choice(charList)
    text = StringVar()
    text.set(password)
    password += random.choice(iconList)
    main.passwd = pbkdf2_sha256.hash(password)

# result
    myEntry = Entry(window, bd=0,
                    font=("Arial", 12),
                    state="readonly",
                    textvariable=text)
    myEntry.pack()

# level of security
def order():
    if x.get() == 0:
        main.secLevel = []
    elif x.get() == 1:
        main.secLevel = [1, 2]
    elif x.get() == 2:
        main.secLevel = [1, 2, 3]
    elif x.get() == 3:
        main.secLevel = [1, 2, 3, 4, 5, 6]
    else:
        print("huh?")

def Hash():
    text2 = StringVar()
    text2.set(main.passwd)
    myEntry2 = Entry(window, bd=0,
                     font=("Arial", 12),
                     state="readonly",
                     textvariable=text2)
    myEntry2.pack()

# start window
window = Tk()
window.title("Password Generator")
label = Label(window, text="Type the keyword you'd like \nto make a password.", font=('Times New Roman', 18))
label.pack()

entry = Entry(window,
              font=('Times New Roman', 20),
              fg='black')
entry.pack(anchor=W)

submitButton = Button(window, text="Submit", command=submit)
submitButton.pack(anchor=N)

strengh = ['None', 'Weak', 'Mid', 'Strong']
x = IntVar()
for index in range(len(strengh)):
    radiobutton = Radiobutton(window,
                              text=strengh[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=("Helvetica", 12, 'bold', 'italic'),
                              width=4,
                              command=order
                              )
    radiobutton.pack(anchor=N)
hashButton = Button(window, text="Hash", command=Hash)
hashButton.pack(anchor=S)
window.mainloop()
