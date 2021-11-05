a = [
    [1, 3, 7, 7],
    [2, 2, 2, 8],
    [1, 6, 9, 9],
    [1, 6, 8, 9]
]

def perfeita(m1):
    linha = len(m1)
    for elemento in m1:
        if len(elemento) != linha:
            return False
    return True

def matriz(m1):
    if perfeita(m1):
        soma = 0
        linha = len(m1) - 1
        for a in m1:
            soma += a[linha]
            linha -= 1
        print(soma)
    else:
        print("Erro")

matriz(a)
         

