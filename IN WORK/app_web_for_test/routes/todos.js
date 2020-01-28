const{Router} = require('express');
//const Todo = require('..r/models/todo');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const config = require('../config/db');
const passport =require('passport');

const logDB = require("../NodeJS-website-func/loginDB");
const con = require("../NodeJS-website-func/sql");
const mainDB = require("../NodeJS-website-func/MainDB");
const codeDB = require("../NodeJS-website-func/CodeDB");
const actsDB = require("../NodeJS-website-func/ActsDB");
const send = require("../NodeJS-website-func/SendMessage");


let conn = new con.SqlConnection(
    'localhost',
    'root',
    'site',
    ''
);
let loginDB = new logDB.loginDB(conn);
let MainDB = new mainDB.MainDB(conn);
let CodeDB = new codeDB.CodeDB();
let ActsDB = new actsDB.ActsDB(conn);
let Send = new send.send(conn);
global.a = false;
let dog= ActsDB.getallacts();
let excel=CodeDB.getCode();
const router = Router();

let urlencodedparser=bodyParser.urlencoded({extended:false});
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



router.get('/', (req,res) => {
  res.render('reg',{
    title:"registration",
    isCreate:true
  });
});

router.post('/',urlencodedparser,function (req,res) {
  if(!req.body){
    res.render('reg',{
      title:"registration",
      isCreate:true
    });
  }
  const login = req.body.login;
  const password = req.body.pass;

  if(password === "8899" && login === "mihaildorodnikov032@gmail.com"){
    res.redirect('/main')
    a = true;
  }else{
    res.redirect('/')
  }
});

////////////////////////////////////////////////////////////////////////////////////////<img src="https://pbs.twimg.com/media/DdCFB1bX4AAxOKL.jpg" alt="test">



if (a){
  router.get('/main',(req,res) => {
    res.render('simple',{
      title:"main",
      isCreate:true
    });
  });

  router.get('/acts', (req,res)=>{
    //const todos = await Todo.find({})
    res.render('index',{
      title:'kostya',
      isIndex:true,
      todos:dog
    });
  });

  router.get('/create',(req,res)=>{
    res.render('create',{
      title:'create todos',
      isCreate:true
    });
  });

  router.get('/delete',(req,res)=>{
    res.render('delete',{
      title:'create todos',
      isCreate:true,
      todos:dog
    });
  });
}else {
  router.get('/main',passport.authenticate('jwt',{session:false}),(req,res) => {
    res.render('simple',{
      title:"main",
      isCreate:true
    });
  });

  router.get('/acts',passport.authenticate('jwt',{session:false}), (req,res)=>{
    //const todos = await Todo.find({})
    res.render('index',{
      title:'kostya',
      isIndex:true,
      todos:dog
    });
  });

  router.get('/create',passport.authenticate('jwt',{session:false}),(req,res)=>{
    res.render('create',{
      title:'create todos',
      isCreate:true
    });
  });

  router.get('/delete',passport.authenticate('jwt',{session:false}),(req,res)=>{
    res.render('delete',{
      title:'create todos',
      isCreate:true,
      todos:dog
    });
  });
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
router.post('/main',urlencodedparser,function (req,res) {
  res.render('simple',{
    title:"main",
    isCreate:true,
    code:excel
  });
});
router.post('/acts',urlencodedparser, (req,res) => {
  res.render('index',{
    title:'kostya',
    isIndex:true,
    todos:dog
  });
});
router.post('/create',urlencodedparser, (req, res) => {
  let cat =[];
  cat[cat.length] = req.body.title;
  dog[dog.length]=ActsDB.addacts(cat);
  console.log(dog);
  res.render('index',{
    title:'kostya',
    isIndex:true,
    todos:dog

  });
});
router.post('/main',urlencodedparser,function (req,res) {
  res.render('simple',{
    title:"main",
    isCreate:true,
    code:excel
  });
});
router.post('/delete',urlencodedparser, (req, res) => {
  dog[dog.length] = req.body.title;
  if (req.body)
  res.render('delete',{
    title:'удаление',
    isIndex:true,
    todos:dog

  });
});


module.exports =router;
