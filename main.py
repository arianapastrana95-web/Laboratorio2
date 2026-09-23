def mostrar_menu():
    
    print("\n--- SISTEMA DE ORIENTACIÓN Y REGISTRO ---")
    print("Módulo de Soporte Académico")
    print("-----------------------------------------")

def asignar_prioridad(tipo_consulta):
    if tipo_consulta in ["pagos", "plataforma"]:
        return "Alta"
    else:
        return "Media"
def validar_texto_obligatorio(texto):
   
    return texto.strip() != ""

def mostrar_resumen(codigo, nombre, consulta, descripcion, prioridad):
    
    print("\n=========================================")
    print("        RESUMEN DE LA SOLICITUD          ")
    print("=========================================")
    print(f"Código Alumno: {codigo}")
    print(f"Estudiante:    {nombre}")
    print(f"Consulta:      {consulta.capitalize()}")
    print(f"Prioridad:     {prioridad}")
    print(f"Descripción:   {descripcion}")
    print("=========================================\n")

def principal():

    mostrar_menu()
    
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

    prioridad = asignar_prioridad(tipo_consulta)
    mostrar_resumen(codigo_estudiante, nombre_estudiante, tipo_consulta, descripcion_breve, prioridad)

if __name__ == "__main__":
    principal()