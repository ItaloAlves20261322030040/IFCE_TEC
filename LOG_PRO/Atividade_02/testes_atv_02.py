



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





