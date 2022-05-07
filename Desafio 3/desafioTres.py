def SeqCertas(vetor, soma):
    #lista p/ guardar resultados certos
    resultado = []

    #lista usada para a verificação
    temporario = []

    # limpando e organizando o vetor
    vetor = sorted(list(set(vetor)))

    TesteNum(resultado, vetor, temporario, soma, 0)
    return resultado

def TesteNum(resultado, vetor, temporario, soma, index):
    if (soma == 0):
        # Adiciona a resultado a sequencia certa
        resultado.append(list(temporario))
        return

    # Iterate from index to len(arr) - 1
    for i in range(index, len(vetor)):

        # Verificando se a soma não ultrapassa o limite
        if (soma - vetor[i]) >= 0:

            temporario.append(vetor[i])
            TesteNum(resultado, vetor, temporario, soma - vetor[i], i)

            temporario.remove(vetor[i])


# Entradas
vetor = [2,3,4]
soma = 10
resultado = SeqCertas(vetor, soma)
resultado.sort(reverse=True)

# Imprimir a(s) menor(es) sequencia(s)
for i in resultado:
    if len(i) <= len(resultado[0]):
        print(i)
