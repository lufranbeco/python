# Dobleces Estandar
alto_estandar = 179.0
ancho_estandar = 33.0
profundidad_estandar = 30.0

# Cortes Estandar
corte_dobleces_ancho_estandar = 1.6 + 2.2 + 2.2 + 1.6
ancho_corte_puerta_estandar = 32.6
alto_entrepaño_estandar = 32.4
ancho_entrepaño_estandar = 37.1

print("\n\n---------- LOCKER ----------")
# Entradas
alto_doblado = float(input("Alto: "))
ancho_doblado = float(input("Ancho: "))
profundidad_doblado = float(input("Profundidad: "))
puertas = int(input("Cantidad de puertas: "))
piso = float(input("Cuantos centimetros de piso puede ver: "))

# Diferencias
diferencia_alto = abs(alto_estandar - alto_doblado)
diferencia_ancho = abs(ancho_estandar - ancho_doblado)
diferencia_profundo = abs(profundidad_estandar - profundidad_doblado)

print("\n\n\n---------- CUERPO ----------")
# ---------- CUERPO ----------
# Corte Alto
dobles_arriba = float(input("Doblés de arriba: "))
dobles_abajo = float(input("Doblés de abajo: "))
corte_alto = alto_estandar + diferencia_alto + dobles_arriba + dobles_abajo

print(f"El corte del cuerpo a lo alto es de {corte_alto}")

# Corte Ancho
corte_ancho = (profundidad_doblado - 0.3)*2 + corte_dobleces_ancho_estandar + (ancho_doblado - 0.3)
print(f"El corte del cuerpo a lo ancho es de {corte_ancho}")


print("\n\n---------- PUERTAS ----------")
# ---------- Puertas ----------
# Corte Alto
corte_alto_puertas = (((alto_doblado - piso) - (puertas*0.5)) / puertas) + 4.8
print(f"Alto: {corte_alto_puertas:.1f}")

# Corte Ancho
corte_ancho_puertas = 0
if ancho_estandar < ancho_doblado:
    corte_ancho_puertas = ancho_corte_puerta_estandar + diferencia_ancho
    print(f"Ancho: {corte_ancho_puertas}")
else: 
    corte_ancho_puertas = ancho_corte_puerta_estandar - diferencia_ancho
    print(f"Ancho: {corte_ancho_puertas}")


print("\n\n---------- ENTREPAÑOS ----------")
# ---------- Entrepaños ----------
# Corte Alto
corte_alto_entrepaños = 0
if profundidad_estandar < profundidad_doblado:
    corte_alto_entrepaños = alto_entrepaño_estandar + diferencia_profundo
    print(f"Alto: {corte_alto_entrepaños}")
else: 
    corte_alto_entrepaños = alto_entrepaño_estandar - diferencia_profundo
    print(f"Alto: {corte_alto_entrepaños}")

# Corte Ancho
corte_ancho_entrepaños = 0
if ancho_estandar < ancho_doblado:
    corte_ancho_entrepaños = ancho_entrepaño_estandar + diferencia_ancho
    print(f"Ancho: {corte_ancho_entrepaños}")
else: 
    corte_ancho_entrepaños = ancho_entrepaño_estandar - diferencia_ancho
    print(f"Ancho: {corte_ancho_entrepaños}")