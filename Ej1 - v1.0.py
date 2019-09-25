from collections import Counter

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
frecuencia = [12.781, 1.617, 3.678, 5.057, 13.270, 0.509, 1.187, 1.179, 5.181, 0.581,   #a, b, c, d, e, f, g, h, i, j
              0.002, 5.606, 3.114, 6.548, 0.208, 9.485, 2.546, 1.498, 6.690, 7.594, 3.971,     #k, l, m, n, ñ, o, p, q, r, s, t
              4.782, 1.240, 0.001, 0.079, 1.192, 0.403] # u, v, w, x, y, z

c = "xqxpwggoyffaoeqjjvmaefyjpvouuvnfalvfgtujuvqbñhxeuqbfrmrrcqwwwekqñfjwrrpqqhftvguxwsrmpfhrfeccitededntjñsothgffaoepupwwrjuktuaoebiyhñadbjfosnlqdjufokqdrxwslequrlitufrxfpgofqdlpvefwhuodqdidkirdljrxrvmsfohsrxwtssrryfxwkajñljpsvgxlrwsdhhuxuwacyurwwnvouxlmadbjjñsctqjtddoklqhleivzktvvecuknrluxuuwrjuvcfideokbvwhuejxqihñochsnrfdvxfxwwrjuktuaoknsfotigpuzpmrrgflhfejbjtssrrxqjailggqhlhnuqbtvqatucnhftgftjñlacnifssrvzkjownlqupmwfvzulruirpfwwaeeqqxsarroytpwsheuxlveeoyfñwshbiprjuvxuhrfvzqdjrttvzuwxftjulrihpgclplltrcfwñhqmqswhhqmqqhhitreyfgsrebjzpmrrgfahftrvfxrlivygwhjuvnblxfakpupdlccnlxxdakzfxhsnhhrpluaktqxwsdgztjvwnzzwzphdvxfxwwrjuktuaokbszssdgfknhfezygtumaeoyfhltjnkjjacrcfwñhqmqjzjaejbhzhioueyfohstqtjudokpupwhdgburssrlqqlxsrubyrvmrmosnrfek"

repeticiones = []
ocurrencias = []
mcds = []
    
####################################
#           ENCRIPTAR
####################################
# Obtiene el siguiente alfabeto en usar
def siguientealfabeto(letra):
    global estado
    global alfabeto

    index = alfabeto.index(letra)
    
    estado = alfabeto[index:27]+alfabeto[0:index]

# Encripta usando el cifrado Vignere
def encriptar(mensaje, llave):
    mensaje = mensaje.lower()
    llave = llave.lower()
    criptograma = ""
    i = 0
    
    for letra in mensaje:
        if i == len(llave):
            i = 0
        pos = alfabeto.find(letra) + alfabeto.find(llave[i])
        if pos > 26:
            pos = pos-27
        criptograma += alfabeto[pos]
        i += 1
    return criptograma

####################################
#           DESENCRIPTAR
####################################
# Función para desencriptar con la llave
def desencriptar(criptograma, llave):
    criptograma = criptograma.lower()
    llave = llave.lower()
    mensaje = ""
    i = 0
    
    for letra in criptograma:
        if i == len(llave):
            print("-",end="")
            i = 0
        pos = alfabeto.find(letra) - alfabeto.find(llave[i])
        if pos < 0:
            pos += 27
        print(alfabeto[pos],end="")
        mensaje += alfabeto[pos]
        i += 1
    #return mensaje

# Revisa si la repetición ya está agregada en la lista de repeticiones
def existe(repeticion):
    global repeticiones

    for rep in repeticiones:
        if rep[0] == repeticion:
            return True
        continue
    return False

# Obtiene el indice de cierta repeticion en la lista de repeticiones
def buscar(repeticion):
    contador = 0
    for rep in repeticiones:
        if rep[0] == repeticion:
            break
        contador += 1
    return contador

# Obtiene Maximo Comun Divisor de dos números
def mcd(x, y):
    while(y):
        x, y = y, x % y

    return x

# Obtiene el Maximo Comun Divisor de todas las distancias de cierto n-grama
def maximoComunDivisor():
    global repeticiones
    
    for rep in repeticiones:
        if(len(rep[1])>1):
            val = rep[1][0]
            for distancia in rep[1]:
                if(distancia == val):
                    continue
                val = mcd(val, distancia)
            rep[2] = val;

#Obtiene el posible largo de la clave
def posibleLargoClave():
    global repeticiones
    global ocurrencias
    global mcds
    
    for rep in repeticiones:
        if(rep[2]>0):
            if(ocurrencias == [] or rep[2] not in mcds):
                mcds += [rep[2]]
                ocurrencias += [1]
            if(rep[2] in mcds):
                ocurrencias[mcds.index(rep[2])] += 1
    return getLargoClave()

# Se usa esta función para buscar en el mensaje las ocurrencias de cierto n-grama
def analizar_aux(mensaje, ngrama):
    global repeticiones
    
    index = 0
    contador = 0
    while(index < len(mensaje)):
        repeticion = mensaje[index:index+ngrama]
        if(len(repeticion)<ngrama):
            break
        elif existe(repeticion):
            repeticiones[buscar(repeticion)][1] += [index]
            index += 1
        else:
            repeticiones += [[repeticion, [index],0]]
            index += 1

def printNGramas():
    global repeticiones
    n = 2
    for rep in repeticiones:
        if(len(rep[0])>n):
            n+=1
            print("=====================================")
            print(" GRAMAS DE", n, "CARACATERES OBTENIDOS")
            print("=====================================")
        if(len(rep[1])>1):
            print(rep)

def getLargoClave():
    global ocurrencias
    global mcds
    print("Posibles longitudes de clave")
    contador = 0

    maxOcurrencias = 0
    longitud = 0
    print()
    while(contador<len(ocurrencias)):
        if(mcds[contador] > 3 and mcds[contador] < 20 and maxOcurrencias < ocurrencias[contador]):
            maxOcurrencias = ocurrencias[contador]
            longitud = mcds[contador]
        print("Longitud: ",mcds[contador], "\tOcurrencias: ", ocurrencias[contador])
        contador += 1
    print("\nEl número con mayor cantidad de ocurrencias distinto de 1, 2 y 3(irrealista) es",longitud,"con", maxOcurrencias, "\n")
    return longitud
    
def acomodarPorLargoClave(largo):
    global c
    mensaje = [[]]
    i = 0
    j = 0
    
    for letra in c:
        if i == largo:
            mensaje += [[]]
            j += 1
            i = 0
        mensaje[j] += [letra]
        i += 1
    count = 0

    for block in mensaje:
        if(count == 6):
            print()
            count = 0
        print(block, end="")
        count +=1
    print()
    
    return mensaje

# Busca los n-gramas en un criptograma con n = 3, ..., 6
def analyze():
    global c
    global frecuencia
    global alfabeto
    
    i = 3
    # Analiza el criptograma en busqueda de n-gramas de 1 a 3
    while(i<=16):
        analizar_aux(c, i)
        i += 1

    # Obtiene el Maximo Comun Divisor de las distancias
    maximoComunDivisor()

    printNGramas()
    # Imprime las posibles longitudes de claves
    largoLlave = posibleLargoClave()

    mensaje = acomodarPorLargoClave(largoLlave)

    print("Division del criptograma según la longitud obtenida:")
    results = []
    submensaje = ""
    i = 0
    while i < largoLlave:
        for block in mensaje:
            if(len(block)<largoLlave):
                break
            else:
                submensaje += block[i]
        results += [Counter(submensaje)]
        submensaje = ""
        i += 1

    print("Frecuencias por carácter y por columna:")
    key = ""
    i = 0
    while i < 27:
        key = ""
        for res in results:
            if(len(res) <= i):
                print("", end="\t\t")
                if res == results[-1]:
                    print()
            else:
                letra = res.most_common()[i][0]
                frec = res.most_common()[i][1]
                print(letra,'%.1f'%(frec*frecuencia[alfabeto.find(letra)]), end = "\t\t")
                key += letra
                if res == results[-1]:
                    print()
        i += 1
        #print("\n",key)
analyze()
