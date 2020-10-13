def main():
	#Se define la llave
	key='ENCRYPT'
  #Se lee la entrada
  lines = []
  for line in fileinput.input():
    lines.append(line)
	choice=lines[0].replace("\n","")
	plain_text=input()
  text = lines[1].replace(" ","") 
  text = text.replace("\n","")
	matrix = definirMatriz(m,key)
	finalPhrase='';
	if(option=='ENCRYPT'):
		finalPhrase=encrypt(matrix,text,m)
	else:
		finalPhrase=decrypt(matrix,text,m)

	print(finalPhrase)
