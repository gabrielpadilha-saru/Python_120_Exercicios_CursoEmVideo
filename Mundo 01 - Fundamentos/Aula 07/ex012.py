"""
Faça um algoritmo que leio preço de um produto e mostre seu novo preço.
com 5% de desconto.
"""
preco = float(input('Qual é o preço do produto? R$'))
novo_preco = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${novo_preco}')
