import tkinter as tk

def DummyD():
    formato_elegido = generar_formato.get()
    alumnos = mostrar_alumnos.get("1.0", tk.END)
    if formato_elegido == "0" or not alumnos:
        return
    switch_formato(formato_elegido, alumnos)

def switch_formato(formato_elegido, alumnos):
    if formato_elegido == "csv":
        generar_csv(alumnos)
    elif formato_elegido == "json":
        generar_json(alumnos)
    elif formato_elegido == "sql":
        generar_sql(alumnos)
    elif formato_elegido == "xml":
        generar_xml(alumnos)
    else:
        print("Formato invalido")

def generar_csv(alumnos):
    salida = ""
    alumnos2 = alumnos.split("\n")

    for alumno in alumnos2:
        if alumno:
            salida += alumno + "\n"

    with open('alumnos.csv', 'w') as file:
        file.write(salida)

def generar_json(alumnos):
    salida = []
    alumnos2 = alumnos.split("\n")

    for alumno in alumnos2:
        if alumno:
            alumno_data = alumno.split(", ")
            salida.append({
                "expediente": alumno_data[0],
                "apellido1": alumno_data[1],
                "apellido2": alumno_data[2],
                "nombre": alumno_data[3],
                "correo": alumno_data[4],
                "fechaNacimiento": alumno_data[5]
            })

    import json
    with open('alumnos.json', 'w') as file:
        json.dump(salida, file, indent=2)

def generar_sql(alumnos):
    salida = "CREATE DATABASE IF NOT EXISTS evento;\n USE evento;\nCREATE TABLE IF NOT EXISTS asistentes(expediente INT NOT NULL, apellido1 VARCHAR(255), apellido2 VARCHAR(255), nombre VARCHAR(255), correo VARCHAR(255) NOT NULL, fechaNacimiento DATE);\n INSERT INTO asistentes (expediente, apellido1, apellido2, nombre, correo, fechaNacimiento) VALUES\n"
    alumnos2 = alumnos.split("\n")

    for alumno in alumnos2:
        if alumno:
            alumno_data = alumno.split(", ")
            salida += "('" + "', '".join(alumno_data) + "'),\n"

    salida = salida[:-2] + ";"
    with open('alumnos.sql', 'w') as file:
        file.write(salida)

def generar_xml(alumnos):
    salida = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<asistentes>\n"
    alumnos2 = alumnos.split("\n")

    for alumno in alumnos2:
        if alumno:
            alumno_data = alumno.split(", ")
            salida += "  <asistente>\n"
            salida += "    <expediente>" + alumno_data[0] + "</expediente>\n"
            salida += "    <apellido1>" + alumno_data[1] + "</apellido1>\n"
            salida += "    <apellido2>" + alumno_data[2] + "</apellido2>\n"
            salida += "    <nombre>" + alumno_data[3] + "</nombre>\n"
            salida += "    <correo>" + alumno_data[4] + "</correo>\n"
            salida += "    <fechaNacimiento>" + alumno_data[5] + "</fechaNacimiento>\n"
            salida += "  </asistente>\n"

    salida += "</asistentes>"
    with open('alumnos.xml', 'w') as file:
        file.write(salida)

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Formatos")

# Crear los widgets
generar_formato = tk.StringVar(root)
generar_formato.set("0")
tk.Label(root, text="Seleccione el formato:").pack()
formato_menu = tk.OptionMenu(root, generar_formato, "0", "csv", "json", "sql", "xml")
formato_menu.pack()

tk.Label(root, text="Ingrese los alumnos (uno por línea):").pack()
mostrar_alumnos = tk.Text(root, height=10, width=50)
mostrar_alumnos.pack()

generar_boton = tk.Button(root, text="Generar", command=eleccion)
generar_boton.pack()

root.mainloop()
