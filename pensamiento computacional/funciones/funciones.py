def nombre_completo(nombre,apellido,inverso=False):
	if inverso:
		return(f'{apellido} {nombre}')
	else:
		return(f'{nombre} {apellido}')

print(nombre_completo('Gustavo','Barboza'))
print(nombre_completo('Gustavo','Barboza',inverso=True))
print(nombre_completo(apellido='Barboza',nombre='Gustavo'))
#tanto por orden de argumentos o por keywords python logra
#reconocer las funciones.

