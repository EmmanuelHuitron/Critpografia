import fileinput


suma = 0
for i in fileinput.input(): 
	num = float (i)
	suma= suma+num
total = str(suma) 
totalint = str(int(suma))
dec = ".0" 
cadena = totalint+dec 
res = int(suma)
if cadena==total:
	res = int(suma)
	print(res)

if cadena!=total:
	res = float(suma)
	print(res)

