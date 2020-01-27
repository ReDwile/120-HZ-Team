const deasync = require("deasync");

const loginDB = class {

    constructor(con) {
        this.SQLCon = con;
    }

    getPassword(login) {  // Получение пароля для логина из бд
        let ret = null;

        this.SQLCon.SqlConnect(this.SQLCon.con); // Подключение к  бд

        this.SQLCon.con.query(`SELECT password FROM website WHERE login = ?`, [login], function (err, res, field) {
            ret = res[0].password
        });

        this.SQLCon.SqlEnd(this.SQLCon.con); // отключение от бд

        while ((ret == null)) {
            deasync.runLoopOnce();
        }
        return ret;
    }

};

module.exports.loginDB = loginDB;