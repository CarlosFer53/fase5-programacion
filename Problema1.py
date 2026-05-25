# Nombre del Estudiante: Carlos Fernando Rodriguez Salazar
# Grupo: 986
# Programa: Ingeniería de Sistemas
# Código Fuente: Autoría propia

def clasificar_sesion(duracion, clics):
    #Clasificar como "Alto" si Duración > 180s y Clics > 8
    if duracion > 180 and clics > 8:
        return "Alto"
    #Clasificar como "Bajo" si Duración < 60s o Clics < 3
    elif duracion < 60 or clics < 3:
        return "Bajo"
    #Clasificar como "Medio" en cualquier otro caso
    else:
        return "Medio"
    
def generar_informe(matriz_sesiones):
    print("\n" + "="*40)
    print("    REPORTE DE SESIONES")
    print("="*40)
    print(f"{'ID Cliente':<15}  |  {'Clasificación'}")
    print("-"*40)
    
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        clasificacion = clasificar_sesion(duracion, clics)
        print(f"{id_cliente:<15}  |  {clasificacion}")
    print("="*40 + "\n")
    
if __name__ == "__main__":
    # Matriz con 5 filas de datos: [ID Cliente, Duración, Clics]
    matriz_sesiones = [
        ["CLI-001", 200, 10],  # Alto
        ["CLI-002", 45, 5],    # Bajo (por duración)
        ["CLI-003", 120, 6],   # Medio
        ["CLI-004", 190, 2],   # Bajo (por clics)
        ["CLI-005", 150, 9]    # Medio
    ]
    
    generar_informe(matriz_sesiones)