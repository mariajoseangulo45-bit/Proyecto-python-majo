from gestionarPerso import guardar_persona, actualizar_persona,listar_persona,eliminar_persona
from validacion import validarEntero,validarMenu
from gestionarHerra import actualizar_herramienta,guardar_herramienta,eliminar_herramienta,listar_herramienta1
from gestionarPrestamo import prestamos, listar_prestamos, herramienta_mas_solicitada,usuario_mayorsoli,eliminar_prestamo
from logs import listar_logs

CLAVE_AD="1234"


def menu():
     while True:
        op=validarEntero('''
            Bienvenido
            1. Usuario
            2. Administrador
            3. Salir
                     
        ''')
        match op:
            case 1:
                menu_usuario()
            case 2:
                        clave = input("Ingrese la clave de administrador: ")
                        if clave==CLAVE_AD:
                            print("Acceso concedido")
                            print("entrando al menu interno")
                            menu_admi()
                        else:
                             print("contraseña incorrecta")
                             break
            case 3:
                print('Salir')
                break
            case _:
                print('Opcion no encontrada')

#menu ADMINISTRADOR
def menu_admi():
            while True:
                        op=validarMenu('''
                            1. Menu Usuario
                            2. Menu Herramientas
                            3. Menu prestamos
                            4. Listar logs
                            5. Salir            
                        ''',1,5)
                        match op:
                            case 1:
                                persona()
                            case 2:
                                herramienta()
                            case 3:
                                menu_prestamos()
                            case 4:
                                listar_logs()
                            case 5:
                                print('Salir')
                                return
                            case _:
                                print('Opcion no encontrada')
#menu usuario-admi

def menu_prestamos():
     while True:
        op=validarMenu('''
            1. Listar prestamos
            2. eliminar prestamos
            3. Herramienta mas solicitada
            4. Usuario mayor prestamos
            5. Salir            
            ''',1,5)
        match op:
            case 1:
                listar_prestamos()
            case 2:
                eliminar_prestamo()
            case 3:
                herramienta_mas_solicitada()
            case 4:
                usuario_mayorsoli()
            case 5:
                print('Salir')
                return
            case _:
                print('Opcion no encontrada')
                  
def persona():
    while True:
        op=validarMenu('''
            Bienvenido

            1. Agregar usuario
            2. Actualizar usuario
            3. Eliminar usuario
            4. Listar
            5. Salir
                     
        ''',1,5)
        match op:
            case 1:
                guardar_persona()
            case 2:
                actualizar_persona()
            case 3:
                eliminar_persona()
            case 4:
                listar_persona()
            case 5:
                print('Gracias por usar nuestro servicios')
                break
            case _:
                print('Error, ingrese una opcion valida')

#menu herramientas-admi
def herramienta():
    while True:
        op=validarMenu('''
            Bienvenido

            1. Agregar herramienta
            2. Actualizar herramienta
            3. Eliminar herramienta
            4. Listar
            5. Salir
                     
        ''',1,5)
        match op:
            case 1:
                guardar_herramienta()
            case 2:
                actualizar_herramienta()
            case 3:
                eliminar_herramienta()
            case 4:
                listar_herramienta1()
            case 5:
                print('Guardado correctamente')
                break
            case _:
                print('Ingrese una opcion valida: ')

#menu USUARIO
def menu_usuario():
            while True:
                        op=validarMenu('''
                            1. Prestamos
                            2. Listar prestamos
                            3. Listar herramientas
                            4. Salir            
                        ''',1,4)
                        match op:
                            case 1:
                                prestamos()
                            case 2:
                                listar_prestamos() 
                            case 3:
                                listar_herramienta1()
                            case 4:
                                print('Salir')
                                break  
                            case _:
                                print('Opcion no encontrada')



    

    
