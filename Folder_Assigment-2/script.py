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
    
    def btn_Products_Table():
        root.destroy();
        Products_Table(conn=conn);
    
    def btn_Order_Table():
        root.destroy()
        Orders_Table(conn=conn);


    btn_user_view=tk.Button(root,text="User-View",font=("Arial",19),command=btn_User_Table);
    btn_user_view.grid(row=2,column=0,sticky=tk.N);

    btn_customer=tk.Button(root,text="Customers",font=("Arial",19),command=btn_Customer_Table);
    btn_customer.grid(row=2,column=2,sticky=tk.N);

    btn_products=tk.Button(root,text="Products",font=("Arial",19),command=btn_Products_Table);
    btn_products.grid(row=3,column=0,sticky=tk.N);

    btn_orders=tk.Button(root,text="Orders",font=("Arial",19),command=btn_Order_Table);
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


    def btn_Edit_Customer():
        if(len(table_customer.selection())==0 or len(table_customer.selection())>1 ):
            messagebox.showwarning("Warning", "Select 1 Customer to Edit")
            return;

        val_selected=table_customer.item(table_customer.selection()[0])['values'];
        print(val_selected)
        root.destroy();
        frame_edit=tk.Tk();
        frame_edit.geometry("400x300");
        
        frame_edit.columnconfigure(0,weight=1);
        frame_edit.columnconfigure(1,weight=1);
        

        for i in range(10):
            frame_edit.rowconfigure(i,weight=1);
        

        lbl_title=tk.Label(frame_edit,text="Edit Customer Id:"+str(val_selected[0]),font='Helvetica 16 bold')
        lbl_title.grid(row=0,column=0,rowspan=2,sticky=tk.NE);


        def back_Customer_table():
            frame_edit.destroy();
            Customer_Table(conn=connection);


        btn_back_customer=tk.Button(frame_edit,text="Back Customer_Table",command=back_Customer_table);
        btn_back_customer.grid(row=0,column=1,rowspan=2,sticky=tk.NE)

        
        frame_insert_edit=tk.Frame(frame_edit,bg="grey");
        frame_insert_edit.grid(row=2,column=0,rowspan=8,columnspan=2,sticky=tk.NSEW);

        customername_edit_var=tk.StringVar();
        phonenr_edit_var=tk.StringVar();
        useredit_var=tk.StringVar();
        
        lbl_nameCustomer=tk.Label(frame_insert_edit,text="Customer Name:");
        lbl_nameCustomer.pack(anchor="w",padx=60,pady=5);

        txt_nameCustomer=tk.Entry(frame_insert_edit,textvariable=customername_edit_var);
        txt_nameCustomer.insert(0,val_selected[1]);
        txt_nameCustomer.pack(fill="x",padx=60);


        lbl_phonecust=tk.Label(frame_insert_edit,text="Phone Customer:");
        lbl_phonecust.pack(anchor="w",padx=60,pady=5);

        txt_phonecust=tk.Entry(frame_insert_edit,textvariable=phonenr_edit_var);
        txt_phonecust.insert(0,val_selected[2]);
        txt_phonecust.pack(fill="x",padx=60);

        
        lbl_useredit=tk.Label(frame_insert_edit,text="User Insert(Edit):");
        lbl_useredit.pack(anchor="w",padx=60,pady=5);

        text_useredit=tk.Entry(frame_insert_edit,textvariable=useredit_var);
        text_useredit.insert(0,USER[0]);
        text_useredit.config(state="disabled")
        text_useredit.pack(padx=60,fill="x");


        def Edit_Customer_function_btn(val_selected):
            if(len(customername_edit_var.get())==0 or len(phonenr_edit_var.get())==0):
                messagebox.showwarning("showwarning", "Fill all the fields!");
                return;
            """ print(customername_edit_var.get());
            print(phonenr_edit_var.get());
            print(useredit_var.get()); """
            cursor_db=connection.cursor();
            cursor_db.execute(f"Update customers_table set name_customer='{customername_edit_var.get()}',phone_number='{phonenr_edit_var.get()}',user_id='{useredit_var.get()}' where id={val_selected[0]} ");
            connection.commit();
            if(cursor_db.rowcount>0):
                messagebox.showinfo("showinfo", "Customer Edited");
                frame_edit.destroy();
                Customer_Table(conn=connection);


        
        btn_Edit_cust=tk.Button(frame_insert_edit,text="EditCustomer",command=lambda:Edit_Customer_function_btn(val_selected));
        btn_Edit_cust.pack(pady=20);

        

        frame_edit.mainloop();


    btn_edit=tk.Button(frame_btn,text="Edit",command=btn_Edit_Customer);
    btn_edit.grid(row=0,column=1);


    def delete_customer():
        number_selected=len(table_customer.selection())
        #print(number_selected)
        if(number_selected>0):
            val=messagebox.askyesno("askquestion", f"Are you sure you want to delete {number_selected} customers?")
            #print(val)
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
    root=tk.Tk();
    root.geometry("1200x800");
    root.title("Product Table");

    for i in range(5):
        root.columnconfigure(i,weight=1);
        root.rowconfigure(i,weight=1)

    #Title-Frame and UserName-title:
    frame_title=tk.Frame(root);
    frame_title.grid(row=0,column=2,sticky="nsew");

    lbl_title=tk.Label(frame_title,text="Products Table",font=("Arial",21));
    lbl_title.pack();

    lbl_username=tk.Label(frame_title,text="UserName: "+USER[1],font=("Arial",17));
    lbl_username.pack();


    def btn_back():
        root.destroy();
        User_Menu(conn=conn);

    btn_back=tk.Button(root,text="Back to Meniu",command=btn_back);
    btn_back.grid(row=0,column=5,sticky=tk.NE);




    #Label Insert Data:
    frame_insert=tk.Frame(root,bg="grey");
    frame_insert.grid(row=1,column=0,rowspan=4,columnspan=2,sticky="NSEW");

    name_product=tk.StringVar();
    value_product=tk.StringVar();
    quantity_product=tk.StringVar();
    userinsert_txt=tk.StringVar();


    lbl_nameProduct=tk.Label(frame_insert,text="Name Product:");
    lbl_nameProduct.pack(anchor="w",padx=5,pady=5);

    text_productname=tk.Entry(frame_insert,textvariable=name_product);
    text_productname.pack(anchor="w",padx=5,fill="x");

    #tk.Label(frame_insert).pack(pady=20);

    lbl_valueproduct=tk.Label(frame_insert,text="Value Product:");
    lbl_valueproduct.pack(anchor="w",padx=5,pady=5);

    text_valueproduct=tk.Entry(frame_insert,textvariable=value_product);
    text_valueproduct.pack(anchor="w",padx=5,fill="x");


    lbl_quantityproduct=tk.Label(frame_insert,text="Quantity Product:");
    lbl_quantityproduct.pack(anchor="w",padx=5,pady=5);

    text_quantityproduct=tk.Entry(frame_insert,textvariable=quantity_product);
    text_quantityproduct.pack(anchor="w",padx=5,fill="x");
    


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



    def is_float(string):
        try:
            # float() is a built-in function
            float(string)
            return True
        except ValueError:
            return False






    def add_customer():
        """ print(customername_txt.get()); 
        print(phone_number_txt.get())
        print(userinsert_txt.get()) """
        if(len(name_product.get())==0 or len(value_product.get())==0 or len(quantity_product.get())==0 or  len(userinsert_txt.get())==0):
            messagebox.showwarning("Warning", "Fill All the Fields")
            return;
        if( (not is_float(value_product.get())) or ( not quantity_product.get().isnumeric() )  ):
            messagebox.showwarning("Warning", "Product Value and Quantity have to be a number");
            return;

        cursor_db=connection.cursor();
        cursor_db.execute(f"INSERT into products_table(name_product,value_product,quantity,user_id) values('{name_product.get()}',{value_product.get()},'{quantity_product.get()}','{userinsert_txt.get()}') ");
        connection.commit();
        if(cursor_db.rowcount>0):
            messagebox.showinfo("showinfo", "Product created")
            table_insert();

    btn_add=tk.Button(frame_btn,text="Add",command=add_customer);
    btn_add.grid(row=0,column=0);






    def Edit_Product_btn():
        if(len(table_product.selection())==0 or len(table_product.selection())>1 ):
            messagebox.showwarning("Warning", "Select 1 Product to Edit")
            return;

        val_selected=table_product.item(table_product.selection()[0])['values'];
        root.destroy();
        frame_edit=tk.Tk();
        frame_edit.geometry("500x400");
        
        frame_edit.columnconfigure(0,weight=1);
        frame_edit.columnconfigure(1,weight=1);
        

        for i in range(10):
            frame_edit.rowconfigure(i,weight=1);
    

        lbl_title=tk.Label(frame_edit,text="Edit Product Id:"+str(val_selected[0]),font='Helvetica 16 bold')
        lbl_title.grid(row=0,column=0,rowspan=2,sticky=tk.NE);


        def back_Product_table():
            frame_edit.destroy();
            Products_Table(conn=connection);


        btn_back_customer=tk.Button(frame_edit,text="Back Product_Table",command=back_Product_table);
        btn_back_customer.grid(row=0,column=1,rowspan=2,sticky=tk.NE)

        frame_insert_edit=tk.Frame(frame_edit,bg="grey");
        frame_insert_edit.grid(row=2,column=0,rowspan=8,columnspan=2,sticky=tk.NSEW);

        name_product_edit=tk.StringVar();
        value_product_edit=tk.StringVar();
        quantity_product_edit=tk.StringVar();
        userinsert_txt_edit=tk.StringVar();


        lbl_nameProduct=tk.Label(frame_insert_edit,text="Name Product:");
        lbl_nameProduct.pack(anchor="w",padx=60,pady=5);

        txt_nameProduct=tk.Entry(frame_insert_edit,textvariable=name_product_edit);
        txt_nameProduct.insert(0,val_selected[1]);
        txt_nameProduct.pack(fill="x",padx=60);


        lbl_valueprod=tk.Label(frame_insert_edit,text="Value Product:");
        lbl_valueprod.pack(anchor="w",padx=60,pady=5);

        txt_valueprod=tk.Entry(frame_insert_edit,textvariable=value_product_edit);
        txt_valueprod.insert(0,val_selected[2]);
        txt_valueprod.pack(fill="x",padx=60);



        lbl_quantityprod=tk.Label(frame_insert_edit,text="Quantity Product:");
        lbl_quantityprod.pack(anchor="w",padx=60,pady=5);

        txt_quantityprod=tk.Entry(frame_insert_edit,textvariable=quantity_product_edit);
        txt_quantityprod.insert(0,val_selected[3]);
        txt_quantityprod.pack(fill="x",padx=60);

        

        lbl_useredit=tk.Label(frame_insert_edit,text="User Insert(Edit):");
        lbl_useredit.pack(anchor="w",padx=60,pady=5);

        text_useredit=tk.Entry(frame_insert_edit,textvariable=userinsert_txt_edit);
        text_useredit.insert(0,USER[0]);
        text_useredit.config(state="disabled")
        text_useredit.pack(padx=60,fill="x");

        def Edit_Product_function_btn(val_selected):
            if(len(name_product_edit.get())==0 or len(value_product_edit.get())==0 or len(quantity_product_edit.get())==0):
                messagebox.showwarning("Warning", "Fill All the Fields")
                return;
            if( (not is_float(value_product_edit.get())) or ( not quantity_product_edit.get().isnumeric() )  ):
                messagebox.showwarning("Warning", "Product Value and Quantity have to be a number");
                return;
            print("Eidt");
            """ print(customername_edit_var.get());
            print(phonenr_edit_var.get());
            print(useredit_var.get()); """
            cursor_db=connection.cursor();
            cursor_db.execute(f"Update products_table set name_product='{name_product_edit.get()}',value_product={value_product_edit.get()},quantity='{quantity_product_edit.get()}',user_id='{userinsert_txt_edit.get()}' where id_prod={val_selected[0]} ");
            connection.commit();
            if(cursor_db.rowcount>0):
                messagebox.showinfo("showinfo", "Product Edited");
                frame_edit.destroy();
                Products_Table(conn=connection)


        
        btn_Edit_cust=tk.Button(frame_insert_edit,text="EditProduct",command=lambda:Edit_Product_function_btn(val_selected));
        btn_Edit_cust.pack(pady=20);





        frame_edit.mainloop();
    





    btn_edit=tk.Button(frame_btn,text="Edit",command=Edit_Product_btn);
    btn_edit.grid(row=0,column=1);






    def delete_product_btn():
        number_selected=len(table_product.selection())
        if(number_selected>0):
            val=messagebox.askyesno("askquestion", f"Are you sure you want to delete {number_selected} product?")
            #print(val)
            if(val):
                for i in table_product.selection():
                    product_selected=table_product.item(i)
                    cursor_db=conn.cursor();
                    cursor_db.execute(f"Delete from products_table where id_prod={product_selected['values'][0]}");
                    connection.commit();
                    #print(customer_selected['values'])
                    table_product.delete(i);



    btn_delete=tk.Button(frame_btn,text="Delete",command=delete_product_btn);
    btn_delete.grid(row=0,column=2);



    #Table:
    frame_table=tk.Frame(root,bg="white");
    frame_table.grid(row=1,column=2,columnspan=4,rowspan=4,sticky=tk.NSEW);

    frame_table.columnconfigure(0,weight=1);
    frame_table.columnconfigure(1,weight=1); 
    
    frame_table.rowconfigure(0,weight=1);

    def Retrieve_mysqlProducts():
        cursor_db=conn.cursor();
        cursor_db.execute(f"Select * from products_table");
        user_data=cursor_db.fetchall()
        return user_data;

    table_product=ttk.Treeview(frame_table,columns=('id_prod','name_prod','value_prod','quantity_prod','user_id'),show="headings");
    table_product.heading('id_prod',text="Id:");
    table_product.heading('name_prod',text="Name Product:");
    table_product.heading('value_prod',text="Value Product:");
    table_product.heading('quantity_prod',text="Quantity Product:");#quantity_prod
    table_product.heading('user_id',text="User-Id:");
    table_product.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW);

    customer_data=Retrieve_mysqlProducts();
    for i in customer_data:
        table_product.insert(parent="",index=tk.END,values=i);
    



    def clear_all():
        for item in table_product.get_children():
            table_product.delete(item)

    def table_insert():
        clear_all();
        customer_data=Retrieve_mysqlProducts();
        for i in customer_data:
            table_product.insert(parent="",index=tk.END,values=i);


    root.mainloop();















def Orders_Table(conn):
    root=tk.Tk();
    root.geometry("1650x900");
    root.title("Order Table");

    for i in range(5):
        root.columnconfigure(i,weight=1);
        root.rowconfigure(i,weight=1)

    #Title-Frame and UserName-title:
    frame_title=tk.Frame(root);
    frame_title.grid(row=0,column=2,sticky="nsew");

    lbl_title=tk.Label(frame_title,text="Order Table",font=("Arial",21));
    lbl_title.pack();

    lbl_username=tk.Label(frame_title,text="UserName: "+USER[1],font=("Arial",17));
    lbl_username.pack();


    def btn_back_func():
        root.destroy();
        User_Menu(conn=conn);

    btn_back=tk.Button(root,text="Back to Meniu",command=btn_back_func);
    btn_back.grid(row=0,column=5,sticky=tk.NE);

    frame_insert=tk.Frame(root,bg="grey");
    frame_insert.grid(row=1,column=0,rowspan=4,columnspan=2,sticky="NSEW");
    
    product_var=tk.StringVar();
    value_prod_var=tk.StringVar();
    quantity_prod_var=tk.StringVar();
    customer_var=tk.StringVar();
    user_id_var=tk.StringVar();

    
    
    def Retrieve_Products_sql():
        cursor_db=connection.cursor();
        cursor_db.execute(f"Select id_prod,name_product,value_product from products_table");
        product_data=cursor_db.fetchall()
        return product_data;


    lbl_nameProduct=tk.Label(frame_insert,text="Select Product:");
    lbl_nameProduct.pack(anchor="w",padx=5,pady=5);

    value_prod=Retrieve_Products_sql();
    products_mysql=[];
    for i in value_prod:
        var=str(i[0])+"<->"+str(i[1])
        products_mysql.append(var)
    #products_mysql=[];

    #print(products_mysql);
    text_productname=ttk.Combobox(frame_insert, textvariable=product_var)
    text_productname.pack(anchor="w",padx=5,fill="x");
    text_productname.config(values=products_mysql,state="readonly")
    if(len(products_mysql)>0):
        text_productname.current(0);

    

    tk.Label(frame_insert,bg="grey").pack(pady=2);


    lbl_valueprod=tk.Label(frame_insert,text="Value 1-Product:");
    lbl_valueprod.pack(anchor="w",padx=5,pady=5);

    text_valueprod=tk.Entry(frame_insert,textvariable=value_prod_var);
    if(len(products_mysql)>0):
        text_valueprod.insert(0,value_prod[text_productname.current()][2]);
    text_valueprod.config(state="disabled")
    text_valueprod.pack(anchor="w",padx=5,fill="x");

    def get_Value_Product(event):
        #print(text_productname.current());
        text_valueprod.config(state="normal");
        text_valueprod.delete(0,tk.END)
        text_valueprod.insert(0,value_prod[text_productname.current()][2]);
        text_valueprod.config(state="disabled")

    text_productname.bind('<<ComboboxSelected>>',get_Value_Product)


    tk.Label(frame_insert,bg="grey").pack(pady=2);


    lbl_quantityproduct=tk.Label(frame_insert,text="Quantity Product:");
    lbl_quantityproduct.pack(anchor="w",padx=5,pady=5);

    text_quantityproduct=tk.Entry(frame_insert,textvariable=quantity_prod_var);
    text_quantityproduct.pack(anchor="w",padx=5,fill="x");


    
    tk.Label(frame_insert,bg="grey").pack(pady=2);

    
    def Retrieve_Customer_sql():
        cursor_db=connection.cursor();
        cursor_db.execute(f"Select id,name_customer from customers_table");
        product_data=cursor_db.fetchall()
        return product_data;

    value_custm=Retrieve_Customer_sql();
    customer_mysql=[];
    for i in value_custm:
        var=str(i[0])+"<->"+str(i[1])
        customer_mysql.append(var)
    #customer_mysql=[];    

    lbl_nameCustomer=tk.Label(frame_insert,text="Select Customer:");
    lbl_nameCustomer.pack(anchor="w",padx=5,pady=5);

    text_customername=ttk.Combobox(frame_insert, textvariable=customer_var)
    text_customername.pack(anchor="w",padx=5,fill="x");
    text_customername.config(values=customer_mysql,state="readonly")
    if(len(customer_mysql)>0):
        text_customername.current(0);


    tk.Label(frame_insert,bg="grey").pack(pady=2);

    lbl_userinsert=tk.Label(frame_insert,text="User Insert:");
    lbl_userinsert.pack(anchor="w",padx=5,pady=5);

    text_userinsert=tk.Entry(frame_insert,textvariable=user_id_var);
    text_userinsert.insert(0,USER[0]);
    text_userinsert.config(state="disabled")
    text_userinsert.pack(anchor="w",padx=5,fill="x");




    tk.Label(frame_insert,bg="grey").pack(pady=2);





    frame_btn=tk.Frame(frame_insert,bg="grey");
    frame_btn.pack(padx=5,pady=20,fill="x");

    frame_btn.columnconfigure(0,weight=1);
    frame_btn.columnconfigure(1,weight=1);
    frame_btn.columnconfigure(2,weight=1);



    #print(product_var.get());
    def btn_add_order():
        print(product_var.get());
        print(value_prod_var.get())
        print(quantity_prod_var.get())
        print(customer_var.get())
        print(user_id_var.get())
        if(len(product_var.get())==0 or len(value_prod_var.get())==0 or len(quantity_prod_var.get())==0 or len(customer_var.get())==0 or len(user_id_var.get())==0 ):
            messagebox.showwarning("Warning", "Fill All the Fields");
            return;

    btn_add=tk.Button(frame_btn,text="Add",command=btn_add_order);
    btn_add.grid(row=0,column=0);

    btn_edit=tk.Button(frame_btn,text="Edit");
    btn_edit.grid(row=0,column=1);


    btn_delete=tk.Button(frame_btn,text="Delete");
    btn_delete.grid(row=0,column=2);


    

    #Table Orders:
    frame_table=tk.Frame(root,bg="white");
    frame_table.grid(row=1,column=2,columnspan=4,rowspan=4,sticky=tk.NSEW);

    frame_table.columnconfigure(0,weight=1);
    frame_table.columnconfigure(1,weight=1); 
    
    frame_table.rowconfigure(0,weight=1);


    table_product=ttk.Treeview(frame_table,columns=('id_order','prod_sel','value_1_prod','quantity_prod','value_total','customer_sel','user_id'),show="headings");
    table_product.heading('id_order',text="Id:");
    table_product.heading('prod_sel',text="Product Ordered:");
    table_product.heading('value_1_prod',text="Value 1-Product:");
    table_product.heading('quantity_prod',text="Quantity Order:");
    table_product.heading('value_total',text="Value-Total Product:");
    table_product.heading('customer_sel',text="Customer Ordered:");
    table_product.heading('user_id',text="User-Id:");
    table_product.grid(row=0,column=0,columnspan=2,sticky=tk.NSEW);

    """ customer_data=Retrieve_mysqlProducts();
    for i in customer_data:
        table_product.insert(parent="",index=tk.END,values=i); """
    



    root.mainloop();    











if __name__=="__main__":
    USER=[0,""];
    try:
        connection=mysql.connector.connect(
        host='localhost',
        database='db_python1',
        user="root",
        password="root");
        #Log_IN(conn=connection);
        Orders_Table(conn=connection)
        #Products_Table(conn=connection)
        #Customer_Table(conn=connection);
        #User_Menu(conn=connection);
        #User_Table(conn=connection);
    except Error as e:
        print("Error DataBase: ",e);    


