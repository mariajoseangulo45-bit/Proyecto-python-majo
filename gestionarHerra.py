from gestionarJson import cargar, guardar, generar_id
from validacion import validarEntero,nombre_valido, validarDecimal
from logs import logs_stock, logs_nombres
ARCHIVO1="herramienta.json"


def guardar_herramienta():
    herramienta=cargar(ARCHIVO1)
    tipo=input("Ingrese construccion o jardineria: ")
    nombre=input("Ingrese el nombre de la herramienta: ")
    logs_nombres()

    if nombre_valido(nombre)==False or existeNombre(nombre)==True:
        nombre=input('Ingrese el nombre de la herramienta valido')
        logs_nombres()
        return
        
    
    stock=validarEntero("Ingrese la cantidad: ")
    if stock==0:
        estado="NO DISPONIBLE"
    if stock>0:
         estado="DISPONIBLE"

    costo=validarDecimal("Ingrese el costo del prestamo: ")
        #crear ususario y admi y guardar 
    nueva_persona={
        "id": generar_id(herramienta),
        "tipo": tipo,
        "nombre": nombre,
        "stock": stock,
        "estado": estado,
        "costo prestamo": costo
    }
    herramienta.append(nueva_persona)
    guardar(ARCHIVO1,herramienta)
    print("HERRAMIENTA GUARDADA CORRECTAMENTE!")

def existeNombre(nombre):
    herramienta=cargar(ARCHIVO1)
    for elemento in herramienta:
        if nombre.lower() == elemento["nombre"].lower():
            return True
    return

def actualizar_herramienta():
    herramienta=cargar(ARCHIVO1)
    listar_herramienta()

    while True:
        encontrado=False
        
        id_herramienta=validarEntero("Escoja el id a actualizar o presione 0 para salir: ")
        while id_herramienta==None:
            id_herramienta=validarEntero("Error, escoja el id a actualizar: ")
        if id_herramienta == 0:
            print("Saliendo...")
            return  

        for validar in herramienta:
            if str(id_herramienta).strip()==str(validar["id"]).strip():
                encontrado=True

                while True:
                    op=int(input('''
                        Bienvenido
                        1. Actualizar tipo
                        2. Actualizar nombre
                        3. Actualizar stock
                        4. Actualizar costo prestamo
                        5. Salir
                                
                    '''))
                    match op:
                            case 1:
                                        tipo=input('Ingrese el nuevo tipo: ')
                                        while nombre_valido(tipo)==False:
                                            tipo=input('Ingrese nombre valido: ')
                                            logs_nombres()
                                        validar["nombre"]=tipo
                                        guardar(ARCHIVO1, herramienta)
                                        print('tipo actualizado!')
                            case 2:
                                nombre=input('Ingrese el nombre nuevo ')
                                while nombre_valido(nombre)==False:
                                        nombre=input('Ingrese nombre valido: ')
                                        validar["nombre"]=nombre
                                        guardar(ARCHIVO1, herramienta)
                                        print('Nombre actualizado!')        
                            case 3:
                                stock=validarEntero('Ingrese el nuevo stock: ')
                                validar["stock"]=stock
                                validar["estado"] = "DISPONIBLE" if stock > 0 else "NO DISPONIBLE"
                                guardar(ARCHIVO1, herramienta)
                                print('Stock actualizado!')
                            case 4:
                                        costo=input('Ingrese el nuevo costo: ')
                                        validar["costo"]=costo
                                        guardar(ARCHIVO1, herramienta)
                                        print('Costo actualizado!')
                            case 5:
                                print('Actualizado correctamente')
                                return
                            case _:
                                print('Ingrese un id valido: ')
                    break
                break
        if not encontrado:
            ("Herramienta no encontrada")
        continue

def listar_herramienta():
    herramienta=cargar(ARCHIVO1)

    if not herramienta:
        print("No hay herramienta \n")
        return
    for elemento in herramienta:
        print("----")
        print(f'ID: {elemento["id"]} --> {elemento["nombre"]}')

def eliminar_herramienta():
    contador_aux=0
    herramienta=cargar(ARCHIVO1)
    listar_herramienta()
    id_herramienta=validarEntero("Escoja el id a eliminar: ")
    while(id_herramienta==None):
        id_herramienta=validarEntero("ERROR, escoja un id válido a eliminar: ")
    
    for elemento in herramienta:
        if id_herramienta==elemento["id"]:
            herramienta.pop(contador_aux)
            guardar(ARCHIVO1, herramienta)
            print('¡Herramienta eliminada correctamente!')
            return
        contador_aux+=1
    print("La herramienta no existe. \n")

#usuario
def listar_herramienta1():
    herramienta=cargar(ARCHIVO1)

    if not herramienta:
        print("No hay herramienta \n")
        return
    for elemento in herramienta:
        print("----")
        for clave, valor in elemento.items():
            print(f'{clave}:{valor}')
    return herramienta

#stock usuario
def stock_herramienta():
        herramienta=cargar(ARCHIVO1)
        
        id_herramienta=validarEntero("Escoja el id de la herramienta que desea tomar: ")
        while id_herramienta==None:
            id_herramienta=validarEntero("Error, escoja el id de la herramienta que desea tomar: ")

        cantidad=int(input("Ingrese la cantidad de herramientas: "))
        while cantidad is None:
             #validar real 
             cantidad=validarEntero("Error, ingrese una cantidad valida: ")

        
        encontrado=None
        for validar in herramienta:
            if str(id_herramienta).strip()==str(validar["id"]).strip():
                encontrado=validar
                break
                
        if not encontrado:
             print("Herramienta no encontrada")
             return False

        if cantidad> encontrado["stock"]:
            print(f'No hay suficiente stock. Solo hay {encontrado["stock"]} disponobles')
            logs_stock()
            return
         
        if cantidad<= encontrado["stock"]:
            encontrado["stock"] -= cantidad
            print(f'Prestadas {cantidad} de {encontrado["nombre"]}. Stock restante: {encontrado["stock"]}')
        
        costo_unidad=float(encontrado["costo prestamo"])
        costo_prestamo=cantidad*costo_unidad
        print("El costo del prestamo es de", costo_prestamo)
        
            #guardar en el json actualizado
        guardar(ARCHIVO1, herramienta)

        return id_herramienta, cantidad, costo_prestamo
    





