numero = 0
while numero <= 100:
    if numero % 2 != 0:
        numero += 1
        continue
    print(f'O número {numero} é par!')
    if numero == 10:
        print("OPS... já verifiquei muitos números pares")
        break
    numero += 1
