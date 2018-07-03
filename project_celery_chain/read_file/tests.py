# import xlrd
#
# wb2 = xlrd.open_workbook('usuarios.xls')
# sheet = wb2.sheet_by_index(0)
#
# dir_cantidad = len(sheet.col_values(0))-1
# header = [
#         'id',
#         'last_login',
#         'is_superuser',
#         'username',
#         'first_name',
#         'last_name',
#         'email',
#         'is_staff',
#         'is_active',
#         'date_joined'
#     ]
#
# print(sheet.cell_value(0,1))
#
# lista = [0]*sheet.ncols
#
# for r in range(1, sheet.nrows):
#     for c in range(0, sheet.ncols):
#          lista[c] = sheet.cell_value(r,c)
#     print(lista)

#
# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('usuario.xlsx')
# worksheet = workbook.add_worksheet()
#
# worksheet.write(0, 0, "id")
# worksheet.write(0, 1, "last_login")
# worksheet.write(0, 2, "is_superuser")
# worksheet.write(0, 3, "username")
# worksheet.write(0, 4, "first_name")
# worksheet.write(0, 5, "last_name")
# worksheet.write(0, 6, "email")
# worksheet.write(0, 7, "is_staff")
# worksheet.write(0, 8, "is_active")
# worksheet.write(0, 9, "date_joined")
# workbook.close()
