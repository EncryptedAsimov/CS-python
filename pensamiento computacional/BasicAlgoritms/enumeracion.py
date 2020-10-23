objetivo = int(input('Escoge un entero '))
respuesta = 0

while respuesta**2 < objetivo:
	respuesta += 1 

if respuesta**2 == objetivo:
	print(f'la raiz cuadrada de {objetivo} es {respuesta}')
else:
	print('El numero no tiene raiz cuadrada perfecta')