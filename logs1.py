from gestionarJson import generar_id,cargar,guardar
from datetime import date

ARCHIVO_LOGS1="logs.json"

def logs_cantidad():
    logs=cargar(ARCHIVO_LOGS1)

    nuevo_logs={
        "id":generar_id(logs),
        "fecha":date.today().strftime("%Y-%m-%d"),
        "cantidad":"cantidad no encontrado",
        "mensaje":"La cantidad solicitada supera las unidades disponibles!"
    }
    logs.append(nuevo_logs)
    guardar(ARCHIVO_LOGS1,logs)