num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador: ")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = num1 + num2

elif operador == "-":
    resultado = num1 - num2

elif operador == "/":
    resultado = num1 / num2

elif operador == "*":
    resultado = num1 * num2

elif operador == "%":
    resultado = num1 % num2

elif operador == "**":
    resultado = num1 ** num2
else:
    resultado = "Uma falha ocorreu. Verifique seus inputs"

print (resultado)
