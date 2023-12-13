def relacionar_nombres_y_edades(nombres, edades):
    relacion = {}
    for i in range(len(nombres)):
        relacion[nombres[i]] = edades[i]
    return relacion

nombres = ["Oriol", "Aleix", "Pol", "Ramon", "Dani", "Angela", "Gerard"]
edades = [18, 19, 19, 21, 18, 19, 20]
print(relacionar_nombres_y_edades(nombres, edades), "\b\b")
print ("Y recuerda cuidarte de la admiración mal gestionada")
