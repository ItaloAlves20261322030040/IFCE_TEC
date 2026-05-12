#9. Cálculo de desconto
#Peça:preço de um produto
#Peça:percentual de desconto
#Mostre:valor do desconto
#Mostre:preço final
preco = float(input("Digite o preço do produto:"))
desconto = float(input("Digite o desconto '%' a ser praticado:"))
valor_do_desconto = preco*(desconto/100)
print("Valor do desconto será de: ",valor_do_desconto)

preco_final=preco-valor_do_desconto
print("Preço final do produto será de: ",preco_final)