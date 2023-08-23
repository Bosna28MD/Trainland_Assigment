create database if not exists db_python1;
use db_python1;

create table if not exists user_tabel(
id int not null auto_increment,
username varchar(256) not null,
age int ,
pwd varchar(256) not null,
primary key(id)
);

#insert into user_tabel(username,age,pwd) values("user1",23,"qwe123");
#drop table user_tabel;



create table if not exists customers_table(
id int not null auto_increment primary key,
name_customer varchar(255),
phone_number varchar(20) ,
user_id int
);
#insert into customers_table(name_customer,phone_number,user_id) values('customer1','0745612385',1);
#drop table customers_table;

create table if not exists products_table(
id_prod int not null auto_increment primary key,
name_product varchar(256) not null,
value_product double(16,2) not null,
quantity int not null,
user_id int
);
#insert into products_table(name_product,value_product,quantity,user_id) values('product1',25.75,10,1);
#drop table products_table;


create table if not exists orders_table(
id int not null auto_increment primary key,
id_prod int not null,
quantity_prod int not null,
id_customer int not null,
date_order DATE DEFAULT (CURRENT_DATE),
user_id int
);

#insert into 
#drop table orders_table;
#insert into orders_table(id_prod,quantity_prod,id_customer,user_id) values(1,2);
