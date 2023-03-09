#ouput

x = int(input("se ingresa el valor de x: "))
y = int(input("se ingresa el valor de y: "))

# processing

if x > 0 and y > 0:
    print("el punto se encuentra en el primer cuadrante del plano cartesiano ")

if x < 0 and y > 0:
    print("el punto se encuentra en el segundo cuadrante del plano cartesiano ")

if x < 0 and y < 0:
    print("el punto se encuentra en el tercero cuadrante del plano cartesiano ")

if x > 0 and y < 0:
    print("el punto se encuentra en el cuarto cuadrante del plano cartesiano ")

if x==0 and y==0:
    print("el punto esta en el origen del plano cartesiano ")

if x == 0 or y == 0:
    if x != 0:
        print("se encuentra en el eje x ")
    if y != 0:
        print("se encuentra en el eje y ")