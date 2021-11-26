#project name:- event management system
#project by:- Vishal Baliram Kharche
#             Roshani Rahul Kharche


from tkinter import *
import tkinter.messagebox as message
import mysql.connector
from PIL import ImageTk,Image
#import mysql.connector



def login_verify():
    
    username1 = user.get()
    password1 = passw.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    
    if username1 == 'vishal':
        if password1 == '123456':
            enter_data()
            
 
        else:
            password_not_recognised()
            
 
    else:
        user_not_found()
        

def password_not_recognised():
    
    password_not_recog_screen = Toplevel(root)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("180x120")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",cursor='hand2', command=password_not_recog_screen.destroy).pack()


 
def user_not_found():
    
    user_not_found_screen = Toplevel(root)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("180x120")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",cursor='hand2',command=user_not_found_screen.destroy).place(x=70,y=50,width=50,height=20)



def getvalues():
    cname=username.get()
    caddress=useraddress.get()
    cmobileno=usermobileno.get()
    cfsd=userfunctionsd.get()
    cfed=userfunctioned.get()
    clocation=userlocation.get()
        
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database='design_management')
    mydata=mydb.cursor()
    sql="INSERT INTO design_management VALUES(%s,%s,%s,%s,%s,%s)"
    val=(cname,caddress,cmobileno,cfsd,cfed,clocation)
    mydata.execute(sql,val)
    mydata.execute("commit")
    popup()
    mydb.close()

def popup():
    global pop
    pop=Toplevel(loginscreen)
    pop.geometry('180x120')
    Label(pop, text="Insert Sucessfully").pack()
    Button(pop, text="OK",cursor='hand2', command=exit3).pack()

def reset_data():
    entryname.delete(0,END)
    entryaddress.delete(0,END)
    entrymobileno.delete(0,END)
    entryfunctionsd.delete(0,END)
    entryfunctioned.delete(0,END)
    entrylocation.delete(0,END)
    

def afterdata():
    
    global loginscreen
    #loginscreen=Tk()
    loginscreen=Toplevel(data)
    loginscreen.geometry('1000x600')
    loginscreen.resizable(False,False)
    loginscreen.title('WELCOME TO DIPAK TENT HOUSE')

    imag=Image.open('image/decore1.jpeg')
    photo=ImageTk.PhotoImage(imag)
    bgimage=Label(loginscreen,image=photo).place(x=0,y=0,relwidth=1,relheight=1)

    f1=Frame(loginscreen, borderwidth=8,width=850,height=390, bg="white", relief=SUNKEN)
    f1.place(x=20,y=40)
    
    Label(f1,text='WELCOME TO DIPAK TENT HOUSE',font='algerian 20 bold',bg="white",fg='coral').place(x=220,y=20)
    name=Label(f1,text='Name',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=60)
    address=Label(f1,text='Address',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=100)
    mobileno=Label(f1,text='Mobile No',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=140)
    functionstartdate=Label(f1,text='Function start date',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=180)
    functionenddate=Label(f1,text='Function end date',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=220)
    location=Label(f1,text='Loaction of function',fg="coral4",bg="white",font=('Times New Roman',15)).place(x=20,y=260)
    global username
    global useraddress
    global usermobileno
    global userfunctioned
    global userfunctionsd
    global userlocation
    
    username=StringVar()
    useraddress=StringVar()
    usermobileno=StringVar()
    userfunctioned=StringVar()
    userfunctionsd=StringVar()
    userlocation=StringVar()

    global entryname
    global entryaddress
    global entrymobileno
    global entryfunctionsd
    global entryfunctioned
    global entrylocation


    entryname=Entry(f1,textvariable=username,bg='gray86')
    entryname.place(x=320,y=60,width=250,height=25)
    entryaddress=Entry(f1,textvariable=useraddress,bg='gray86')
    entryaddress.place(x=320,y=100,width=250,height=25)
    entrymobileno=Entry(f1,textvariable=usermobileno,bg='gray86')
    entrymobileno.place(x=320,y=140,width=250,height=25)
    entryfunctionsd=Entry(f1,textvariable=userfunctionsd,bg='gray86')
    entryfunctionsd.place(x=320,y=180,width=250,height=25)
    entryfunctioned=Entry(f1,textvariable=userfunctioned,bg='gray86')
    entryfunctioned.place(x=320,y=220,width=250,height=25)
    entrylocation=Entry(f1,textvariable=userlocation,bg='gray86')
    entrylocation.place(x=320,y=260,width=250,height=25)


    Button(f1,text='Submit',cursor='hand2',bg='coral',fg='white',command=getvalues).place(x=320,y=300,width=100,height=25)
    Button(f1,text='Exit',cursor='hand2',bg='coral',fg='white',command=exit1).place(x=370,y=340,width=100,height=25)
    Button(f1,text='Reset',cursor='hand2',bg='coral',fg='white',command=reset_data).place(x=420,y=300,width=100,height=25)
    
    loginscreen.mainloop()


def login():
    
    global user
    global passw
    global username_login_entry
    global password_login_entry
    
    global root
    root=Tk()
    root.title('Login page')
    root.geometry('1200x600')
    imag=Image.open('image/decore.jpg')
    photo=ImageTk.PhotoImage(imag)
    bgimage=Label(root,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
    frame1=Frame(root,bg="white", relief=SUNKEN)
    frame1.place(x=150,y=150,width=400,height=340)
    
    user=StringVar()
    passw=StringVar()
    content=Label(frame1,text='Login here',bg='white',fg='SteelBlue1',font=('david',32,'bold')).place(x=90,y=30)
    Label(frame1, text="Username",bg='white',font=('cambria',15)).place(x=90,y=100)
    username_login_entry = Entry(frame1, textvariable=user,bg='gray82')
    username_login_entry.place(x=90,y=140,width=200,height=25)
   
    Label(frame1, text="Password",bg='white',font=('cambria',15)).place(x=90,y=180)
    password_login_entry = Entry(frame1, bg='gray82',textvariable=passw, show= '*')
    password_login_entry.place(x=90,y=220,width=200,height=25)
    
    Button(root, text="Login",fg='white',bg='SteelBlue1',font=('Times New Roman',15),cursor='hand2',command=login_verify).place(x=290,y=420,width=90,height=40)
    root.mainloop()

def enter_data():
    global data
    data=Toplevel(root)
    #data=Tk()
    data.geometry('1000x600')
    data.resizable(False,False)
    data.title('option')
    imag=Image.open('image/8.jpeg')
    photo=ImageTk.PhotoImage(imag)
    bgimage=Label(data,image=photo).place(x=0,y=0,relwidth=1,relheight=1)
#anchor = n, ne, e, se, s, sw, w, nw, or center
    #content=Label(data,text='Welcome To Dipak Tent House',bg="white",fg='red',font='algerian 20 bold').pack()
    f1 = Frame(data, borderwidth=8,width=160,height=200 ,bg="white", relief=SUNKEN)
    f1.place(x=90,y=90,width=380,height=320)


    Button(f1,text='Enter Customer Data',font=('Times New Roman',15),fg='white',bg='SteelBlue1',cursor='hand2',command=afterdata,).place(x=70,y=70,width=220,height=40)
    Button(f1,text='Calculate stage rent',font=('Times New Roman',15),fg='white',bg='SteelBlue1',cursor='hand2',command=cstagerent).place(x=72,y=140,width=220,height=40)
    Button(f1,text='Exit',font=('Times New Roman',15),fg='white',bg='SteelBlue1',cursor='hand2',command=exit2).place(x=120,y=220,width=110,height=40)
    data.mainloop()


def cstagerent():
    global stagerent
    #stagerent=Tk()
    stagerent=Toplevel(data)
    stagerent.geometry('874x420')
    stagerent.resizable(False,False)
    stagerent.title('Stage')

    content=Label(stagerent,text='We have the following stages',fg='brown',font='cambria 15 bold').pack()
    f1=Frame(stagerent, borderwidth=8,width=850,height=390, bg="SteelBlue1", relief=SUNKEN)
    f1.place(x=10,y=40)
    ms=Label(f1,text='Marriage Stage',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=15,y=50)
    hs=Label(f1,text='Haldi Stage',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=15,y=90)
    es=Label(f1,text='Engagement Stage',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=15,y=130)
    bs=Label(f1,text='Birthday Stage',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=15,y=170)
    a=Label(f1,text='For How Many Days Did You',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=400,y=10)
    p=Label(f1,text='Enter price',fg='black',bg='SteelBlue1',font=('arial',13,'bold')).place(x=250,y=10)
   
    total=Button(f1,text='Total price',bg='orange',cursor='hand2',command=total_price).place(x=240,y=220,width=90,height=30)
    exitb=Button(f1,text='Exit',width=20,bg='orange',cursor='hand2',command=exit).place(x=300,y=290)
    
    global p1
    global p2
    global p3
    global p4
    global d1
    global d2
    global d3
    global d4
    global text_input
    p1=StringVar()
    p2=StringVar()
    p3=StringVar()
    p4=StringVar()
    d1=StringVar()
    d2=StringVar()
    d3=StringVar()
    d4=StringVar()
    text_input=StringVar()
    totalp=Entry(f1,textvariable=text_input,fg='green',font='cambria 10 bold').place(x=430,y=224)
    ms_price=Entry(f1,textvariable=p1).place(x=235,y=50)
    hs_price=Entry(f1,textvariable=p2).place(x=235,y=90)
    es_price=Entry(f1,textvariable=p3).place(x=235,y=130)
    bs_price=Entry(f1,textvariable=p4).place(x=235,y=170)
    ms_entry=Entry(f1,textvariable=d1).place(x=450,y=50)
    hs_entry=Entry(f1,textvariable=d2).place(x=450,y=90)
    es_entry=Entry(f1,textvariable=d3).place(x=450,y=130)
    bs_entry=Entry(f1,textvariable=d4).place(x=450,y=170)
    stagerent.mainloop()
def total_price():
    t1=eval(p1.get())
    t2=eval(p2.get())
    t3=eval(p3.get())
    t4=eval(p4.get())
    t5=eval(d1.get())
    t6=eval(d2.get())
    t7=eval(d3.get())
    t8=eval(d4.get())
    totalpr=((t1*t5)+(t2*t6)+(t3*t7)+(t4*t8))
    text_input.set(totalpr)

def exit():
    stagerent.destroy()
def exit1():
    loginscreen.destroy()
def exit2():
    data.destroy()

def exit3():
    pop.destroy()



login()
