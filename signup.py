from tkinter import *

from firebase import firebase
firebase1 = firebase.FirebaseApplication('https://adminstorage-b279e.firebaseio.com/')
firebase = firebase.FirebaseApplication('https://user-storage-b95c1.firebaseio.com/')   
def login():
        def ret():
                i=str(e4.get())
                print(i)
                name=str(e5.get())
                print(name)
                passw=str(e6.get())
                print(passw)
                def add():
                        print("Added")
                def update():
                        print("Updated")
                def view():
                        print("Viewed")
                j=i[:2]
                if j=='Ad':
                        NI=i+name
                        result=firebase1.get('/Records/'+NI,'Password')
                        print(result)
                        if result==passw:
                                root4=Tk()
                                btn2=StringVar()
                                root4.title("Admin Page")
                                f12=Frame(root4)
                                f12.pack()
                                l11=Label(f12,text="Choose the option ")
                                l11.pack(side=LEFT)
                                R3=Radiobutton(f12,text="Add The Product",value="add",variable=btn2,command=add)
                                R3.pack(anchor=E)
                                R4=Radiobutton(f12,text="Update The Product",value="update",variable=btn2,command=update)
                                R4.pack(anchor=E)
                                R5=Radiobutton(f12,text="View The Product",value="view",variable=btn2,command=view)
                                R5.pack(anchor=E)
                                root4.mainloop()
                        else:   
                                print("Wrong Credentials")
                elif j=="Us":
                        NI=i+name
                        print(NI)
                        result=firebase.get('/Records/'+NI,'Password')
                        print(result)
                        if result==passw:
                                root5=Tk()
                                root5.title("Welcome "+str(name))
                                root5.mainloop()
                        else:
                                print("Wrong password")
                        
        root=Tk()
        root.title("Login")
        f8=Frame(root)
        f8.pack()
        l8=Label(f8,text="Id: ")
        l8.pack(side=LEFT)
        e4=Entry(f8,text="")
        e4.pack(side=RIGHT)
        f9=Frame(root)
        f9.pack()
        l9=Label(f9,text="Name: ")
        l9.pack(side=LEFT)
        e5=Entry(f9,text="")
        e5.pack(side=RIGHT)
        f10=Frame(root)
        f10.pack()
        l10=Label(f10,text="Password: ")
        l10.pack(side=LEFT)
        e6=Entry(f10,text="")
        e6.pack(side=RIGHT)
        f11=Frame(root)
        f11.pack()
        b3=Button(f11,text="Submit", width=5,height=2,command=ret)
        b3.pack()


def signup():
        root1=Tk()
        btn1=StringVar()

        def create(event):
                def ret():
                        sel=btn1.get()
                        print(sel)
                        i=str(e1.get())
                        print(i)
                        name=str(e2.get())
                        print(name)
                        passw=str(e3.get())
                        print(passw)
                        em=str(e4.get())
                        print(em)
                        j=i[0:2]
                        print(j)
                        if j=='Ad':
                                NI=i+name
                                data={'Id':i,'Name':name,'Password':passw}
                                result=firebase1.put("/Records",NI,data)
                        elif j=='Us':
                                NI=i+name
                                data={'Id':i,'Name':name,'Password':passw}
                                result=firebase.put("/Records",NI,data)
                                
                f2=Frame(root1)
                f2.pack()
                l2=Label(f2,text="Id: ")
                l2.pack(side=LEFT)
                e1=Entry(f2,text="")
                e1.pack(side=RIGHT)
                if (btn1.get())=='admin':
                        l3=Label(f2,text="(Write your Id as Ad...)")
                        l3.pack(side=RIGHT)
                elif btn1.get()=='user':
                        l3=Label(f2,text="(Write your Id as Us...)")
                        l3.pack(side=RIGHT)
                f3=Frame(root1)
                f3.pack()
                l4=Label(f3,text="Name: ")
                l4.pack(side=LEFT)
                e2=Entry(f3,text="")
                e2.pack(side=RIGHT)
                f4=Frame(root1)
                f4.pack()
                l5=Label(f4,text="Password: ")
                l5.pack(side=LEFT)
                e3=Entry(f4,text="")
                e3.pack(side=RIGHT)
                f5=Frame(root1)
                f5.pack()
                l6=Label(f5,text="Email-id: ")
                l6.pack(side=LEFT)
                e4=Entry(f5,text="")
                e4.pack(side=RIGHT)
                f6=Frame(root1)
                f6.pack()
                b1=Button(f6,text="Submit", width=5,height=2,command=ret)
                b1.pack()
                f7=Frame(root1).pack()
        root1.title("Registeration")
        f1=Frame(root1)
        f1.pack()
        l1=Label(f1,text="Create Account as:")
        l1.pack(side=LEFT)
        R1=Radiobutton(f1,text="Admin",value="admin",variable=btn1)
        R1.pack(anchor = E)
        R2=Radiobutton(f1,text="User",value="user",variable=btn1)
        R2.pack(anchor = E)
        b1=Button(f1,text="Create")
        b1.pack()
        b1.bind("<Button-1>",create)
    
root3=Tk()
f12=Frame(root3)
l12=Label(text="Choose your option").pack()
b4=Button(text="Login",width=5,height=2,command=login)
b4.pack(anchor="center")
b5=Button(text="SignUp",width=5,height=2,command=signup).pack(anchor="center")
root3.mainloop()
