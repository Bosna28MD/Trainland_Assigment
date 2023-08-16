import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
#from tkinter.messagebox import showinfo






def Register(conn):
    root=tk.Tk();

    root.geometry("300x250");

    frame1=tk.Frame(root);

    frame1.columnconfigure(index=0,weight=1);
    frame1.columnconfigure(index=1,weight=3);

    username_var=tk.StringVar();
    age_var=tk.StringVar();
    pwd_var=tk.StringVar();

    lbl_title=tk.Label(frame1,text="Register",font=("Arial",18));
    lbl_title.grid(row=0,column=1);

    lbl_username=tk.Label(frame1,text="UserName:");
    lbl_age=tk.Label(frame1,text="Age:");
    lbl_pwd=tk.Label(frame1,text="Password:");

    lbl_username.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5);
    lbl_age.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)
    lbl_pwd.grid(row=3,column=0,sticky=tk.W,padx=5,pady=5);

    txt_user=tk.Entry(frame1,textvariable=username_var);
    txt_age=tk.Entry(frame1,textvariable=age_var);
    txt_pwd=tk.Entry(frame1,textvariable=pwd_var,show="*");

    txt_user.grid(row=1,column=1);
    txt_age.grid(row=2,column=1);
    txt_pwd.grid(row=3,column=1);



    def Register_db():
        if(len(username_var.get())==0 or age_var.get()==0 or len(pwd_var.get())==0 ):
            messagebox.showwarning("Warning", "Fill All the Fields")
            return;
        if(not age_var.get().isnumeric()):
            messagebox.showwarning("Warning", "Insert a number in Age-field")
            return;
        cursor_db=connection.cursor();
        cursor_db.execute(f"Select * from user_tabel where username='{username_var.get()}'");
        if(len(cursor_db.fetchall())>0):
            messagebox.showwarning("Warning","This user already exist");
            return;
        user_data=(username_var.get(),age_var.get(),pwd_var.get());
        cursor_db.execute(f"INSERT into user_tabel(username,age,pwd) values('{username_var.get()}','{age_var.get()}','{pwd_var.get()}') ");
        connection.commit();
        if(cursor_db.rowcount>0):
            messagebox.showinfo("showinfo", "User created")
        #print(cursor_db.fetchall())
        """ print(username_var.get())
        print(age_var.get())
        print(pwd_var.get()) """
    
    btn_register=tk.Button(frame1,text="Register",command=Register_db);
    btn_register.grid(row=4,column=1);

    def func_gotoLogIn():
        root.destroy();
        Log_IN(conn=conn);

    btn_gotoLOgIn=tk.Button(frame1,text="Go to LogIN",command=func_gotoLogIn);
    btn_gotoLOgIn.grid(row=5,column=1);

    frame1.pack();

    root.mainloop();








def Log_IN(conn):
    root=tk.Tk();
    root.geometry("300x200");
    root.title("LogIn")

    frame1=tk.Frame(root);
    
    frame1.columnconfigure(index=0,weight=1);
    frame1.columnconfigure(index=1,weight=3);


    """ root.rowconfigure(index=0,weight=1);
    root.rowconfigure(index=1,weight=1); """

    username_var=tk.StringVar();
    pwd_var=tk.StringVar();

    lbl_title=tk.Label(frame1,text="LogIn",font=("Arial",18));
    lbl_title.grid(row=0,column=1,padx=5,pady=5,sticky="nsew");

    lbl_username=tk.Label(frame1,text="UserName:");
    lbl_pwd=tk.Label(frame1,text="Password:");

    lbl_username.grid(row=1,column=0,padx=5,pady=5);
    lbl_pwd.grid(row=2,column=0,padx=5,pady=5);



    txt_user=tk.Entry(frame1,textvariable=username_var);
    txt_pwd=tk.Entry(frame1,textvariable=pwd_var,show="*");

    txt_user.grid(row=1,column=1)
    txt_pwd.grid(row=2,column=1)

    def LogIn_Db():
        """ print(username_var.get());
        print(pwd_var.get()) """
        if(len(username_var.get())==0 or len(pwd_var.get())==0 ):
            messagebox.showwarning("Warning", "Fill All the Fields")
            return;
        cursor_db=connection.cursor();
        cursor_db.execute(f"Select * from user_tabel where username='{username_var.get()}'");
        user_data=cursor_db.fetchall()
        if(len(user_data)==0):
            messagebox.showwarning("Warning","This user doesn't exist");
            return;
        if(user_data[0][3]!=pwd_var.get()):
            messagebox.showwarning("Warning","Incorrect password");
            return;
        global USER
        USER=[user_data[0][0],username_var.get().capitalize()];
        root.destroy();
        User_Menu(conn=conn);



    btn_login=tk.Button(frame1,text="LogIN",command=LogIn_Db);
    btn_login.grid(row=3,column=1);


    def func_gotoRegister():
        root.destroy();
        Register(conn=conn);

    btn_register=tk.Button(frame1,text="Create Cont",command=func_gotoRegister);
    btn_register.grid(row=4,column=1)

    frame1.pack(pady=10);
    root.mainloop();


def User_Menu(conn):
    root=tk.Tk();
    root.title("User Menu")
    root.geometry("700x500")

    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1);
    root.columnconfigure(2,weight=1);

    lbl_title=tk.Label(root,text="UserName:"+USER[1]);
    lbl_title.grid(row=0,column=1);

    def func_logout():
        global USER
        USER=[];
        root.destroy()
        Log_IN(conn=conn);


    btn_logout=tk.Button(root,text="LogOut",command=func_logout);
    btn_logout.grid(row=0,column=2,sticky=tk.E);


    root.mainloop();


if __name__=="__main__":
    USER=[];
    try:
        connection=mysql.connector.connect(
        host='localhost',
        database='db_python1',
        user="root",
        password="root");
        Log_IN(conn=connection);
    except Error as e:
        print("Error DataBase: ",e);    

#Log_IN();
#Register()
#User_Menu()