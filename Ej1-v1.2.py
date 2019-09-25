from collections import Counter

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
frecuencia = [12.781, 1.617, 3.678, 5.057, 13.270, 0.509, 1.187, 1.179, 5.181, 0.581,   #a, b, c, d, e, f, g, h, i, j
              0.002, 5.606, 3.114, 6.548, 0.208, 9.485, 2.546, 1.498, 6.690, 7.594, 3.971,     #k, l, m, n, ñ, o, p, q, r, s, t
              4.782, 1.240, 0.001, 0.079, 1.192, 0.403] # u, v, w, x, y, z

c = "xqxpwggoyffaoeqjjvmaefyjpvouuvnfalvfgtujuvqbñhxeuqbfrmrrcqwwwekqñfjwrrpqqhftvguxwsrmpfhrfeccitededntjñsothgffaoepupwwrjuktuaoebiyhñadbjfosnlqdjufokqdrxwslequrlitufrxfpgofqdlpvefwhuodqdidkirdljrxrvmsfohsrxwtssrryfxwkajñljpsvgxlrwsdhhuxuwacyurwwnvouxlmadbjjñsctqjtddoklqhleivzktvvecuknrluxuuwrjuvcfideokbvwhuejxqihñochsnrfdvxfxwwrjuktuaoknsfotigpuzpmrrgflhfejbjtssrrxqjailggqhlhnuqbtvqatucnhftgftjñlacnifssrvzkjownlqupmwfvzulruirpfwwaeeqqxsarroytpwsheuxlveeoyfñwshbiprjuvxuhrfvzqdjrttvzuwxftjulrihpgclplltrcfwñhqmqswhhqmqqhhitreyfgsrebjzpmrrgfahftrvfxrlivygwhjuvnblxfakpupdlccnlxxdakzfxhsnhhrpluaktqxwsdgztjvwnzzwzphdvxfxwwrjuktuaokbszssdgfknhfezygtumaeoyfhltjnkjjacrcfwñhqmqjzjaejbhzhioueyfohstqtjudokpupwhdgburssrlqqlxsrubyrvmrmosnrfek"

ngramas = []
ocurrencias = []
mcds = []

####################################
#           ENCRIPTAR
####################################
# Encripta usando el cifrado Vignere
def encriptar(mensaje, llave):
    #Pone el mensaje y la llave en minuscula para asegurar está limpio
    mensaje = mensaje.lower(); llave = llave.lower()

    criptograma = ""
    i = 0

    for letra in mensaje:
        if i == len(llave): #Si el indice es del mismo tamaño que la llave, entonces lo reinicia
            i = 0

        pos =  alfabeto.find(letra) + alfabeto.find(llave[i])       #Obtiene la siguiente posición de letra para el criptograma. Lo hace sumando
                                                                    #la posición de la letra del mensaje y de la llave en el alfabeto.
        criptograma += alfabeto[pos%len(alfabeto)]                  #Hace modulo el largo del alfabeto para asegurar que esta en el mismo
        i += 1
    return criptograma

####################################
#           DESENCRIPTAR
####################################
# Desencripta usando el cifrado Vignere
def desencriptar(criptograma, llave):
    #Pone el mensaje y la llave en minuscula para asegurar está limpio
    criptograma = criptograma.lower(); llave = llave.lower()

    mensaje = ""
    i = 0

    for letra in criptograma:
        if i == len(llave): #Si el indice es del mismo tamaño que la llave, entonces lo reinicia
            i = 0

        pos = alfabeto.find(letra) - alfabeto.find(llave[i])        #Obtiene el siguiente caracter del mensaje.
        if pos < 0:                                                 #Si es menor que 0 le suma 27 para asegurar
            pos += len(alfabeto)                                    #que está en el alfabeto

        mensaje += alfabeto[pos]
        i += 1
    return mensaje


####################################
#    ROMPER EL CIFRADO VIGNERE
####################################
# Obtiene Maximo Comun Divisor de dos números usando el metodo de la division euclidea
def mcd(x, y):
    while(y):               # Ejecuta el proceso hasta que y sea 0
        x, y = y, x % y     # x = y; y = x % y; Se basa en como funcionan las tuplas en python
                            # y su capacidad de ser intercambiables.
    return x

# Obtiene el Maximo Comun Divisor de todas las distancias de cierto n-grama, que se haya repetido en más de una ocasión
def maximoComunDivisor():
    global ngramas

    for rep in ngramas:
        if(len(rep[1])>=2):                  #Si se repite por lo menos 2 veces
            val = rep[1][0]                  #Setea como valor la primer distancia
            for distancia in rep[1]:
                val = mcd(val, distancia)    #Actualiza el valor con el mcd, del valor anterior y la nueva distancia
            rep[2] = val                     #Asigna en la lista el mcd

# Imprime todos los ngramas que tengan repeticiones
def printNGramas():
    global ngramas

    n = 2       #se salta los ngramas menores de 2 caracteres
    for rep in ngramas:
        if(len(rep[0])>n):
            n+=1
            print("=====================================")
            print(" GRAMAS DE", n, "CARACATERES OBTENIDOS")
            print("=====================================")
        if(len(rep[1])>1):
            print(rep[0], "Distancias:", rep[1], "MCD:", rep[2])

# Obtiene el posible largo de la clave
def largoClave():
    global ngramas
    global ocurrencias
    global mcds

    maxOcurrencias = longitud = 0

    for rep in ngramas:
        if(rep[2]>0):   #Si el cmd del ngrama es mayor que 0
            if(ocurrencias == [] or rep[2] not in mcds):    # Si la lista de ocurrencias de mcd está vacia o el cmd no está en su lista correspondiente
                mcds += [rep[2]]                            # Agrega el mcd a la lista
                ocurrencias += [1]                          # Agrega uno a las ocurrencias de ese mcd a la lista
            if(rep[2] in mcds):                             # Si el mcd ya está en la lista
                ocurrencias[mcds.index(rep[2])] += 1        # Se le suma uno a la lista de ocurrencias de cmds.

    print("\nPosibles longitudes de clave")
    for contador in range(len(ocurrencias)):
        # Si el mcd de la posición es mayo que cero y menor que veinte
        # y la ocurrencia de ese cmd es mayor a la que está actualmente marcada como máxima
        if(mcds[contador] > 3 and mcds[contador] < 20 and maxOcurrencias < ocurrencias[contador]):
            maxOcurrencias = ocurrencias[contador]
            longitud = mcds[contador]
        print("Longitud: ",mcds[contador], "\tOcurrencias: ", ocurrencias[contador])

    print("\nEl número con mayor cantidad de ocurrencias distinto de 1, 2 y 3(irrealista) es",longitud,"con", maxOcurrencias, "\n")
    return longitud     #retorna la longitud de la clave

# Acomoda el texto en grupos de un largo dado
def acomodarPorLargoClave(largo, criptograma):
    mensaje = [[]]
    i = j = 0

    for letra in criptograma:
        if i == largo:          # Si ya se llego al largo del criptograma
            mensaje += [[]]     # Agrega un nuevo bloque
            j += 1              # Agarra la siguiente posición del nuevo bloque
            i = 0               # Reinicia el indice
        mensaje[j] += [letra]   # Agrega la letra al mensaje
        i += 1                  # Incrementa el indice

    i = 1
    for i in range(len(mensaje)):
        if (i)%3 == 0:            # Si ya se llego al corte
            print()                 # Salto de línea
        print(mensaje[i-1], end="")   # Imprime el bloque
    print("\n")

    return mensaje

# Revisa si algún n-grama ya está agregado en la lista de ngramas
def existe(repeticion):
    global ngramas

    for rep in ngramas:
        if rep[0] == repeticion:    #Si está, retorna True
            return True
    return False                    #Si sale del for retorna False

# Obtiene el indice de cierta repeticion en la lista de ngramas
def buscar(repeticion):
    if(not existe(repeticion)):         #Si el ngrama no existe retorna -1
        return -1

    contador = 0
    for rep in ngramas:
        if rep[0] == repeticion:
            break                       #Cuando encuentra el ngrama, sale del for y retorna el contador
        contador += 1

    return contador

# Se usa esta función para buscar en el mensaje las ocurrencias de cierto n-grama
def analizar_aux(mensaje, ngrama):
    global ngramas

    contador = 0
    while(contador < len(mensaje)):
        repeticion = mensaje[contador:contador+ngrama]  #Obtiene el ngrama del mensaje
        if(len(repeticion)<ngrama):                     #Si el tamaño de la repetición es menor que el ngrama, no hay que revisarlo
            break
        else:
            indice = buscar(repeticion)                 #Busca el indice del ngrama en la lista de ngramas
            if indice == -1:                            #Si no lo encuentra, es que no está
                ngramas += [[repeticion, [contador],0]] #Entonces lo agrega
            else:
                ngramas[indice][1] += [contador]        #Si está, agrega la posición del ngrama a la lista de distancias.
            contador += 1

# Busca los n-gramas en un criptograma con n = 3, 4, 5, ...
def analyze():
    global c
    global frecuencia
    global alfabeto

    i = 3
    # Analiza el criptograma en busqueda de n-gramas de 3 a 8 caracteres
    while(i<=8):
        analizar_aux(c, i)
        i += 1

    # Calcula el Maximo Comun Divisor de las distancias
    maximoComunDivisor()
    printNGramas()

    # Imprime las posibles longitudes de claves
    largoLlave = largoClave()

    print("Division del criptograma según la longitud obtenida:")
    mensaje = acomodarPorLargoClave(largoLlave, c)

    results = []
    submensaje = ""

    for i in range(largoLlave):
        for block in mensaje:
            if(len(block)<largoLlave):      # Si el largo del bloque es igual al largo de la llave se sale
                break
            else:
                submensaje += block[i]      # Se agrega al submensaje la letra del bloque en cierta columna
        results += [Counter(submensaje)]    # Se hace una cuenta de la cantidad de caracteres y la guardan
        submensaje = ""                     # Limpia el submensaje

    print("Frecuencias de carácter por cada columna: (caracter, frecuencia en columna, frecuencia en columna multiplicado a la frecuencia letra en alfabeto español)")
    for i in range(len(alfabeto)):
        key = ""
        for res in results:
            if(len(res) <= i):
                print("", end="\t\t")
                if res == results[-1]:
                    print()
            else:
                letra = res.most_common()[i][0]
                frec = res.most_common()[i][1]
                print(letra, frec, '%.1f'%(frec*frecuencia[alfabeto.find(letra)]), end = "   \t")
                if res == results[-1]:
                    print()

analyze()
