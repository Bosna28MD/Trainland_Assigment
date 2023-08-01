create database if not exists node_project1;
use node_project1;

create table if not exists user_tabel(
id int not null auto_increment primary key,
email varchar(255) not null,
username varchar(255) ,
age int,
pwd varchar(256) not null,
money double(16,2) default 50.00,
number_books int default 0
);


#drop table user_tabel;