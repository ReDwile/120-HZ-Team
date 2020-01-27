const deasync = require("deasync");

const Send = class {

    constructor(con){
        this.SQLCon = con;
    }

    GetTgId(acts){ // Достает все айдишники ТГ, принадлежащие данной активности
        let res = null;
        let sqlq = "SELECT TgId FROM MainTableV1 WHERE acts = ?";

        this.SQLCon.SqlConnect(this.SQLCon.con);
        for(let i = 0;i<acts.length; i++){
            this.SQLCon.con.query(sqlq, [acts[i]], function(err, result, fields){
                for(let j = 0;j<result.length;j++){
                    res.push(result[i].TgId)
                }
            })
        }
        this.SQLCon.SqlEnd(this.SQLCon.con);

        while((res == null)){
            deasync.runLoopOnce();
        }

        return res;
    }

    getVkId(acts){ // Достает все айдишники ВК, принадлежащие данной активности
        let res = null;
        let sqlq = "SELECT VkId FROM MainTableV1 WHERE acts = ?";

        this.SQLCon.SqlConnect(this.SQLCon.con);
        for(let i = 0;i<acts.length; i++){
            this.SQLCon.con.query(sqlq, [acts[i]], function(err, result, fields){
                for(let j = 0;j<result.length;j++){
                    res.push(result[i].VkId)
                }
            })
        }
        this.SQLCon.SqlEnd(this.SQLCon.con);

        while((res == null)){
            deasync.runLoopOnce();
        }
        return res;
    }

    send(acts, text){
        let VkId = this.getVkId(acts);
        let TgId = this.GetTgId(acts);
        

        /*Вызываю функцию отправки сообщения, 4 аргумента: название активности, массив вкид, массив тгид, текст сообщения

        pythonsend(acts, text, TgId, VkId);

        */
    }

}