#changing the code won't make you a coder
import zipfile
from tkinter import *
from tkinter import messagebox

def tk():
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.geometry('250x170')
    root.title('SPIDER Cracker')
    root.configure(background='black')
    messagebox.showinfo("Credits", ''.join('All Rights Reserved To Bropocalypse Team'))
    form = LabelFrame(root, text="Set", font='calibri 9 italic', background='black', foreground='cyan')
    form.grid(row=1, columnspan=2, sticky='WE', \
    padx=5, pady=0, ipadx=120, ipady=65)
    l = Label(form, text=" ZIP Filename  :", font='calibri 10', background='black', foreground='white')
    l.place(x=10, y=10)
    l2 = Label(form, text="Password List :", font='calibri 10', background='black', foreground='white')
    l2.place(x=10, y=40)
    global e, e1, ee
    e = Entry(form, width=15)
    e.place(x=103, y=12)
    e1 = Entry(form, width=15)
    e1.place(x=103, y=42)
    b = Button(form, text='Start', font='calibri 10', background='black', foreground='white', command=main)
    b.place(x=100, y=80)
    ll = Label(root, text='Password Is :', font='calibri 10', background='black', foreground='white')
    ll.place(x=30, y=140)
    ee = Entry(root, width=15)
    ee.place(x=120, y=142)
    root.mainloop()

def main():
    pass_list = e1.get()
    zip_file = e.get()
    amine = zipfile.ZipFile(zip_file)
    psw = len(list(open(pass_list, "rb")))
    messagebox.showinfo("", ''.join('N° Of Passwords is : '+ str(psw)))
    if crack_password(pass_list, amine) == False:
        messagebox.showerror("", ''.join('Password Not Found !'))

def crack_password(pass_list, amine):
    with open(pass_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    amine.extractall(pwd=word)
                    ss = word.decode()
                    ee.insert(0, ss)
                    return True
                except:
                    continue
    return False

tk()
