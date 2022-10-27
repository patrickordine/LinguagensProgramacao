#Lê 3 números, verifica se é um triangulo e calcula a área

import math

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o primeiro número: "))
c = int(input("Digite o primeiro número: "))
p = (float(a) + float(b) + float(c)) / 2.0
area = math.sqrt(p*(p-float(a))*(p-float(b))*(p-float(c)))

if (a + b > c) and (a + c> b) and (b + c > a):
    print("\nTriangulo encontrado!")

    if(a==b) and (a==c):
        print("Equilatero... Área = %0.2f" %area)
    elif (a == b) or (a == c) or (b == c):
        print("Isosceles... Área = %0.2f" %area)
    else:
        print("Escaleno... Área = %0.2f" %area)
else:
    print("Os valores não forma um triangulo...")