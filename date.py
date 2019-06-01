import datetime
year=input('enter the year: ')
month=input('enter the month: ')
date=input('enter the date: ')

bday= f'{date} {month},{year}'

m=datetime.datetime.strptime(bday,'%d %m,%Y')
tdy=datetime.datetime.today()
r=(tdy-m)
print(r)
