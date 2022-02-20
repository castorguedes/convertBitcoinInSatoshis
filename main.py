# O Satoshi é a menor forma de fracionar o Bitcoin,
# assim como os centavos são a menor foma de fracionar o Real.
# Por exemplo: 100 centavos são iguais a R$1 enquanto
# 100.000.000 Satoshis correspondem a 1 Bitcoin.

qtdBtcUsu = float(input('Quantas BTC você possui? Utilize o formato norte-americano (Casas decimais separadas por um ponto): '))
qtdStsUsu = float(100000000*qtdBtcUsu) #Variavel fixa com a formula de conversão entre Bitcoin e Satoshis
btcBRL = 205019.38 #Variavel fixa com a cotação do Bitcoin em Reais no dia 20/02/22
btcUSD = 39894.80 #Variavel fixa com a cotação do Bitcoin em Dolares no dia 20/02/22
calculoBRL = qtdBtcUsu * btcBRL #Conversão de BTC para BRL
calculoUSD = qtdBtcUsu * btcUSD #Conversão de BTC para USD
textoCalculoBRL = f'R$ {calculoBRL:,.2f}' #Adicionando o separador de milhar do BRL
textoCalculoUSD = f'US$ {calculoUSD:,.2f}' #Adicionando o separador de milhar do USD
textoQtdStsUsu = f'{qtdStsUsu:,.2f} Satoshis' #Adicionando o separador de milher dos Satoshis

print()

print(f'{qtdBtcUsu} Bitcoin(s) no dia 20/02/22 valia(m) {(textoCalculoBRL)}')
print(f'{qtdBtcUsu} Bitcoin(s) no dia 20/02/22 valia(m) {(textoCalculoUSD)}')
print(f'{qtdBtcUsu} Bitcoin(s) equivalem a {(textoQtdStsUsu)}')