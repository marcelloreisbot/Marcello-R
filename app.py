# Programa de calculo de valor de compra com descontos progressivos
# Autor: Marcello Reis de Campos Melo

# Entrada
valor_compra= float(input("Valor total da compra: R$"))

# Processamento
if valor_compra <200:
    desconto =0.05
elif valor_compra <300:
    desconto =0.10
else:
    desconto =0.15

valor_desconto = valor_compra * desconto
valor_final = valor_compra-valor_desconto

#Saida
print(f"desconto: {desconto * 100:0f}%")
print(f"valor do desconto: R$ {valor_desconto:.2f}")
print(f"valor final da compra: R$ {valor_final:.2f}")
