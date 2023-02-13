def es_bisiesto(anio):
    if anio % 4==0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

int_anio = int(input("Ingrese anio: "))

print("bisiesto =",es_bisiesto(int_anio))