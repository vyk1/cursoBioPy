# # -*- coding: utf-8 -*-

valor1 = float(input("Insira a primeira nota: "))
valor2 = float(input("Insira a segunda nota: "))
soma = valor1 + valor2
media = soma/2

if media < 6:
    print "sua média foi de : ", media, "\nsituação: reprovado"
else:
    print "sua média foi de : ", media, "\nsituação: aprovado"
