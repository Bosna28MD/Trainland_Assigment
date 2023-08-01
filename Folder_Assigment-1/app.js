////Command Line:  
//npm install --save body-parser,npm install --save express, npm install --save ejs,npm install --save mysql2 
//console.log("Project------");

const express=require('express');
const path=require('path');
const session=require('express-session');
const bcrypt=require('bcrypt');
const connectFlash = require('connect-flash');
const passport=require('passport');
const cookieParser=require('cookie-parser');
const db=require('./config/db_connect.js');
const initPassportLocal=require('./controler/passport.js');
const log_in_controler=require('./controler/log-in_controler.js');

const app=express();

app.use(cookieParser('secret'));

app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: false,
    cookie: {
        maxAge: 1000 * 60 * 60 * 24 // 86400000 1 day
    }
  }));

app.use(connectFlash());

app.use(express.urlencoded({extended: 'false'}))
app.use(express.json())

app.set('view engine','ejs');
app.set('views','views');

app.use(express.static(path.join(__dirname,'public'))); //For css,image

app.use(passport.initialize());
app.use(passport.session());

initPassportLocal();

app.get('/',(req,res,next)=>{
    let user=[];
    if(typeof req.user === "undefined"){ user=false; }
    else{ user=req.user; }
    res.render('index.ejs',{title:"Main Page",user:user});
});


app.get('/book-description',(req,res,next)=>{
    let user=[];
    if(typeof req.user === "undefined"){ user=false; }
    else{ user=req.user; }
    res.render('book-descrpt.ejs',{title:"Book Description",user:user});
});


app.get('/cart',log_in_controler.checkLoggedIn,(req,res,next)=>{
    res.render('cart.ejs',{title:"Cart Page",user:req.user});
});


app.get('/my-library',log_in_controler.checkLoggedIn,(req,res,next)=>{
    res.render('mylibrary.ejs',{title:"My Library",user:req.user});
});



app.get('/log-in',log_in_controler.checkLoggedOut,(req,res,next)=>{
    res.render('login.ejs',{title:"LogIn Page",error:req.flash("errors"),user:false});
});

app.post('/log-in',passport.authenticate("local", {
    successRedirect: "/",
    failureRedirect: "/log-in",
    successFlash: true,
    failureFlash: true
}));


app.get('/register',log_in_controler.checkLoggedOut,(req,res,next)=>{
    res.render('register.ejs',{title:"Register Page",error:req.flash("errors"),user:false});
});

app.post('/register',(req,res,next)=>{
    console.log(req.body,"Post Register--->");
    
    db.query('Select * from user_tabel where email = ?',[req.body.email_inp],
    async (err,results)=>{
        if(err) throw err;
        if(results.length>0){
            req.flash('errors', 'This email is already used');
            return res.redirect('/register');
        }

        const pwd_hash=await bcrypt.hash(req.body.pwd_inp,10);
        db.query('Insert into user_tabel(username,email,pwd,age) values(?,?,?,?)',
        [req.body.username_inp,req.body.email_inp,pwd_hash,req.body.age_inp],(err_ins,res_ins)=>{
            if(err_ins){ throw err_ins; }
            else{ res.redirect('/log-in'); }
        });


    }); 
});


app.get('/user-info',log_in_controler.checkLoggedIn,(req,res,next)=>{
    res.render('user-info.ejs',{title:"User Info Page",user:req.user});
});

app.post('/logout',log_in_controler.postLogOut);

app.listen(5000);