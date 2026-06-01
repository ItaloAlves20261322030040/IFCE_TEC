"""Classificador de Triângulos
Escreva um programa que receba os três lados de um triângulo e:

Valide se os valores formam um triângulo válido:

Todos os lados devem ser maiores que zero
A soma de dois lados quaisquer deve ser maior que o terceiro lado — verifique os três casos:

a + b > c
a + c > b
b + c > a


Se inválido, exibir "Os valores não formam um triângulo." e encerrar


Se válido, classifique pelo tipo de lados:

Todos iguais → "Equilátero"
Dois iguais → "Isósceles"
Todos diferentes → "Escaleno"


Classifique pelos ângulos usando os quadrados dos lados:

Se a² + b² == c² (ou qualquer combinação) → "Retângulo"
Se a² + b² > c² → "Acutângulo"
Se a² + b² < c² → "Obtusângulo"
(considere c como o maior lado)


Exiba o resultado: -> Triângulo: Isósceles e Retângulo

"""

# ============================================
# CLASSIFICADOR DE TRIÂNGULOS
# Semana 3 — Lógica de Programação com Python
# ============================================

# ── ENTRADA DE DADOS ─────────────────────────

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

# ── VALIDAÇÃO ────────────────────────────────

lados_positivos = a > 0 and b > 0 and c > 0
desigualdade    = a + b > c and a + c > b and b + c > a
eh_triangulo    = lados_positivos and desigualdade

if not eh_triangulo:
    print("Os valores não formam um triângulo.")

else:

    # ── CLASSIFICAÇÃO POR LADOS ──────────────

    if a == b == c:
        classificacao_por_lados = "Equilátero"
    elif a == b or b == c or a == c:
        classificacao_por_lados = "Isósceles"
    else:
        classificacao_por_lados = "Escaleno"

    # ── CLASSIFICAÇÃO POR ÂNGULOS ────────────
    # Identifica o maior lado para usar na classificação

    maior = max(a,b,c)
    
    if a >= b and a >= c:
        maior    = a
        cateto1  = b
        cateto2  = c
    elif b >= a and b >= c:
        maior    = b
        cateto1  = a
        cateto2  = c
    else:
        maior    = c
        cateto1  = a
        cateto2  = b

    soma_quadrados    = cateto1 ** 2 + cateto2 ** 2
    quadrado_maior    = maior ** 2

    if soma_quadrados == quadrado_maior:
        classificacao_por_angulo = "Retângulo"
    elif soma_quadrados > quadrado_maior:
        classificacao_por_angulo = "Acutângulo"
    else:
        classificacao_por_angulo = "Obtusângulo"

    # ── SAÍDA ────────────────────────────────

    print(f"Triângulo: {classificacao_por_lados} e {classificacao_por_angulo}")
