from openpyxl import load_workbook
# from openpyxl.chart import BarChart, LineChart, PieChart, Reference
wb =load_workbook('sample.xlsx')
ws = wb.active

a1 = ws["A1"]
b1 = ws["B1"]
c1 = ws["C1"]
