# Estandar
alto_estandar = 179.0
ancho_estandar = 33.0
profundidad_estandar = 30.0
corte_dobleces_ancho_estandar = 1.6 + 2.2 + 2.2 + 1.6

# Entradas
alto_doblado = float(input("Alto del locker: "))
ancho_doblado = float(input("Ancho del locker: "))
profundidad_doblado = float(input("Profundidad del locker: "))

# Diferencias
diferencia_alto = abs(alto_estandar - alto_doblado)
diferencia_ancho = abs(ancho_estandar - ancho_doblado)
diferencia_profundo = abs(profundidad_estandar - profundidad_doblado)

# Corte Alto
dobles_arriba = float(input("Doblés de arriba: "))
dobles_abajo = float(input("Doblés de abajo: "))
corte_alto = alto_estandar + diferencia_alto + dobles_arriba + dobles_abajo

print(f"El corte del cuerpo a lo alto es de {corte_alto}")

# Corte ancho
corte_ancho = (profundidad_doblado - 0.3)*2 + corte_dobleces_ancho_estandar + (ancho_doblado - 0.3)
print(f"El corte del cuerpo a lo ancho es de {corte_ancho}")