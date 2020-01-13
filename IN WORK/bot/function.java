import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;


import java.io.File;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.ss.usermodel.FormulaEvaluator;
import org.apache.poi.ss.usermodel.Row;


class Main{

        public ArrayList<String> extractExcelContentByColumnIndex(int columnIndex){
            ArrayList<String> columndata = null;
            try {
                File f = new File("sample.xlsx");
                FileInputStream ios = new FileInputStream(f);
                HSSFWorkbook workbook = new HSSFWorkbook(ios);
                HSSFSheet sheet = workbook.getSheetAt(0);
                Iterator<Row> rowIterator = sheet.iterator();
                columndata = new ArrayList<>();

                while (rowIterator.hasNext()) {
                    Row row = rowIterator.next();
                    Iterator<Cell> cellIterator = row.cellIterator();
                    while (cellIterator.hasNext()) {
                        Cell cell = cellIterator.next();

                        if(row.getRowNum() > 0){ //To filter column headings
                            if(cell.getColumnIndex() == 0){// To match column index


                                columndata.add(cell.getNumericCellValue()+"");


                            }
                        }
                    }
                }
                ios.close();
                System.out.println(columndata);
            } catch (Exception e) {
                e.printStackTrace();
            }
            return columndata;
        }

}
