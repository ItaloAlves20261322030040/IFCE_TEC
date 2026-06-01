# Inicialização das variáveis
soma_total_vendas = 0
total_itens_vendidos = 0
contador_acima_100 = 0
maior_preco_unitario = 0
nome_mais_caro = ""
maior_faturamento = 0
nome_maior_faturamento = ""

# Validação de quantidade de produtos
while True:
    qtd_produtos = int(input("Quantos produtos serão registrados? "))
    if qtd_produtos > 0:
        break
    print("O número deve ser maior que zero.")
    
contador = 0

# Processamento
while True:
    if contador >= qtd_produtos:
        break
    
    contador += 1
    print(f"\n--- Produto {contador} ---")
    
    # Validação nome do produto
    while True:
        nome = input("Nome do produto: ").strip()
        if len(nome) >= 3:
            break
        print("O nome deve ter pelo menos 3 caracteres.")

    # Validação quantidade do produto
    while True:
        quantidade = int(input(f"Quantidade de '{nome}': "))
        if quantidade > 0:
            break
        print("A quantidade deve ser maior que zero.")

    # Validação preço do produto
    while True:
        preco = float(input(f"Preço unitário de '{nome}': "))
        if preco > 0:
            break
        print("O preço deve ser maior que zero.")
        
    # Cálculos por produto
    valor_total_produto = quantidade * preco

    if valor_total_produto > 500:
        print("Venda de alto valor registrada!")
    if quantidade > 50:
        print("Grande volume de vendas registrado!")
        
    if valor_total_produto <= 100:
        print("Classificação: Baixa")
    elif valor_total_produto <= 500:
        print("Classificação: Média")
    else:
        print("Classificação: Alta")
    
    
    # Acumuladores globais
    soma_total_vendas += valor_total_produto
    total_itens_vendidos += quantidade
    
    if valor_total_produto > 100:
        contador_acima_100 += 1
        
    # Verificação de maior preço unitário
    if preco > maior_preco_unitario:
        maior_preco_unitario = preco
        nome_mais_caro = nome
        
    # Verificação de maior faturamento individual
    if valor_total_produto > maior_faturamento:
        maior_faturamento = valor_total_produto
        nome_maior_faturamento = nome

# Relatório Final E saída de Dados
print("\n----------------------------------------")
print("          RELATÓRIO FINAL")
print("----------------------------------------")
print(f"Produtos registrados : {qtd_produtos}")
print(f"Total de itens : {total_itens_vendidos}")
print(f"Total de vendas : R$ {soma_total_vendas:.2f}")
print(f"Vendas acima R$100 : {contador_acima_100}")
print("----------------------------------------")
print(f"Produto mais caro : {nome_mais_caro} - R$ {maior_preco_unitario:.2f}")
print(f"Maior faturamento : {nome_maior_faturamento} - R$ {maior_faturamento:.2f}")
print("----------------------------------------")
print(f"MÉDIA por venda : R$ {soma_total_vendas/qtd_produtos:.2f}")
print("----------------------------------------")