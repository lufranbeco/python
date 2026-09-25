# Estandar
alto_estandar = 179.0
ancho_estandar = 33.0
profundidad_estandar = 30.0
corte_dobleces_ancho_estandar = 1.6 + 2.2 + 2.2 + 1.6
ancho_corte_puerta_estandar = 32.6

# Entradas
alto_doblado = float(input("Alto del locker: "))
ancho_doblado = float(input("Ancho del locker: "))
profundidad_doblado = float(input("Profundidad del locker: "))
puertas = int(input("Cantidad de puertas: "))
piso = float(input("Cuantos centimetros de piso puede ver: "))

# Diferencias
diferencia_alto = abs(alto_estandar - alto_doblado)
diferencia_ancho = abs(ancho_estandar - ancho_doblado)
diferencia_profundo = abs(profundidad_estandar - profundidad_doblado)

# ---------- CUERPO ----------
# Corte Alto
dobles_arriba = float(input("Doblés de arriba: "))
dobles_abajo = float(input("Doblés de abajo: "))
corte_alto = alto_estandar + diferencia_alto + dobles_arriba + dobles_abajo

print(f"El corte del cuerpo a lo alto es de {corte_alto}")

# Corte Ancho
corte_ancho = (profundidad_doblado - 0.3)*2 + corte_dobleces_ancho_estandar + (ancho_doblado - 0.3)
print(f"El corte del cuerpo a lo ancho es de {corte_ancho}")


# ---------- Puertas ----------
# Corte Alto
corte_alto_puertas = (((alto_doblado - piso) - (puertas*0.5)) / puertas) + 4.8
print(f"{corte_alto_puertas:.1f}")

# Corte Ancho
corte_ancho_puertas = 0
if ancho_estandar < ancho_doblado:
    corte_ancho_puertas = ancho_corte_puerta_estandar + diferencia_ancho
    print(corte_ancho_puertas)
else: 
    corte_ancho_puertas = ancho_corte_puerta_estandar - diferencia_ancho
    print(corte_ancho_puertas)