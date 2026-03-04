from gestionarJson import cargar, guardar, generar_id
from validacion import validarEntero,nombre_valido
from logs import logs_nombres

ARCHIVO="personas.json"

def guardar_persona():
    persona=cargar(ARCHIVO)

    nombre=input("Ingrese el nombre completo: ")
    logs_nombres()
    while nombre_valido(nombre)==False or existeNombre(nombre)==True:
        nombre=input('Ingrese el nombre de la persona valida: ')
        logs_nombres()
    telefono=validarEntero("Ingrese su numero de telefono: ")
    direccion=input("Ingrese la direccion: ")
    cargo=input("Ingrese si es usuario o administrador: ")
    clave=int(input("Asigne una clave al usuario: "))
        #crear ususario y admi y guardar 
    nueva_persona={
        "id": generar_id(persona),
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "cargo": cargo,
        "clave": clave
    }
    persona.append(nueva_persona)
    guardar(ARCHIVO,persona)
    print("¡PERSONA GUARDADA CORRECTAMENTE!")

def existeNombre(nombre):
    persona=cargar(ARCHIVO)
    for elemento in persona:
        if nombre.lower() == elemento["nombre"].lower():
            return True
    return 

def listar_persona():
    persona=cargar(ARCHIVO)

    if not persona:
        print("No hay persona \n")
        return[]
    for elemento in persona:
        print("----")
        for clave, valor in elemento.items():
            print(f'{clave}:{valor}')
    return persona 

def actualizar_persona():
    persona=cargar(ARCHIVO)
    listar_persona()

    while True:
        encontrado=False
        
        id_persona=validarEntero("Escoja el id a actualizar o presione 0 para salir: ")
        while id_persona==None:
            id_persona=validarEntero("Error, escoja el id a actualizar: ")
        if id_persona == 0:
            print("Saliendo...")
            return  


        for validar in persona:
            if str(id_persona).strip()==str(validar["id"]).strip():
                encontrado=True

                while True:
                    op=int(input('''
                    *********************
                        Bienvenido
                        1. Actualizar nombre
                        2. Actualizar telefono
                        3. Actualizar direccion
                        4. Salir
                                 
                    *********************           
                    '''))
                    match op:
                            case 1:
                                        nombre=input('Ingrese el nombre: ')
                                        while nombre_valido(nombre)==False:
                                            nombre=input('Ingrese nombre valido: ')
                                        validar["nombre"]=nombre
                                        guardar(ARCHIVO, persona)
                                        print('¡Nombre actualizado!')
                            case 2:
                                        telefono=validarEntero('Ingrese el nuevo numero: ')
                                        validar["telefono"]=telefono
                                        guardar(ARCHIVO, persona)
                                        print('¡Telefono actualizado!')
                            case 3:
                                        direccion=input('Ingrese la nueva direccion: ')
                                        validar["direccion"]=direccion
                                        guardar(ARCHIVO, persona)
                                        print('¡Direccion actualizada!')
                            case 4:
                                print('Actualizado correctamente')
                                return
                            case _:
                                print('Ingrese un id valido: ')
                    break
                break
        if not encontrado:
            ("Persona no encontrada")
        continue
    
                  
def eliminar_persona():
    contador_aux=0
    persona=cargar(ARCHIVO)
    listar_persona()
    id_persona=validarEntero("Escoja el id a eliminar: ")
    while(id_persona==None):
        id_persona=validarEntero("ERROR, escoja un id válido a eliminar: ")
    
    for elemento in persona:
        if id_persona==elemento["id"]:
            persona.pop(contador_aux)
            guardar(ARCHIVO, persona)
            print('¡Persona eliminada correctamente!')
            return
        contador_aux+=1
    print("La persona no existe. \n")



