const MainDB = class{

    constructor(con) {
        this.SQLCon = con;
    }

    del_acts_from_mainDB(acts) {
        let sql = `UPDATE MainTableV1 SET acts = '' WHERE acts = ?`;

        this.SQLCon.SqlConnect(this.SQLCon.con);

        for(let i = 0; i < acts.length; i++){
            this.SQLCon.con.query(sql, [acts[i]])
        }

        this.SQLCon.SqlEnd(this.SQLCon.con)

    }

};

module.exports.MainDB = MainDB;