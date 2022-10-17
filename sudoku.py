
rows, cols = (9, 9)
sudoku = [[0 for i in range(cols)] for j in range(rows)]
# sudoku[0]=[0,0,6,0,9,0,0,5,0]
# sudoku[1]=[8,3,4,0,0,5,0,0,0]
# sudoku[2]=[5,9,1,2,8,0,0,6,0]
# sudoku[3]=[0,0,0,4,3,0,0,0,2]
# sudoku[4]=[0,0,9,7,0,1,5,4,8]
# sudoku[5]=[0,0,8,5,0,0,6,7,0]
# sudoku[6]=[1,0,0,9,7,0,4,0,5]
# sudoku[7]=[0,0,3,0,0,0,0,1,6]
# sudoku[8]=[6,4,0,0,5,0,2,8,0]
#print(arr)

def seleccionar_numero(sudoku, numero ,i , j):
	
	volver = True
	if(i==9):
		return sudoku
	if(numero>9):
		return False

	sudoku[i][j]=numero
	print(sudoku)

	if(comprobar(sudoku)==True): 
		while volver:								#SABER QUE POSICION 
			iSiguiente, jSiguiente = siguiente(i,j)
			if(sudoku[iSiguiente][jSiguiente]==0):
				volver = False
			print("intentando...")
		print("ANTES DE PROBAR LA SIGUIENTE")
		sudokuAnterior = sudoku
		print(sudoku)
		P = seleccionar_numero(sudoku, 1, iSiguiente, jSiguiente)
		print("AAAA%", P)
		if(P==False):

			print("OIDO COCINA")
			print(sudokuAnterior)
			return seleccionar_numero(sudokuAnterior, numero+1,i,j)
	else:
		if(numero>8):
			print("AHORAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
			return False
		return seleccionar_numero(sudoku, numero+1, i, j)

	return True


	

def siguiente(i, j):
	j += 1
	if(j>8):
		i += 1
		j = 0
	return (i, j)





def comprobar_completo(sudoku):
	for i in range(9):
		for j in range(9):
			if(sudoku[i][j]==0):
				return False
	return True

def comprobar(sudoku):
	print("columnas")
	if(comprobar_columnas(sudoku)==False):
		return False
	print("filas")
	if(comprobar_filas(sudoku)==False):
		return False
	print("cuadrados")
	if(comprobar_cuadrados(sudoku)==False):
		return False

	return True

def generar_cuadrado(sudoku, it):
	cuadrado = set()
	i0=3*int(it/3)
	for i in range(i0,3+i0):
		j0=3*(it%3)
		for j in range(j0,3+j0):
			x = sudoku[i][j]
			#print(str(i)+"\t"+str(j))
			if(x != 0):
				cuadrado.add(x)
	#print(cuadrado)
	return cuadrado

def comprobar_filas(sudoku):
	for i in range(9):
		fila = sudoku[i]
		#print(fila)
		if(comprobar_duplicados(fila)== False):
			return False
	return True 

def comprobar_columnas(sudoku):
	for j in range(9):
		#print("j: "+str(j))
		columna = [10,11,12,13,14,15,16,17,18,19]
		for i in range(9):
			#print("i: "+str(i)+"  j: "+str(j))
			x = sudoku[i][j]
			#print(x)
			if(x != 0):
				columna[i]=x
		#print(columna)
		if(comprobar_duplicados(columna)==False):
			return False
	return True

def comprobar_duplicados(conjunto):
	numeros=[0,0,0,0,0,0,0,0,0]
	vacio = set()
	if(conjunto != vacio):
		dup=set()
		#print(conjunto)
		for x in conjunto:
			if(x<10 and x>0):
				numeros[x-1]+=1
				if(numeros[x-1]>1):
					dup.add(x)	
		if(dup != vacio):
			return False 
	return True

 
 #    print(dup)  # [1, 5, 1]
	
	# nums = [1, 5, 2, 1, 4, 5, 1]
 
 #    dup = {x for x in nums if nums.count(x) > 1}
 #    print(dup)  # {1, 5}

# comprobar_columnas(sudoku)
def comprobar_cuadrados(sudoku):
	for i in range(9):
		cuadrado=generar_cuadrado(sudoku,i)
		if(comprobar_duplicados(cuadrado)==False):
			return False
	return True





resolver(sudoku)



	