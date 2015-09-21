import xlsxwriter

def excelWrite(list) :
    workbook = xlsxwriter.Workbook('GB.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for col1, col2, col3, col4 in (list):
        worksheet.write(row, col, col1)
        worksheet.write(row, col + 1, col2)
        worksheet.write(row, col + 2, col3)
        worksheet.write(row, col + 3, col4)
        row += 1

    workbook.close()