# Gestión de herramientas 🔨🏗️

**Versión 2026 — Python**

Aplicacion de consola desarrollada en Python para gestionar el prestamo de diferentes tipos de herramientas como jardineria o construcción. Diseñada para el uso de una comunidad que requiere tener el control de las herramienta y una organizacion efectiva en sus prestamos.


***

## 🧩 Problemática que resuelve

Comunidad requiere que el programa permita:
- Registro de usuarios y administradores (datos personales, claves, función).
- Generar solicitudes de prestamos.
- Añadir o editar datos (herramienta, usuarios)
- Validar operaciones según disponibilidad y estado.
- Mantener un historial completo de cada dato mal ingresado.
- Evitar inconsistencias en stock ante errores de digitacion o falta de herramientas.

---

## ✨ Funcionalidades principales

- Gestión de herramientas, prestamos y usuarios.
- Registro de prestamos con ajuste automático de stock y estado.
- Validación de errores como digitación o inconsistencia de datos.
- Validaciones  mensajes claros para el usuario.
- Permanencia de datos por medio de archivos JSON.
- Historial de errores en stock o fechas registradas.

## 🗃️Estructura del proyecto

```
gestion_herramientas/
│
├── main.py
├── herramientas.json
├── usuarios.json
├── prestamos.json
├── logs.json
│
├── funciones/
│   ├── herramientas.py
│   ├── usuarios.py
│   ├── prestamos.py
│   └── validaciones.py
```

## 🔥Algunos códigos usados:

### Guardar nuevo usuario 🔐

```
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
    
```
### Logs del stock 🚨
```
def logs_stock():
    logs=cargar(ARCHIVO_LOGS)

    nuevo_logs={
        "id":generar_id(logs),
        "fecha":date.today().strftime("%Y-%m-%d"),
        "stock":"stock no encontrado",
        "mensaje":"La cantidad solicitada supera las unidades disponibles!"
    }
    logs.append(nuevo_logs)
    guardar(ARCHIVO_LOGS,logs)
```
### Eliminacion de prestamos con devolución de stock 🗑️
```
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
```

## 🔨Tecnologías utilizadas

- Python 3

- JSON para almacenamiento de datos

- Programación estructurada

- Manejo de archivos

- Validación de entradas de usuario

## 👷Autor 

Proyecto desarrollado por María José Sánchez
Estudiante de programación.

