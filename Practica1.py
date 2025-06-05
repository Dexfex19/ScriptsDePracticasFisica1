import math # esta es la unica libreria importada pero es parte de la libreria standard de Python, no requirio de una instalacion aparte. 

#Se crean 2 funciones diferentes para manejar la entrada de datos, ya sea por magnitud y direccion o si es por los mismos componentes


#esta seria la funcion para cuando la entrada es la magnitud y la direccion del vector
def entrada_por_magnitud_direccion():
    magnitud = float(input("Ingrese la magnitud del vector: "))
    direccion = float(input("Ingrese la dirección del vector en grados: "))
    rad = math.radians(direccion) #conversion a radiantes para poder hacer las operaciones trigonometricas 
    x = magnitud * math.cos(rad)
    y = magnitud * math.sin(rad)
    return x, y
#esta es la funcion papra cuando la entrada son los componentes en X y en Y
def entrada_por_componentes():
    x = float(input("Ingrese la componente x del vector: "))
    y = float(input("Ingrese la componente y del vector: "))
    return x, y

#esta funcion adicional se crea para calcular la magnitud y direccion del vector resultante.
def calcular_magnitud_direccion(x, y):
    magnitud = math.sqrt(x**2 + y**2)
    direccion_rad = math.atan2(y, x)  # para el ángulo en radianes se usa atan2 para tener en cuenta el signo y cuadrante
    direccion_deg = math.degrees(direccion_rad)  # aqui se hace la conversión  de radianes a grados
    return magnitud, direccion_deg

def main():
    print("=== Suma de N Vectores ===")
    
    n = int(input("¿Cuántos vectores desea sumar? "))
    while n < 2:
        print("Debe ingresar al menos 2 vectores.")
        n = int(input("¿Cuántos vectores desea sumar? "))

    metodo = input("¿Cómo desea ingresar los vectores? (1: Magnitud y dirección, 2: Componentes): ").strip()
    while metodo not in ["1", "2"]:
        metodo = input("Entrada inválida. Escriba 1 o 2: ")

    suma_x = 0.0
    suma_y = 0.0

    for i in range(n):
        print(f"\nVector {i + 1}:")
        if metodo == "1":
            x, y = entrada_por_magnitud_direccion()
        else:
            x, y = entrada_por_componentes()
        
        suma_x += x
        suma_y += y
        
    magnitud_resultante, direccion_resultante = calcular_magnitud_direccion(suma_x, suma_y)

    print("\n=== Resultado ===")
    print(f"Vector resultante (componentes): ({suma_x:.2f}, {suma_y:.2f})")
    print(f"Magnitud del vector resultante: {magnitud_resultante:.2f}")
    print(f"Dirección del vector resultante: {direccion_resultante:.2f}°")


if __name__ == "__main__":
    main()
