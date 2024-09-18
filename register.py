import pandas as pd

lucro1 = list()
lucro2 = list()
lucro3 = list()
lucro4 = list()

corretor = list() 
casa = list()
valor = list()

#REGISTRO
while True:
    addcorr = corretor.append(input('Nome do corretor responsável: ').capitalize())
    addcasa =casa.append(input('Tipo de casa vendida: [Baixa/Média/Alta] ').capitalize())
    addvalor =valor.append(int(input('Valor da casa: ')))
    resp = input('Deseja registrar mais um imóvel?: ').upper()
    if resp == 'N':
        break


corretor1 = corretor[0]
corretor2 = corretor[1]
corretor3 = corretor[2]
corretor4 = corretor[3]


# COLOCAR OS VALORES NAS LISTAS CORRESPONDENTES
for m in range(len(corretor)):
    if corretor[m] == corretor1:
        lucro1.append(valor[m])
    elif corretor[m] == corretor2:
        lucro2.append(valor[m])
    elif corretor[m] == corretor3:
        lucro3.append(valor[m])
    elif corretor[m] == corretor4:
        lucro4.append(valor[m])

# SOMAS E PORCENTAGENS
soma1 = sum(lucro1)
soma2 = sum(lucro2)
soma3 = sum(lucro3)
soma4 = sum(lucro4)
bonus1 = soma1*0.2
bonus2 = soma2*0.2
bonus3 = soma3*0.2
bonus4 = soma4*0.2

# TABELA
lista = list(zip(corretor,casa,valor))
data = {
    'Corretor': corretor, 
    'Casa': casa,
    'Valor': valor,
}

df = pd.DataFrame(data)

# PRINTS
print('=-'*30)
print(df)
print('=-'*30)
print(f'Segue a tabela com o bônus semanal de cada corretor incluso: \n{corretor1} ------------------------ {bonus1}\n{corretor2} ------------------------ {bonus2}\n{corretor3} ------------------------ {bonus3}\n{corretor4} ------------------------ {bonus4}')
print('=-'*30)
