a = 0
b = 1
c = 0

compare = int(input("Digite o valor a ser comparado: "))
print(compare)


while True:
    c = a+b
    if c == compare:
        print("O valor está na sequência fibonacci")
        break
    if c > compare:
        print("O valor NÃO está na seqência fibonacci")
        break

    a = b
    b = c
