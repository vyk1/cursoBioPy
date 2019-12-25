# coding: utf-8

idade = int(input("Informe sua idade: "))
if idade >= 18:
    print "É maior de idade"
elif idade >= 0 and idade < 18:
    print "Não é maior de idade"
else:
    print "Idade inválida"
