// const bcrypt = require('bcryptjs');
// const fs = require('fs');
// var pass = fs.readFile('../routes/pass.txt');
// const Sequelize = require("sequelize");
// const sequelize = new Sequelize("usersdb2", "root", "123456", {
//   dialect: "mysql",
//   host: "localhost"
// });
// const User = sequelize.define("user", {
//   pass: {
//     type: Sequelize.STRING,
//     autoIncrement: true,
//     primaryKey: true,
//     allowNull: false
//   },
//   name: {
//     type: Sequelize.STRING,
//     allowNull: false
//   },
//   age: {
//     type: Sequelize.INTEGER,
//     allowNull: false
//   }
// });
//
// bcrypt.genSalt(10,function (err,salt) {
//   bcrypt.hash(pass,salt,function (err,hash) {
//
//   })
// })
//
// module.exports={
//   "hash":hash
// };
// console.log(hash);
