# Conversão de real para dolar
print('Conversão de Real para Dolar')
real = float(input("Digite aqui seu valor em real: R$"))
dolar_hoje = 5.16
dolar = real / dolar_hoje

print('hoje seu dinheiro em dolar vale: US${:.2f}'.format(dolar))

# Conversão de dolar para real
print('Conversão de Dolar para Real')
dolar = float(input("Digite o valor em dolar: US$"))
dolar_hoje = 5.16
real = dolar_hoje * real

print('hoje seu dinheiro em Real vale: R${:.2f}'.format(real))
