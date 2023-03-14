string = str(input("Digite uma string para ser invertida: "))
str = ""
for i in string:
    str = i + str
print("String inversa:",str)