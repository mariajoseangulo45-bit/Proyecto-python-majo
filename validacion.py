def validarEntero(mensaje):
    try:
        dato=int(input(mensaje))
        if dato<0:
            print("Ingrese un valor positivo: ")
            return None
        return dato
    except:
        print("Ingrese un valor positivo: ")
        return None
    
def validarDecimal(mensaje):
    try:
        dato=float(input(mensaje))
        if dato<0:
            print("Ingrese un valor positivo: ")
            return None
        return dato
    except:
        print("Ingrese un valor positivo: ")
        return None

    
def validarMenu(mensaje,minimo,maximo):
    try:
        dato=int(input((mensaje)))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None
    
def nombre_valido(nombre):
    #strip elimina los espacios
    if nombre.strip()=="":
        print("Nombre vacio")
        return False
    return True

