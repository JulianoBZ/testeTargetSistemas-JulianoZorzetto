SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros
array_porcentagem = []

dict_porcentagem = {
    "SP": (SP/total),
    "RJ": (RJ/total),
    "MG": (MG/total),
    "ES": (ES/total),
    "Outros": (Outros/total)
}


print("Os valores da porcentagem por estado são: ")
print(dict_porcentagem)
