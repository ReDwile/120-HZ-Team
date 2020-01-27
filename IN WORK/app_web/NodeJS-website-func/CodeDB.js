const XlsxPopulate = require('xlsx-populate');
const deasync = require('deasync');

const CodeDB = class{

    getCode(){
        let value = null;

        XlsxPopulate.fromFileAsync("/Users/lalkalol/Desktop/bot/Data/code.xlsx")
            .then(workbook => {
            value = workbook.sheet("Лист1").cell("A1").value()
        });

        while((value == null)){
            deasync.runLoopOnce()
        }

        return value;
    }
}

module.exports.CodeDB = CodeDB;