import math
import time

def obter_numero(mensagem):
    """Solicita um número com validação de entrada."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")

def menu():
    """Menu de opções."""
    print("\n=== CALCULADORA ===")
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Potenciação")
    print("Digite '0001' para sair.")
    print("==============================")

def operacao_basica(op, num1, num2):
    """Operações basicas."""
    operacoes = {
        "1": num1 + num2,
        "2": num1 - num2,
        "3": num1 * num2,
        "4": "Erro: Divisão por zero não é permitida." if num2 == 0 else num1 / num2,
    }
    return operacoes.get(op, "Erro: Operação inválida.")

def raiz_quadrada(num):
    """Calcula a raiz quadrada de um número."""
    if num < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(num)

def potencia(base, expoente):
    """Calcula a potenciação."""
    return base ** expoente

def calculadora():
    """Função principal da calculadora."""
    while True:
        menu()
        operacao = input("Operação desejada: ").strip()

        if operacao == "0001":
            print("Encerrando. Até mais!")
            break

        if operacao in ["1", "2", "3", "4"]:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            resultado = operacao_basica(operacao, num1, num2)
            print(f"O resultado é: {resultado}")

        elif operacao == "5":
            num = obter_numero("Digite o número para calcular a raiz quadrada: ")
            resultado = raiz_quadrada(num)
            print(f"O resultado é: {resultado}")

        elif operacao == "6":
            base = obter_numero("Digite a base: ")
            expoente = obter_numero("Digite o expoente: ")
            resultado = potencia(base, expoente)
            print(f"O resultado é: {resultado}")

        else:
            print("Erro: Operação inválida. Por favor, escolha uma opção válida.")

        # Pausa antes de exibir o menu novamente
        time.sleep(2)

calculadora()

