const mainDB = require("./MainDB");
const deasync = require("deasync");

const ActsDB = class{

    constructor(con) {
        this.SQLCon = con;
        this.mainDB = new mainDB.MainDB(this.SQLCon);
    }

    getallacts(){
        let ret = null;
        let sqlq = 'SELECT name FROM Acts';

        this.SQLCon.SqlConnect(this.SQLCon.con);
        this.SQLCon.con.query(sqlq, function (err, res, fields) {
            ret = res.name;
        });

        this.SQLCon.SqlEnd(this.SQLCon.con);

        while((ret == null)){
            deasync.runLoopOnce()
        }

        return ret;
    }

    delacts(acts){
        let sqlq = "DELETE FROM Acts WHERE name = ?"

        this.SQLCon.SqlConnect(this.SQLCon.con);
        for(let i = 0;i<a.length;i++){
            this.SQLCon.con.query(sqlq, [acts[i]]);
        }

        this.SQLCon.SqlEnd(this.SQLCon.con);

        this.mainDB.del_acts_from_mainDB(acts);
    }

    addacts(acts){
        let sqlq = "INSERT INTO Acts VALUES (?)";

        this.SQLCon.SqlConnect(this.SQLCon.con);
        for(let i = 0;i<a.length;i++){
            this.SQLCon.con.query(sqlq, [acts[i]]);
        }

        this.SQLCon.SqlEnd(this.SQLCon.con);
    }
};

module.exports.ActsDB = ActsDB;