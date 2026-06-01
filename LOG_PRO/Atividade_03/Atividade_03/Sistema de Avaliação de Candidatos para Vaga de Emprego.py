# ENTRADA DE DADOS
nome_candidato= input("digite seu nome: ")
idade=int(input("digite sus idade:"))
experiencia_anos=float(input("Digite quantos anos de experiência vocÊ tem na área:"))
nota_tecnica=float(input("Digite sua nota na prova técnica:"))
ingles = input("Possui inglês? (s ou n): ")
superior = input("Possui ensino superior completo? (s ou n): ")


#REGRAS DE PROCESSAMENTOS

#DADOS
dados_validos=True

if not (16 <= idade <= 70):
    print("Sua Idade não está válida para concorrer a vaga.")
    dados_validos=False

if(experiencia_anos < 0):
    print("Você não tem experiencia para concorrer a vaga.")
    dados_validos=False
    
if not (0 <= nota_tecnica <= 10):
    print("Você não tem nota para concorrer a vaga.")
    dados_validos = False

if not dados_validos:
    print("dados inválidos.")
    

#MEU PROGRAMA SO CONTINUARÁ SE OS DADOS FOREM VÁLIDOS.
if dados_validos:

    #CLASSIFICAÇÃO DA NOTA
    classificacao_nota = ""
    if 9 <= nota_tecnica <= 10:
        classificacao_nota= "Excelente"
    elif 7 <= nota_tecnica < 9:
        classificacao_nota = "Boa"
    elif 5 <= nota_tecnica < 7:
        classificacao_nota = "Regular"
    else:
        classificacao_nota = "Insuficiente"   

    #CLASSIFICAÇÃO DA EXPERIÊNCIA
    classificacao_experiencia = ""
    if experiencia_anos >= 5:
        classificacao_experiencia = "Sênior"
    elif 2 <= experiencia_anos < 5:
        classificacao_experiencia = "Pleno"
    elif 0 < experiencia_anos < 2:
        classificacao_experiencia = "Júnior"
    else:
        classificacao_experiencia = "Sem experiência"

    #CLASSIFICAÇÃO DA PONTUAÇÃO
    pontuacao_total = 0
    if nota_tecnica >= 7:
        pontuacao_total += 30
    elif 5 <= nota_tecnica < 7:
        pontuacao_total += 15
    if experiencia_anos >= 1:
        pontuacao_total += 20
    if ingles == 's':
        pontuacao_total += 20
    if superior == 's':
        pontuacao_total += 15
    if 18 <= idade <= 35:
        pontuacao_total += 15

    #PARECER FINAL
    parecer_final = ""
    if pontuacao_total >= 80:
        parecer_final = "APROVADO — Perfil excelente"
    elif 60 <= pontuacao_total <= 79:
        parecer_final = "APROVADO — Bom perfil"
    elif 40 <= pontuacao_total <= 59:
        parecer_final = "EM ANÁLISE — Perfil razoável"
    else:
        parecer_final = "REPROVADO — Perfil abaixo do esperado"

#MENSAGEM ADICIONAL
if classificacao_nota == "Insuficiente":
    parecer_final = "REPROVADO — Nota técnica eliminatória"

#RESULTADO
print("\n==========================================")
print("             RESULTADO FINAL              ")
print("==========================================")
print(f"Classificação da Nota: {classificacao_nota}")
print(f"Nível de Experiência:  {classificacao_experiencia}")
print(f"Pontuação Total: {pontuacao_total} pontos")
print(f"Parecer Final:   {parecer_final}")


if "APROVADO" not in parecer_final:
    if ingles != 's':
        print("Aviso: Recomenda-se curso de inglês")
    if superior != 's':
        print("Aviso: Recomenda-se graduação em andamento")


