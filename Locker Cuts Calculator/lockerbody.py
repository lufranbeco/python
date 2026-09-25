# Estandar
alto_estandar = 179.0

# Entradas
alto_doblado = float(input("Alto del locker: "))

# Diferencias
diferencia_alto = abs(alto_estandar - alto_doblado)

# Corte Alto
dobles_arriba = float(input("Doblés de arriba: "))
dobles_abajo = float(input("Doblés de abajo: "))
corte_alto = alto_estandar + diferencia_alto + dobles_arriba + dobles_abajo

print(f"El corte del cuerpo a lo alto es de {corte_alto}cm")