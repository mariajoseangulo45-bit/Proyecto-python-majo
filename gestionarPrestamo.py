from gestionarPerso import ARCHIVO,listar_persona
from validacion import validarEntero,validarDecimal
from gestionarJson import cargar,guardar
from datetime import date, timedelta
from gestionarHerra import ARCHIVO1,stock_herramienta,listar_herramienta1

ARCHIVO_PRESTAMO="prestamo.json"


def prestamos():
    prestamos=cargar(ARCHIVO_PRESTAMO)
    persona=cargar(ARCHIVO)
    print("Solicitud de prestamo")
    print(" ")

    while True:
        id_persona=validarEntero("Escoja el id para solicitar prestamo: ")
        while id_persona is None:
                id_persona=validarEntero("Error, escoja el id valido para solicitar prestamo: ")
        clave=validarEntero('Ingrese clave: ')

        encontrado=False
        persona_encontrada=None
        for validar in persona:
            if id_persona==validar["id"] and clave==validar["clave"]:
                encontrado=True
                persona_encontrada=validar
                break
        if encontrado:
            print("Acceso correcto")
            break
        else:
            print("ID o clave incorrecta. Intente de nuevo.\n")

    gestion_h=stock_herramienta()
    if not gestion_h:
        return
    

    fecha_inicio= date.today()
    print("Fecha inicio de prestamo ",fecha_inicio)
    dias=validarEntero("Ingrese la cantidad de dias que desea el prestamo")
    while dias<=0:
         dias=validarEntero("Ingrese un numero de dias valido: ")
    fecha_final=fecha_inicio+timedelta(days=dias)
    print("fecha de devolucion: ",fecha_final)

    print("Su solicitud ha sido enviada")

    if prestamos is None:
        prestamos = []
    
    datos={
        "id":id_persona,
        "persona":persona_encontrada["nombre"],
        "herramienta": gestion_h[0],
        "cantidad":gestion_h[1],
        "costo prestamo":gestion_h[2],
        "fecha_inicio":str(fecha_inicio),
        "fecha_devolucion":str(fecha_final)
    }
    
    prestamos.append(datos)
    guardar(ARCHIVO_PRESTAMO, prestamos)
    
    print(" ")
    print("*******************")
    print(" ")
    print("ID:", id_persona)
    print(" ")
    print("Persona:", persona_encontrada["nombre"])
    print(" ")
    print("Herramienta:", gestion_h[0])
    print(" ")
    print("Cantidad:", gestion_h[1])
    print(" ")
    print("Costo prestamo:",gestion_h[2])
    print(" ")
    print("Fecha inicio:", fecha_inicio)
    print(" ")
    print("Fecha devolución:", fecha_final)
    print(" ")
    print("*******************")
    
def listar_prestamos():
    prestamos=cargar(ARCHIVO_PRESTAMO)

    if not prestamos:
        print("No hay prestamos \n")
        return
    for elemento in prestamos:
        print("----")
        for clave, valor in elemento.items():
            print(f'{clave}:{valor}')


def herramienta_mas_solicitada():
    solicitudes=cargar(ARCHIVO_PRESTAMO)
    herramientas=listar_herramienta1()
    
    mayor_consulta=0
    nombre_herra=""
   
    for herramienta in herramientas:
        contador=0
        for prestamo in solicitudes:
            if herramienta["id"]==prestamo["herramienta"]:
                contador+=1
        if contador>mayor_consulta:
            mayor_consulta=contador
            nombre_herra=herramienta["nombre"]
    if mayor_consulta==0:
        print("No hay prestamos")
    else:
        print("")
        print("********************")
        print("")
        print(f"La herramienta mas solicitada es {nombre_herra} con {mayor_consulta} solicitudes")
        print("")
        print("********************")
    return

def usuario_mayorsoli():
    solicitudes=cargar(ARCHIVO_PRESTAMO)
    usuarios=listar_persona()
    mayor_consulta=0
    nombre_usuario=""

    for usuario in usuarios:
        contador=0
        for prestamo in solicitudes:
            if usuario["nombre"]==prestamo["persona"]:
                contador+=1
        if contador>mayor_consulta:
            mayor_consulta=contador
            nombre_usuario=usuario["nombre"]
    
    print("")
    print("********************")
    print("")
    print(f"El usuario con mayor numero de solicitudes es {nombre_usuario}")
    print("")
    print("********************")
    return

#tambien devuelve stock
def eliminar_prestamo():
    contador_aux=0
    prestamos=cargar(ARCHIVO_PRESTAMO)
    herramientas=cargar(ARCHIVO1)
    listar_prestamos()
    id_prestamo=validarEntero("Escoja el id a eliminar: ")
    while(id_prestamo==None):
        id_prestamo=validarEntero("ERROR, escoja un id válido a eliminar: ")
    
    for elemento in prestamos:
        if id_prestamo==elemento["id"]:
            for herramienta in herramientas:
                if str(herramienta["id"]).strip()==str(elemento["herramienta"]).strip():
                    herramienta["stock"]+=elemento["cantidad"]
                    print(f"Nuevo stock es {herramienta['stock']}")
            prestamos.pop(contador_aux)
            guardar(ARCHIVO_PRESTAMO, prestamos)
            guardar(ARCHIVO1,herramientas)
            print('¡Solicitud eliminada correctamente!')
            return
        contador_aux+=1
    print("El prestamo no existe. \n")