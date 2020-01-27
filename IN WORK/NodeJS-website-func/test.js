const logDB = require("./loginDB");
const con = require("./sql");
const mainDB = require("./MainDB");
const codeDB = require("./CodeDB")
/*
let conn = new con.SqlConnection('localhost', 'root', 'site', '');
let loginDB = new logDB.loginDB(conn);
let MainDB = new mainDB.MainDB(conn);

console.log(loginDB.getPassword('testlogin'));

*/
let CodeDB = new codeDB.CodeDB()

console.log(CodeDB.getCode())
