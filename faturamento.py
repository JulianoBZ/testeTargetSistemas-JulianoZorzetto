import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

total = 0
acima_media = []
array_total = []

for i in dados:
    array_total.append(i['valor'])

maior_valor = array_total[0]
menor_valor = array_total[0]
menor_dia = 0
maior_dia = 0
contador = 0
media_cont = 0

for j in array_total:
    contador += 1
    if j > 0:
        if j < menor_valor:
            menor_valor = j
            menor_dia = contador
        if j > maior_valor:
            maior_valor = j
            maior_dia = contador
        total += j
        media_cont += 1

media = total / media_cont
array_dias_bons = []
contador_dias_bons = 0

for p in array_total:
    contador_dias_bons += 1 
    if p > 0:
        if p > media:
            array_dias_bons.append(contador_dias_bons)

print("O menor faturamento foi no dia: ",menor_dia)
print("O maior faturamento foi no dia: ",maior_dia)
print("Os dias com bons faturamentos foram: ",array_dias_bons)

    

