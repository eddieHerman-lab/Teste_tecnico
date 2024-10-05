# 1 Exercicio
#Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?
indice=13
soma=0
k=0
while k < indice:
    k+=1
    soma+=k
print(soma)
# 2 Exercicio

#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def Fibonacci(n):
    numero_temp= n+3
    sequencia = [0, 1]
    while len(sequencia) < numero_temp:
        next_number = sequencia[-1] + sequencia[-2]
        sequencia.append(next_number)
    if n in sequencia:
        return f' {n} Pertence a sequencia fibonacci'
    else:
        return f' {n} Nao pertence a sequencia fibonacci'

try:
    numero= int(input('Numero:'))
except ValueError as error:
    print('Valor indetermiando, somente nuemros!!')
    numero= int(input('Numero:'))

print(Fibonacci(numero))

# 3 Exercicio
# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
# O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
# Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


# Usando a lib Fake pra randomizar esimular dados no JSON

import json
from faker import Faker
import random

# Cirar uma instancia Faker
fake=Faker()

# lista pra armazenar os dados de faturamento
dados_faturamento=[]

# Definir  o numero de dias (considerando 31)
numero_dias=31

#Gerar dados leatortios pra cada dia
for dia in range(1,numero_dias +1):
    valor_faturamento = round(random.uniform(0,5000),2)
    dados_faturamento.append({
        'dia': dia,
        'valor': valor_faturamento
    })
# Salvar os dados em formato JSon

with open('faturamento_random.json' ,'w') as json_file:
    json.dump(dados_faturamento, json_file,indent=4)

print('Dados de faturamentos gerados e salvos em faturamento.random.json')
with open('faturamento_random.json','r')as file:
    dados= json.load(file)

# Filtra o valor de faturamento mos dias uteis (maior que zero):
faturamento_dias_uteis= [dia['valor'] for dia in dados if dia['valor'] > 0]

#1 Menor valor de faturaqmento ocorrido
menor_faturamento= min(faturamento_dias_uteis)

#2 Maior valor de faturamento ocorrido
maior_faturamento= max(faturamento_dias_uteis)

#3 Media mensal
media_faturamento= sum(faturamento_dias_uteis)/len(faturamento_dias_uteis)

#4 Numero de dias no mes que o valor do faturamento foi superior a media
dias_acima_da_media=[]
for valor in faturamento_dias_uteis:
    if valor > media_faturamento:
        dias_acima_da_media.append(valor)
# Reultados
print(f'Menor valor de faturamento : {menor_faturamento}')
print(f' Maior valor de faturamento : {maior_faturamento}')
print(f'Numero de dias com faturamento superior a media : {len(dias_acima_da_media)}')


# 4 Exercicio:
# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43
# RJ – R$36.678,66
#MG – R$29.229,88
# ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
import pandas as pd
import numpy as np

data= {
    'Estados': ['SP', 'RJ', 'MG', 'ES','Outros'],
    'Faturamento':[67.83643, 36.67866,29.22988,27.16548,19.84953],
}
# EScreva um programa onde calcule o percentual que cada etado teve dentro do valor total mensal da distribuidora
Dataframe_data= pd.DataFrame(data)
Percentual_estado= (Dataframe_data['Faturamento']/ sum(Dataframe_data['Faturamento']) *100)
Dataframe_data['Percentual']= Percentual_estado
Dataframe_data['Percentual']= Dataframe_data['Percentual'].round(2)
print(Dataframe_data)


# Exercicio 5
# Ivertendo uma string
def String_invertida(string: str) -> str:
    return f'String Invertida : {string[-1::-1]}'

string_input= input('String Original:')

print(String_invertida(string_input))
