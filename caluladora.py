import math

# Operações a serem realizadas.

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Não é possivel realizar divisão por zero."

def raiz_quadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Erro: Tente novamente. Raiz negativa não exite."

def potenciacao(a, b):
    return a ** b

# Validar entradas do usuario.

def obter_numero(mensagem):
    """
    Validar a entrada de um número.
    Repete ate que seja digitado um número valido.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n--- CALCULADORA AVANÇADA ---")
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Potenciação")
    print("Digite '0001' para sair.")
    print("-----------------------------")

def calculadora():
    while True:
        menu()
        operacao = input("Digite o número da operação desejada: ")

        if operacao == "0001":
            print("Encerrando a calculadora. Até mais!")
            break

        operacoes = {
            "1": adicao,
            "2": subtracao,
            "3": multiplicacao,
            "4": divisao,
            "5": raiz_quadrada,
            "6": potenciacao
        }

        if operacao in operacoes:
            if operacao == "5":  # Raiz quadrada
                num = obter_numero("Digite o número para calcular a raiz quadrada: ")
                resultado = raiz_quadrada(num)
                print(f"O resultado é: {resultado}")

            elif operacao == "6":  # Potenciação
                base = obter_numero("Digite a base: ")
                expoente = obter_numero("Digite o expoente: ")
                resultado = potenciacao(base, expoente)
                print(f"O resultado é: {resultado}")

            else:  # Operações básicas
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")
                resultado = operacoes[operacao](num1, num2)
                print(f"O resultado é: {resultado}")
        else:
            print("Erro: Operação inválida. Por favor, escolha uma opção válida.")

# Executar a calculadora
calculadora()
