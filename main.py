def principal():
    
    codigo_estudiante = input("Código de estudiante: ")
    while codigo_estudiante.strip() == "" or len(codigo_estudiante.strip()) < 5:
        print("Error: El código no puede estar vacío y debe tener al menos 5 caracteres.")
        codigo_estudiante = input("Código de estudiante válido: ")
    nombre_estudiante = input("Nombre completo del estudiante: ")
    tipo_consulta = input("Tipo de consulta (matrícula, pagos, constancia, plataforma, otro): ")
    descripcion_breve = input("Descripción breve de la solicitud: ")

if __name__ == "__main__":
    principal()