def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

if __name__ == "__main__":
    print("Teste da divisão (10 / 2):", divisao(10, 2))