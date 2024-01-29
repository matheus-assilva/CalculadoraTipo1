# Calculadora
def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return 0
    else:
        print("Operação não reconhecida. Escolha uma operação válida.")
        return 0

# Solicitar dados do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

# Chamar a função e exibir o resultado
resultado = calculadora(num1, num2, operacao)
print(f"Resultado da operação: {resultado}")
