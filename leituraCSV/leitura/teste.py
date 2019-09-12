from datetime import date, datetime
from collections import OrderedDict

data1 = "14/03/2018"
data = "13/03/2018"
d = date(1970,10,10)


dia, mes, ano = int(data1[:2]), int(data1[3:5]), int(data1[6:10])
dia2, mes2, ano2 = int(data[:2]), int(data[3:5]), int(data[6:10])


data_maior = date(ano, mes, dia)
data_menor = date(ano2, mes2, dia2)

dic = {'ID': 'AccCtrl', 'jvitor.silva': '14/03/2019', 'v.tassinari': '', 'nf.figueiredo': '29/08/2019', 'lg.santos': '16/01/2019', 'g.brandao': '23/07/2019', 'm.bezerra': '21/08/2019'}
sistema = dic.pop("ID")
dic_2 = dic.copy()
for key in dic_2.keys():
    if dic.get(key) == "":
        dic.pop(key)

print(dic)
print(sistema)

ultimo = OrderedDict(sorted(dic.items(), key=lambda t: date(int(t[1][6:]), int(t[1][3:5]), int(t[1][:2])))).popitem()
print(ultimo)

t1 = '17/08/2018'
t2 = '31/07/2018'
print(t1 < t2)

str_date = '11/07/2018'
date = datetime.strptime(str_date, '%d/%m/%Y').date()
print(date, type(date))