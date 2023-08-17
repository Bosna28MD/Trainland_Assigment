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

    root.rowconfigure(0,weight=1);
    root.rowconfigure(1,weight=1);
    root.rowconfigure(2,weight=1);
    root.rowconfigure(3,weight=1);
    root.rowconfigure(4,weight=1);



    """ lbl_title=tk.Label(root,text="UserName: "+USER[1],font=("Arial",25));
    lbl_title.grid(row=0,column=1,sticky=tk.N); """
    lbl_inventory=tk.Label(root,text="Inventory Managment System",font=("Arial",23))
    lbl_inventory.grid(row=0,column=1,sticky=tk.N);

    lbl_title=tk.Label(root,text="UserName: "+USER[1],font=("Arial",21));
    lbl_title.grid(row=1,column=1,sticky=tk.N);

    def func_logout():
        global USER
        USER=[];
        root.destroy()
        Log_IN(conn=conn);


    btn_logout=tk.Button(root,text="LogOut",command=func_logout);
    btn_logout.grid(row=0,column=2,sticky=tk.NE);

    def btn_User_Table():
        root.destroy();
        User_Table(conn=conn);
    
    def btn_Customer_Table():
        root.destroy();
        Customer_Table(conn=conn);


    btn_user_view=tk.Button(root,text="User-View",font=("Arial",19),command=btn_User_Table);
    btn_user_view.grid(row=2,column=0,sticky=tk.N);

    btn_customer=tk.Button(root,text="Customers",font=("Arial",19),command=btn_Customer_Table);
    btn_customer.grid(row=2,column=2,sticky=tk.N);

    btn_products=tk.Button(root,text="Products",font=("Arial",19));
    btn_products.grid(row=3,column=0,sticky=tk.N);

    btn_orders=tk.Button(root,text="Orders",font=("Arial",19));
    btn_orders.grid(row=3,column=2,sticky=tk.N);


    root.mainloop();






def User_Table(conn):
    root=tk.Tk();
    root.title("User Table");
    root.geometry("700x500");

    root.columnconfigure(0,weight=1);
    root.columnconfigure(1,weight=1);
    root.columnconfigure(2,weight=1);

    root.rowconfigure(0,weight=1);
    root.rowconfigure(1,weight=1);
    root.rowconfigure(2,weight=1);
    root.rowconfigure(3,weight=1);
    root.rowconfigure(4,weight=1);



    def data_User(conn):
        cursor_db=connection.cursor();
        cursor_db.execute(f"Select id,username,age from user_tabel");
        user_data=cursor_db.fetchall()
        return user_data;



    lbl_title=tk.Label(root,text="User Table",font=("Arial",24));
    lbl_title.grid(row=0,column=1,sticky=tk.N);


    def btn_back():
        root.destroy();
        User_Menu(conn=conn);


    btn_back=tk.Button(root,text="Back to Meniu",command=btn_back);
    btn_back.grid(row=0,column=2,sticky=tk.NE)


    lbl_title=tk.Label(root,text="UserName: "+USER[1],font=("Arial",17));
    lbl_title.grid(row=1,column=1,sticky=tk.N);

    tree=ttk.Treeview(root,columns=('id','username','age'),show="headings");
    tree.heading('id',text="Id");
    tree.heading('username',text="UserName");
    tree.heading('age',text="Age");

    tree.grid(row=2,column=0,columnspan=3,sticky="nsew");

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    scrollbar.grid(row=2, column=3 ,sticky=tk.NS)

    tree['yscrollcommand']=scrollbar.set;

    user_data=data_User(conn=conn);
    for user_d in user_data:
        tree.insert(parent="",index=tk.END,values=user_d); 
    """ a=[];
    for i in range(100):
        x='a'+str(i);
        y='b'+str(i);
        z='c'+str(i);
        a.append((x,y,z));
    
    for i in a:
        tree.insert(parent="",index=tk.END,values=i); """


    root.mainloop();









def Customer_Table(conn):
    root=tk.Tk();
    root.geometry("1200x800");
    root.title("Customer Table");

    root.columnconfigure(0,weight=1);
    root.columnconfigure(1,weight=1);
    root.columnconfigure(2,weight=1);
    root.columnconfigure(3,weight=1);
    root.columnconfigure(4,weight=1);
    root.columnconfigure(5,weight=1);

    root.rowconfigure(0,weight=1);
    root.rowconfigure(1,weight=1);
    root.rowconfigure(2,weight=1);
    root.rowconfigure(3,weight=1);
    root.rowconfigure(4,weight=1);
    root.rowconfigure(5,weight=1);


    frame_title=tk.Frame(root);
    frame_title.grid(row=0,column=3,sticky="nsew");

    lbl_title=tk.Label(frame_title,text="Customer Table",font=("Arial",21));
    lbl_title.pack();

    lbl_username=tk.Label(frame_title,text="UserName: "+USER[1],font=("Arial",17));
    lbl_username.pack();

    def btn_back():
        root.destroy();
        User_Menu(conn=conn);

    btn_back=tk.Button(root,text="Back to Meniu",command=btn_back);
    btn_back.grid(row=0,column=5,sticky=tk.NE)



    frame_insert=tk.Frame(root,bg="grey");
    frame_insert.grid(row=1,column=0,rowspan=4,columnspan=2,sticky="NSEW");


    customername_txt=tk.StringVar();
    phone_number_txt=tk.StringVar();
    userinsert_txt=tk.StringVar();

    lbl_nameCustomer=tk.Label(frame_insert,text="Customer Name:");
    lbl_nameCustomer.pack(anchor="w",padx=5,pady=5);

    text_customername=tk.Entry(frame_insert,textvariable=customername_txt);
    text_customername.pack(anchor="w",padx=5,fill="x");



    lbl_phonenr=tk.Label(frame_insert,text="Phone Customer:");
    lbl_phonenr.pack(anchor="w",padx=5,pady=5);

    text_phonenr=tk.Entry(frame_insert,textvariable=phone_number_txt);
    text_phonenr.pack(anchor="w",padx=5,fill="x");
    

    lbl_userinsert=tk.Label(frame_insert,text="User Insert:");
    lbl_userinsert.pack(anchor="w",padx=5,pady=5);

    text_userinsert=tk.Entry(frame_insert,textvariable=userinsert_txt);
    text_userinsert.insert(0,USER[0]);
    text_userinsert.config(state="disabled")
    text_userinsert.pack(anchor="w",padx=5,fill="x");


    frame_btn=tk.Frame(frame_insert,bg="grey");
    frame_btn.pack(padx=5,pady=20,fill="x");

    frame_btn.columnconfigure(0,weight=1);
    frame_btn.columnconfigure(1,weight=1);
    frame_btn.columnconfigure(2,weight=1);

    def add_customer():
        """ print(customername_txt.get()); 
        print(phone_number_txt.get())
        print(userinsert_txt.get()) """
        if(len(customername_txt.get())==0 or len(phone_number_txt.get())==0 or userinsert_txt.get()==0):
            messagebox.showwarning("Warning", "Fill All the Fields")
            return;
        cursor_db=conn.cursor();
        cursor_db.execute(f"INSERT into customers_table(name_customer,phone_number,user_id) values('{customername_txt.get()}','{phone_number_txt.get()}','{userinsert_txt.get()}') ");
        connection.commit();
        if(cursor_db.rowcount>0):
            messagebox.showinfo("showinfo", "User created")
        table_insert();
    


    

    btn_add=tk.Button(frame_btn,text="Add",command=add_customer);
    btn_add.grid(row=0,column=0);

    btn_edit=tk.Button(frame_btn,text="Edit");
    btn_edit.grid(row=0,column=1);


    def delete_customer():
        number_selected=len(table_customer.selection())
        print(number_selected)
        if(number_selected>0):
            val=messagebox.askyesno("askquestion", f"Are you sure you want to delete {number_selected} customers?")
            print(val)
            if(val):
                for i in table_customer.selection():
                    customer_selected=table_customer.item(i)
                    cursor_db=conn.cursor();
                    cursor_db.execute(f"Delete from customers_table where id={customer_selected['values'][0]}");
                    connection.commit();
                    #print(customer_selected['values'])
                    table_customer.delete(i);

    btn_delete=tk.Button(frame_btn,text="Delete",command=delete_customer);
    btn_delete.grid(row=0,column=2);


    """ table_customer=ttk.Treeview(root,columns=('id','customer_name','phone_nr','user_id'),show="headings");
    table_customer.heading('id',text="Id:");
    table_customer.heading('customer_name',text="Customer Name:");
    table_customer.heading('phone_nr',text="Phone_Number:");
    table_customer.heading('user_id',text="User-Id:");
    table_customer.grid(row=1,column=3,rowspan=4,sticky=tk.NSEW);

    scrollbar = ttk.Scrollbar(root, orient='vertical', command=table_customer.yview)
    scrollbar.grid(row=1, column=5 ,rowspan=4,sticky=tk.NS)

    table_customer['yscrollcommand']=scrollbar.set;

    a=[];
    for i in range(100):
        x='a'+str(i);
        y='b'+str(i);
        z='c'+str(i);
        w="d"+str(i);
        a.append((x,y,z,w));
    
    for i in a:
        table_customer.insert(parent="",index=tk.END,values=i);  """
    
    frame_table=tk.Frame(root,bg="white");
    frame_table.grid(row=1,column=2,columnspan=4,rowspan=4,sticky=tk.NSEW);

    frame_table.columnconfigure(0,weight=1);
    frame_table.columnconfigure(1,weight=1); 
    
    frame_table.rowconfigure(0,weight=1);


    def Retrieve_mysqlCUstomer():
        cursor_db=conn.cursor();
        cursor_db.execute(f"Select * from customers_table");
        user_data=cursor_db.fetchall()
        return user_data;




    table_customer=ttk.Treeview(frame_table,columns=('id','customer_name','phone_nr','user_id'),show="headings");
    table_customer.heading('id',text="Id:");
    table_customer.heading('customer_name',text="Customer Name:");
    table_customer.heading('phone_nr',text="Phone_Number:");
    table_customer.heading('user_id',text="User-Id:");
    table_customer.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW);

    customer_data=Retrieve_mysqlCUstomer();
    for i in customer_data:
        table_customer.insert(parent="",index=tk.END,values=i);  

    def clear_all():
        for item in table_customer.get_children():
            table_customer.delete(item)

    def table_insert():
        clear_all();
        customer_data=Retrieve_mysqlCUstomer();
        for i in customer_data:
            table_customer.insert(parent="",index=tk.END,values=i);

    """ scrollbar = ttk.Scrollbar(frame_table, orient='vertical', command=table_customer.yview)
    scrollbar.grid(row=0, column=1 ,sticky=tk.NS)
    table_customer['yscrollcommand']=scrollbar.set; """ 

    root.mainloop();






def Products_Table(conn):
    pass


def Orders_Table(conn):
    pass





if __name__=="__main__":
    USER=[0,""];
    try:
        connection=mysql.connector.connect(
        host='localhost',
        database='db_python1',
        user="root",
        password="root");
        #Log_IN(conn=connection);
        Customer_Table(conn=connection);
        #User_Menu(conn=connection);
        #User_Table(conn=connection);
    except Error as e:
        print("Error DataBase: ",e);    


