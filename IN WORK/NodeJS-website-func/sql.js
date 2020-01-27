const mysql = require("mysql2");

const sqlconnection = class {

    constructor(host, user, database, password) {

        this.con = mysql.createConnection({
            host: host, //localhost
            user: user, //lalkalol_crochz
            database: database,  //lalkalol_crochz
            password: password //python
        });
    }

    SqlConnect(connection) {
        connection.connect(function (err) {
            if (err) {
                return console.error("Ошибка: " + err.message);
            } else {
                console.log("Подключение к серверу MySQL успешно установлено");
            }
        });
    }

    SqlEnd(connection) {
        connection.end(function (err) {
            if (err) {
                return console.log("Ошибка: " + err.message);
            }
            console.log("Подключение закрыто");
        });
    }
};

module.exports.SqlConnection = sqlconnection;