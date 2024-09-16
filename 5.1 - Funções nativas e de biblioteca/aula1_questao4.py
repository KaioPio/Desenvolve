import datetime

datatual = datetime.datetime.now()
print(datatual)
datatext = datatual.strftime('%d/%m/%Y')
print (f"Data:{datatext}")
horaat = datatual.strftime('%H:%M')
print (f"Hora:{horaat}")