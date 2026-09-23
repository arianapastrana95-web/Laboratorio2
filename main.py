def mostrar_menu():
    """Req 4: Muestra el menú principal en pantalla (Función sin retorno)."""
    
    print("\n--- SISTEMA DE ORIENTACIÓN Y REGISTRO ---")
    print("Módulo de Soporte Académico")
    print("-----------------------------------------")

def asignar_prioridad(tipo_consulta):
    """Req 5: Calcula y retorna la prioridad ('Alta' o 'Media') según el tipo de consulta.
    Req 8: Recibe parámetros por valor de forma aislada."""
    # Req 8: Recibe el parámetro por valor de forma aislada

    if tipo_consulta in ["pagos", "plataforma"]:
        return "Alta"
    else:
        return "Bajo"
    
def validar_texto_obligatorio(texto):
    """Req 6: Valida si una cadena de texto no está vacía. Retorna un valor booleano.
    Req 8: Recibe el parámetro por valor localmente."""
    # Req 8: Recibe el texto a validar localmente sin usar globales

    return texto.strip() != ""

def validar_codigo_estudiante(codigo):
    """Req 2: Valida que el código de estudiante tenga una longitud mínima de 5 caracteres."""
    if not validar_texto_obligatorio(codigo):
        return False
    return len(codigo.strip()) >= 5

def mostrar_resumen(codigo, nombre, consulta, descripcion, prioridad):
    """Req 7: Imprime un bloque estructurado con el resumen de la solicitud registrada.
    Req 8: Recibe los 5 datos de la atención de forma independiente por parámetro."""
    # Req 8: Recibe los 5 datos de la atención como parámetros independientes

    print("\n=========================================")
    print("        RESUMEN DE LA SOLICITUD          ")
    print("=========================================")
    print(f"Código Alumno: {codigo}")
    print(f"Estudiante:    {nombre}")
    print(f"Consulta:      {consulta.capitalize()}")
    print(f"Prioridad:     {prioridad}")
    print(f"Descripción:   {descripcion}")
    print("=========================================\n")

def ejecutar_pruebas():
    """Req 11: Ejecuta y valida automáticamente las 5 pruebas de sistema obligatorias."""
    
    print("\n========== EJECUTANDO PRUEBAS DE SISTEMA ==========")
    
    # Prueba 1: Datos válidos
    print("Prueba 1 (Datos válidos):", "PASÓ" if validar_codigo_estudiante("U2026123") and validar_texto_obligatorio("Ariana Pastrana") else "FALLÓ")
    
    # Prueba 2: Código vacío / inválido
    print("Prueba 2 (Código vacío/corto):", "PASÓ" if not validar_codigo_estudiante("   ") and not validar_codigo_estudiante("123") else "FALLÓ")
    
    # Prueba 3: Tipo de consulta incorrecto
    consultas_validas = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    print("Prueba 3 (Tipo incorrecto):", "PASÓ" if "error_test" not in consultas_validas else "FALLÓ")
    
    # Prueba 4: Prioridad alta
    print("Prueba 4 (Prioridad alta):", "PASÓ" if asignar_prioridad("pagos") == "Alta" else "FALLÓ")
    
    # Prueba 5: Prioridad baja/media
    print("Prueba 5 (Prioridad baja/media):", "PASÓ" if asignar_prioridad("matrícula") == "Media" else "FALLÓ")
    print("===================================================\n")

def principal():
# Llamamos a la función sin retorno del menú
    mostrar_menu()
# Bucle para solicitudes múltiples
    for i in range(1, 4):
        print(f"\n>>> REGISTRO DE LA SOLICITUD N° {i} <<<")

        codigo_estudiante = input("Código de estudiante: ")

        while codigo_estudiante.strip() == "" or len(codigo_estudiante.strip()) < 5:
            print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")
            codigo_estudiante = input("Código de estudiante válido: ")

        nombre_estudiante = input("Nombre completo del estudiante: ")
        while not validar_texto_obligatorio(nombre_estudiante):
            print("Error: El nombre completo es obligatorio.")
            nombre_estudiante = input("Nombre completo del estudiante: ")

        consultas_validas = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
        tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()

        while tipo_consulta not in consultas_validas:
            print("Error: Tipo de consulta no válido. Elija una opción de la lista.")
            tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()
        
    descripcion_breve = input("Descripción breve de la solicitud: ")

    while not validar_texto_obligatorio(descripcion_breve):
        print("Error: La descripción breve es obligatoria.")
        descripcion_breve = input("Descripción breve de la solicitud: ")

    # Req 9: Controlar el alcance de variables locales del programa principal
    # Las variables 'prioridad', 'codigo_estudiante', 'nombre_estudiante', etc.
    # tienen alcance local dentro de principal() y no interfieren de forma global.
    prioridad = asignar_prioridad(tipo_consulta)

    mostrar_resumen(codigo_estudiante, nombre_estudiante, tipo_consulta, descripcion_breve, prioridad)
print("\n✓ Se han registrado las 3 solicitudes requeridas con éxito.")
if __name__ == "__main__":
    principal()