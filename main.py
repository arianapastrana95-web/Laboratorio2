def mostrar_menu():
    
    print("\n--- SISTEMA DE ORIENTACIÓN Y REGISTRO ---")
    print("Módulo de Soporte Académico")
    print("-----------------------------------------")

def asignar_prioridad(tipo_consulta):
    if tipo_consulta in ["pagos", "plataforma"]:
        return "Alta"
    else:
        return "Media"

def principal():

    mostrar_menu()
    
    codigo_estudiante = input("Código de estudiante: ")

    while codigo_estudiante.strip() == "" or len(codigo_estudiante.strip()) < 5:
        print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")
        codigo_estudiante = input("Código de estudiante válido: ")

    nombre_estudiante = input("Nombre completo del estudiante: ")

    consultas_validas = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()
    
    while tipo_consulta not in consultas_validas:
        print("Error: Tipo de consulta no válido. Elija una opción de la lista.")
        tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ").strip().lower()
        
    descripcion_breve = input("Descripción breve de la solicitud: ")
    prioridad = asignar_prioridad(tipo_consulta)

if __name__ == "__main__":
    principal()