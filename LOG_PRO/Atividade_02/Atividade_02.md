Questões de Prática — Semana 2
Expressões Lógicas e Pensamento Booleano
Questão 1
Booleanos e conversão

O código abaixo contém três erros. Identifique cada um deles, explique o motivo e reescreva o código corrigido:

ativo = true 
# Erro: "true" deve ser "True" (com T maiúsculo) para ser reconhecido como um valor booleano em Python.

senha = input("Digite sua senha: ") 
# Erro: A variável "senha" é uma string, mas a comparação posterior espera um número inteiro. É necessário converter a entrada para um tipo numérico, como int.
# Correção:senha = int(senha)

acesso = senha == 1234
print(acesso)
# Erro: A entrada do usuário é sempre uma string, então a comparação com o número 1234 não funcionará corretamente.
# Correção: acesso = senha == 1234 (converter para int -  inteiro)




Questão 2
Operadores Lógicos

Complete a tabela abaixo com o resultado de cada expressão, considerando x = True e y = False:

Expressão           Resultado
x and y             False
x or y              True
not x               False
not y               True
x and not y         True
not x or y          False
not (x or y)        False  
not x and not y     False




Questão 3
Tradução português → código

Transforme cada regra abaixo em uma expressão Python. Use variáveis com nomes adequados:

a) Um aluno é aprovado se a nota for maior ou igual a 6 e a frequência for maior que 75.
# aluno_aprovado = nota >= 6 and frequencia > 75

b) Um cliente tem desconto se for estudante ou se o valor da compra for maior que 300 reais.
# tem_desconto = eh_estudante or valor_compra > 300

c) Um usuário pode acessar o sistema se estiver logado e o sistema não estiver em manutenção.
# pode_acessar = esta_logado and not sistema_em_manutencao

d) Um número é considerado inválido se for menor que 0 ou maior que 100.
# numero_invalido = numero < 0 or numero > 100



Questão 4
Tradução código → português

Leia cada expressão abaixo e escreva em português claro o que ela representa:

a)pode_viajar = tem_passagem and not viagem_cancelada
# Poderá viajar se tiver passagem e a viagem não estiver cancelada.

b)desconto = idade <= 12 or idade >= 60
# Terá desconto se tiver 12 anos ou menos, ou se tiver 60 anos ou mais.

c)aprovado = nota >= 5 and nota <= 10 and frequencia >= 75
# Será aprovado se a nota for entre 5 e 10 (inclusive) e a frequência for maior ou igual a 75%.

d)acesso_negado = not usuario_ativo or senha_errada
# Acesso será negado se o usuário não estiver ativo ou se a senha estiver errada.

Questão 5
Leitura e interpretação de expressões compostas

Dado o código abaixo, responda as perguntas sem executar (não enganem o professor):

idade = 17
saldo = 500
cliente_vip = True
em_promocao = False

r1 = idade >= 18 and saldo >= 100
# O resultado de r1 será False, pois a idade é menor que 18, mesmo que o saldo seja maior que 100.
r2 = idade >= 18 or cliente_vip
# O resultado de r2 será True, pois o cliente é VIP, mesmo que a idade seja menor que 18.
r3 = saldo >= 100 and (cliente_vip or em_promocao)
# O resultado de r3 será True, pois o saldo é maior que 100 e o cliente é VIP, mesmo que não esteja em promoção.
r4 = not cliente_vip or em_promocao
# O resultado de r4 será False, pois o cliente é VIP (not cliente_vip é False) e não está em promoção (em_promocao é False), então a expressão completa é False.
r5 = (idade >= 18 or cliente_vip) and not em_promocao
# O resultado de r5 será True, pois a idade é menor que 18, mas o cliente é VIP (idade >= 18 or cliente_vip é True) e não está em promoção (not em_promocao é True), então a expressão completa é True.
a) Qual o valor de cada variável r1 até r5?
# r1 = False
# r2 = True
# r3 = True
# r4 = False
# r5 = True
b) Explique com suas palavras o que a expressão r5 representa como regra de negócio.
# Terá acesso as promoções os clientes que são considerados vip e que tenham 18 anos ou mais.


Questão 6
Erro clássico — tipo errado na comparação

Um aluno escreveu o programa abaixo para verificar se o usuário tem 18 anos:

idade = input("Digite sua idade: ")
maior = idade >= 18
print("Maior de idade:", maior)
a) O programa vai funcionar corretamente? Por quê?
# Não, pois quando recebemos o dados ele é uma string, no caso "idade" para compararmos com um inteiro
# precisamos fazer um cast (conversão) para do dado para inteiro.
b) Que tipo de erro acontece?
# Python diz não ser possível um comparação de dados de tipos de diferentes.
c) Reescreva o programa corretamente.
# Resescrevendo progarama
idade = int (input("Digite sua idade: "))
maior = idade >= 18
print("Maior de idade:", maior)
# #######################################

Questão 7
Precedência lógica

Sem usar parênteses extras, determine o resultado de cada expressão abaixo. Depois reescreva cada uma com parênteses deixando explícita a ordem de avaliação:

# Considere:
a = True
b = False
c = True

# Expressões:
print(a or b and c)
# (True or (False and True))
# (True or False)
# True

print(not a or b and c)
# (not True or False and True)
# (False or (False and True))
# (False or False)
# False

print(a and b or not c)
# (True and False or not True)
# ((True and False) or False)
# (False or False)
# False

print(not a and b or c)
# (not True and False or True)
# ((False and False) or True)
# (False or True)
# True

print(a or not b and not c)
# (True or not False and not True)
# (True or (True and False))
# (True or False)
# True

Lembre-se da ordem: not → and → or

Questão 8
Construção de programa completo

Escreva um programa em Python que:

Peça ao usuário para digitar sua idade
Peça ao usuário para digitar sua nota (de 0 a 10)
Peça ao usuário para digitar sua frequência (de 0 a 100)
Calcule e armazene em variáveis booleanas:
Se o aluno é maior de idade (idade >= 18)
Se o aluno foi aprovado por nota (nota >= 6)
Se o aluno teve frequência suficiente (frequencia >= 75)
Se o aluno foi aprovado no geral (nota e frequência suficientes)
Exiba todos os resultados com print()

# Segue programa abaixo , questão 08.
# Solicitando os dados ao usuário
idade  = float(input ("Dgite sua idade: "))
nota   = float (input ("Dgite sua nota de  0 a 10 : "))
frequencia = float (input ("Dgite sua frequencia de 0 a 100 : "))


# Booleanos,  operadores de comparação e lógicos
maior_de_idade = idade >= 18
aprovado_nota = nota >= 6
frequencia_suficiente = frequencia >= 75

aprovado_geral = (aprovado_nota and frequencia_suficiente)


# Exibição dos resultados
print("\n--- Resultados ---")
print ( "Aluno é maior de idade.", maior_de_idade)
print ("Aluno aprovado por nota.",aprovado_nota)
print ("Aluno teve frenquência susficiente .",frequencia_suficiente)
print("Aluno foi Aprovado no Geral", aprovado_geral)
# Fim do programa


Questão 09
Análise crítica — armadilhas lógicas

Cada trecho abaixo contém uma armadilha sutil. Para cada um: identifique o problema, explique o que acontece e reescreva corretamente:

a) — O resultado sempre será True. Por quê?
numero = 5
print(numero == 3 or 5) 
# O Python não interpreta o 5 como parte da comparação numero == ,  o 5 será tratado como um valor isolado após o operador lógico "or".
# reescrevendo: numero = 5
# print(numero == 3 or numero == 5)


b) — Qual o resultado de bool("False")? Isso é intuitivo?
resposta = "False"
print(bool(resposta))
# O Python não ira ler o conteúdo como string. bool  verifica se a string está vazia, como resposta é uma string, mesmo que com  o nome false, o retorno será de True.
# print(resposta == "True")


c) — O que está errado na comparação?
nota = 8
print(nota > 5 and < 10)
# Existe um erro pois falta um elemento a menos para comparar após o 'and' com o < 10 .
# nota = 8
# print(nota > 5 and nota < 10)

d) — Por que esse resultado pode surpreender?
print(not True and False or True)
# Resolvendo o parentese respeitando a hierarquia (not, and, or) veiriquei que resultado é True:
# (False and False or True)
# True or True 
# True

e) — Esse código verifica se idade está entre 18 e 65?
idade = 30
print(18 <= idade <= 65)
É válido em Python? Seria válido em outras linguagens?
# Sim essa sintaxe é aceita no Python, 
# porém pesquisei que em outra lingugens como C, JAva e JavaScript não seria possivel tal comparação, 
# pois ele comparareia o primeiro termo 18 <= idade (resultando em True/1) e nunca conseguiria comparar 
# o resultado boleano com o inteiro 65.
