from gestionarJson import generar_id,cargar,guardar
from datetime import date


ARCHIVO_LOGS="logs.json"

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

def logs_fechas():
    logs=cargar(ARCHIVO_LOGS)

    nuevo_logs={
        "id":generar_id(logs),
        "fecha":date.today().strftime("%Y-%m-%d"),
        "FECHA":"Fecha no encontrada",
        "mensaje":"La fecha solicitada no esta disponible!"
    }
    logs.append(nuevo_logs)
    guardar(ARCHIVO_LOGS,logs)

def logs_nombres():
    logs=cargar(ARCHIVO_LOGS)

    nuevo_logs={
        "id":generar_id(logs),
        "fecha":date.today().strftime("%Y-%m-%d"),
        "mensaje":"El nombre ya se encuentra registrado!"
    }
    logs.append(nuevo_logs)
    guardar(ARCHIVO_LOGS,logs)


def listar_logs():
    logs=cargar(ARCHIVO_LOGS)

    if logs==[]:
        print("No hay logs")
    else:
        print("\nLogs:")
        for elemento in logs:
            print(f"ID {elemento['id']}")
            print(f"Fecha {elemento['fecha']}")
            print(f"mensaje {elemento['mensaje']}")
            print("---------------------------------------")
