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


