# Leitura da idade expressa em anos, meses e dias


from datetime import date

hoje = date.today()

dNasc = int(input("Digite o dia de Nascimento: "))
mNasc = int(input("Digite o mês de Nascimento: "))
aNasc = int(input("Digite o ano de Nascimento: "))

dataNasc = date(aNasc,mNasc,dNasc)

tIdade = hoje - dataNasc
aIdade = tIdade.days/365
mIdade = ((aIdade - int(aIdade))*365) / 30
dIdade = (mIdade - int(mIdade)) * 30


print("Você tem %d anos, %d meses e %d dias" %(aIdade,mIdade,dIdade))

