////Command Line:  
//npm install --save body-parser,npm install --save express, npm install --save ejs,npm install --save mysql2 
//console.log("Project------");

const express=require('express');
const path=require('path');
const app=express();

app.use(express.urlencoded({extended: 'false'}))
app.use(express.json())

app.set('view engine','ejs');

app.use(express.static(path.join(__dirname,'public'))); //For css,image

app.get('/',(req,res,next)=>{
    res.render('index.ejs',{title:"Main Page"});
});


app.get('/book-description',(req,res,next)=>{
    res.render('book-descrpt.ejs',{title:"Book Description"});
});


app.get('/cart',(req,res,next)=>{
    res.render('cart.ejs',{title:"Cart Page"});
});


app.get('/my-library',(req,res,next)=>{
    res.render('mylibrary.ejs',{title:"My Library"});
});


app.get('/log-in',(req,res,next)=>{
    res.render('login.ejs',{title:"LogIn Page"});
});


app.get('/register',(req,res,next)=>{
    res.render('register.ejs',{title:"Register Page"});
});


app.get('/user-info',(req,res,next)=>{
    res.render('user-info.ejs',{title:"User Info Page"});
});

app.listen(5000);