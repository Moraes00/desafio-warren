limite = 10**6
somas = []
final = []

for numero in range(1,limite+1):
    inverso = int(str(numero)[::-1])
    resultado = int(numero+inverso)
    qtdcasas = int(len(str(resultado)))

    if numero % 10 and resultado % 2:
        if qtdcasas == 2:
            if (int(resultado / 10) % 2):
                final.append(numero)
                somas.append(resultado)

        elif qtdcasas == 3:
            if (int(resultado / 10) % 2) and (int(resultado / 100) % 2):
                final.append(numero)
                somas.append(resultado)

        elif qtdcasas == 4:
            if (int(resultado / 10) % 2) and (int(resultado / 100) % 2) and (int(resultado / 1000) % 2):
                final.append(numero)
                somas.append(resultado)

        elif qtdcasas == 5:
            if (int(resultado / 10) % 2) and (int(resultado / 100) % 2) and (int(resultado / 1000) % 2) \
            and (int(resultado / 10000) % 2):
                final.append(numero)
                somas.append(resultado)

        elif qtdcasas == 6:
            if (int(resultado / 10) % 2) and (int(resultado / 100) % 2) and (int(resultado / 1000) % 2) \
            and (int(resultado / 10000) % 2) and (int(resultado / 100000) % 2):
                final.append(numero)
                somas.append(resultado)

        elif qtdcasas == 7:
            if (int(resultado / 10) % 2) and (int(resultado / 100) % 2) and (int(resultado / 1000) % 2) \
            and (int(resultado / 10000) % 2) and (int(resultado / 100000) % 2) and (int(resultado / 1000000) % 2):
                final.append(numero)
                somas.append(resultado)

print(len(final))
print(final)