const path_main_dir=require('../util/path_dir');
 const mysql=require('mysql');
const dotenv=require('dotenv');
dotenv.config({path:path_main_dir+"/.env"});

const db=mysql.createConnection({
    host: process.env.DATABASE_HOST,
    user: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    database:process.env.DATABASE
});

db.connect((error) => {
    if(error) {
        console.log(error)
    } else {
        console.log("MySQL connected!")
    }
});

module.exports = db;  