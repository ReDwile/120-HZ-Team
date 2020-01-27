const express = require('express');
//const mongoose = require('mongoose');
const path = require('path')
const cors = require('cors');
const exphbs = require('express-handlebars');
const todoRoutes = require('./routes/todos');
const passport = require('passport');
const chalk = require('chalk');
const config = require('./config/db');
//const hash = require('./models/user');

const PORT = process.env.PORT || 3000;


const app = express();
const hbs = exphbs.create({
  defaultLayout: 'main',
  extname: 'hbs'
});

app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');
app.set('views', 'views');

app.use(passport.initialize());
app.use(passport.session());
require('./config/passport')(passport);
app.use(express.urlencoded({ extended:true }));
app.use(express.static(path.join(__dirname, 'public')));
//app.use(express.static(path.join(__dirname,'views/partials/scripts')))
app.use(cors());
app.use(todoRoutes);
let test = "jwgvwuedc"


async function start() {
  try {
    app.listen(3000, () => {
      console.log(chalk.yellow('Server has been started...',PORT));
      console.log(`gfdilgvbj${test}`);
    })
  } catch (e) {
    console.log(chalk.red(e));
  }
}

start();
