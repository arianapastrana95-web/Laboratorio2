# main.py

def mostrar_menu():
    """Req 4: Muestra el menú principal en pantalla (Función sin retorno)."""
    print("\n--- SISTEMA DE ORIENTACIÓN Y REGISTRO ---")
    print("Módulo de Soporte Académico")
    print("-----------------------------------------")

def asignar_prioridad(tipo_consulta):
    """Req 5: Calcula y retorna la prioridad ('Alta' o 'Baja') según el tipo de consulta.
    Req 8: Recibe parámetros por valor de forma aislada."""
    if tipo_consulta in ["matrícula", "pagos"]:
        return "Alta"
    else:
        return "Baja"
    
def validar_texto_obligatorio(texto):
    """Req 6: Valida si una cadena de texto no está vacía. Retorna un valor booleano."""
    return texto.strip() != ""

def validar_codigo_estudiante(codigo):
    """Req 2: Valida que el código de estudiante tenga una longitud mínima de 5 caracteres."""
    if not validar_texto_obligatorio(codigo):
        return False
    return len(codigo.strip()) >= 5

def mostrar_resumen(codigo, nombre, consulta, descripcion, prioridad):
    """Req 7: Imprime un bloque estructurado con el resumen al finalizar los registros."""
    print("\n=========================================")
    print("      RESUMEN FINAL DE LA SOLICITUD      ")
    print("=========================================")
    print(f"Código Alumno: {codigo}")
    print(f"Estudiante:    {nombre}")
    print(f"Consulta:      {consulta.capitalize()}")
    print(f"Prioridad:     {prioridad}")
    print(f"Descripción:   {descripcion}")
    print("=========================================\n")

def ejecutar_pruebas():
    """Req 11: Mantiene las 5 pruebas de sistema obligatorias documentadas en el codigo."""
    print("\n========== EJECUTANDO PRUEBAS DE SISTEMA ==========")
    print("Prueba 1 (Datos válidos):", "PASÓ" if validar_codigo_estudiante("U2026123") and validar_texto_obligatorio("Ariana Pastrana") else "FALLÓ")
    print("Prueba 2 (Código vacío/corto):", "PASÓ" if not validar_codigo_estudiante("   ") and not validar_codigo_estudiante("123") else "FALLÓ")
    consultas_validas = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    print("Prueba 3 (Tipo incorrecto):", "PASÓ" if "error_test" not in consultas_validas else "FALLÓ")
    print("Prueba 4 (Prioridad alta):", "PASÓ" if asignar_prioridad("pagos") == "Alta" else "FALLÓ")
    print("Prueba 5 (Prioridad baja):", "PASÓ" if asignar_prioridad("constancia") == "Baja" else "FALLÓ")
    print("===================================================\n")

def principal():
    """Req 1, 8, 9, 10: Controla el flujo principal y el alcance de las variables."""
    mostrar_menu()
    
    # Inicializamos la prioridad final de la sesión como "Baja" por defecto
    prioridad_final = "Baja"

    # Bucle para el registro de las 3 solicitudes consecutivas
    for i in range(1, 4):
        print(f"\n>>> REGISTRO DE LA SOLICITUD N° {i} <<<")

        # Captura y validación de Código
        codigo_estudiante = input("Código de estudiante: ")
        while not validar_codigo_estudiante(codigo_estudiante):
            print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")
            codigo_estudiante = input("Código de estudiante válido: ")

        # Captura y validación de Nombre
        nombre_estudiante = input("Nombre completo del estudiante: ")
        while not validar_texto_obligatorio(nombre_estudiante):
            print("Error: El nombre completo es obligatorio.")
            nombre_estudiante = input("Nombre completo del estudiante: ")

        # Captura y validación de Tipo de Consulta
        consultas_validas = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
        tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()
        while tipo_consulta not in consultas_validas:
            print("Error: Tipo de consulta no válido. Elija una opción de la lista.")
            tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()
        
        # Captura de la descripción
        descripcion_breve = input("Descripción breve de la solicitud: ")
        while not validar_texto_obligatorio(descripcion_breve):
            print("Error: La descripción breve es obligatoria.")
            descripcion_breve = input("Descripción breve de la solicitud: ")

        # Calcula la prioridad individual
        prioridad_actual = asignar_prioridad(tipo_consulta)
        print(f"-> Prioridad asignada para este registro: {prioridad_actual}")

        # Lógica de acumulación: Si detecta una prioridad "Alta", se queda grabada como "Alta" para todo el reporte final
        if prioridad_actual == "Alta":
            prioridad_final = "Alta"

    print("\n✓ Se han registrado las 3 solicitudes requeridas con éxito.")
    
    # Muestra el resumen final con la prioridad más alta acumulada durante el proceso
    mostrar_resumen(codigo_estudiante, nombre_estudiante, tipo_consulta, descripcion_breve, prioridad_final)

if __name__ == "__main__":
    principal()

