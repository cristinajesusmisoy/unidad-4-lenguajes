import re  


path = "archivo.txt"
codigo = "codigobasico.txt"


try:
    archivo1 = open(codigo, 'r')
except:
    
    print("no se encuentra el archivo codigo")
    quit()

muestracodigo = ""

for linea1 in archivo1:
    muestracodigo += linea1


try:
    archivo = open(path, 'r')
except:
    print("El archivo no se encuentra")
    quit()

texto = ""

for linea in archivo:
    texto += linea

print("\n selecciona una opcion")
print("1.Variables válidas\n2.Enteros\n3.Decimales\n4.Operadores aritmeticos\n5.Operadores relacionales\n6.Palabras reservadas")
opcion = int(input("ingrese una opción: "))
    if opcion == 1:
        patronVARIABLES = r'(\b[A-Za-z0-9-_]+\s*[=])+'
        resultadoVARIABLES = re.findall(patronVARIABLES, muestracodigo)
        print("Las variables que estan declaradas son: ",
      resultadoVARIABLES)  
      print("")  
      
        else:
            print("No hay Variables válidas") 
    elif opcion == 2:
        patronENTERO = r'[+,-]?[0-9]+'
        resultadoENTERO = re.findall(patronENTERO, texto)
        print("Los numeros enteros del archivo son: ", resultadoENTERO)
        print("")
        
        else:
            print("No hay Enteros") 
    elif opcion == 3:
        patronDECIMAL = r'[+,-]?[[0-9]*[.]]?[0-9]+'
        resultadoDECIMAL = re.findall(patronDECIMAL, texto)
        print("Los numeros decimales del archivo son: ", resultadoDECIMAL)
        print("")
        else:
            print("no hay decimales") 
    elif opcion == 4:
         patronARITMETICO = r'[\d+]+\s*[\+|\-|\*|\/]+\s*[\d+]+'
        resultadoARITMETICO = re.findall(patronARITMETICO, texto)
        print("Los operadores aritmeticos del archivo son: ", resultadoARITMETICO)
        print("")   
        else:
            print("No hay Operadores aritmeticos")
    elif opcion == 5:
        patronRELACIONAL = r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=]=+\s*[A-Za-z0-9|a-z0-9])+'
        resultadoRELACIONAL = re.findall(patronRELACIONAL, texto)
        print("Los operadores relacionales identificados son: ", resultadoRELACIONAL)
        print("")
        else:
            print("no hay Operadores relacionales")

    elif opcion == 6:
        patronRESERVADAS = r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
        resultadoRESERVADAS = re.findall(patronRESERVADAS, muestracodigo)
        print("LAS PALABRAS RESERVADAS SON: ", resultadoRESERVADAS)
        print("")
        else:
            print("no hay Palabras reservadas")
    else:
        print("\n¡¡¡La opción Seleccionada es Incorrecta!!!")
        



