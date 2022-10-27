#Função que retorna Verdadeiro para números primos e Falso caso contrário

for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if(num % i)== 0:
                print("NÚMERO %d :FALSO" %num)
                break
        else:
            print("NÚMERO %d :VERDADEIRO" %num)