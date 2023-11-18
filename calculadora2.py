class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        #self.tipo = tipo

    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2
    
    def divisao(self):
        return self.num1 / self.num2
    
    def escolhaTipo(self):
        opcao = int(input("Digite qual operação deseja realizar:\n1)Soma\n2)Subtração\n3)Multiplicação\n4)Divisão\n:"))

        if opcao == 1:
            return self.soma()
        elif opcao == 2:
            return self.subtracao()
        elif opcao == 3:
            return self.multiplicacao()
        elif opcao == 4:
            return self.divisao()
        else:
            int(input("Você digitou uma opção inválida!\n Por favor digite qual operação deseja realizar:\n1)Soma\n2)Subtração\n3)Multiplicação\n4)Divisão\n:"))

print("Esse programa simulará uma calculadora online!")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

Calculadora = Calculadora(num1, num2)

resultado = Calculadora.escolhaTipo()

if resultado is not None:
    print(f"Resultado = {resultado}")