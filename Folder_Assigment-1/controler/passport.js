const passportLocal=require("passport-local");
const passport=require("passport");
const bcrypt=require('bcrypt');
const db=require('../config/db_connect.js');

let LocalStrategy = passportLocal.Strategy;

let initPassportLocal = () =>{
    passport.use(new LocalStrategy({
        usernameField: 'email_inp',
        passwordField: 'pwd_inp',
        passReqToCallback: true
    },
    async (req, email, password, done) => {
        try{
            await findUserByEmail(email).then(async (user)=>{
                if(!user){
                    return done(null, false, req.flash("errors", `This user email "${email}" doesn't exist`));
                }
                if(user){
                    let pwd_compare=await bcrypt.compare(password,user.pwd);
                    if(pwd_compare===true){
                        return done(null, user, null);
                    }
                    else{
                        return done(null, false, req.flash("errors", "The password that you've entered is incorrect"));
                    }
                }
            });

        }catch(error1){
            console.log(error1);
            return done(null, false, { message: error1 });
        }

    }));
}


passport.serializeUser((user, done) => {
    done(null, user.id);
});

passport.deserializeUser((id, done) => {
    findUserById(id).then((user) => {
        return done(null, user);
    }).catch(error => {
        return done(error, null)
    });
});

//console.log(findUserByEmail("email1@email.com"))




function findUserByEmail(email)  {
    return new Promise((resolve, reject) => {
        try {
            db.query(
                ' SELECT * FROM `user_tabel` WHERE `email` = ?  ', email,
                function(err, rows) {
                    if (err) {
                        reject(err)
                    }
                    let user = rows[0];
                    resolve(user);
                }
            );
        } catch (err) {
            reject(err);
        }
    });
};


function findUserById(id) {
    return new Promise((resolve, reject) => {
        try {
            db.query(
                ' SELECT * FROM `user_tabel` WHERE `id` = ?  ', id,
                function(err, rows) {
                    if (err) {
                        reject(err)
                    }
                    let user = rows[0];
                    resolve(user);
                }
            );
        } catch (err) {
            reject(err);
        }
    });
};


module.exports = initPassportLocal;