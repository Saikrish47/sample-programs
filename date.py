import datetime
# from dateutil.relativedelta import relativedelta
#
# d=datetime.datetime.today()
# print(d)
# bday=datetime.datetime(2019,5,30,9,00,00,100000)
#
# tbday=bday -
# print(tbday)

# print('enter the year')
year=input('enter the year: ')
# print('enter the month')
month=input('enter the month: ')

# print('enter the date')
date=input('enter the date: ')

#
# year=datetime.datetime.year()
# month=datetime.datetime.month()
# date=datetime.datetime.date()

bday= f'{date} {month},{year}'
# m=datetime.datetime(bday)

m=datetime.datetime.strptime(bday,'%d %m,%Y')
tdy=datetime.datetime.today()
r=(tdy-m)
# p=datetime.datetime.timedelta(tdy-m)
print(r)
# print(bday)
