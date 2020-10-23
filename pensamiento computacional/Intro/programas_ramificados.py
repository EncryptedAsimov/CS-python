num_1 = int(input('Escoge un entero: '))
num_2 = int(input('Escoge otro entero: '))

if num_1 > num_2:
	print(f'El {num_1} es mayor que el {num_2}')
elif num_2 > num_1:
	print(f'El {num_2} es mayor que el {num_1}')
else:
	print('Ambos numeros son iguales')
