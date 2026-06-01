"""Enunciado
Você foi contratado para desenvolver o menu principal de um sistema interno de uma pequena empresa. 
O sistema precisa receber a opção escolhida pelo usuário e direcioná-lo para o módulo correto.
Implemente um programa em Python que:

1. Exiba o menu abaixo para o usuário:

=== SISTEMA ===
1 - Cadastrar
2 - Consultar
3 - Relatório
4 - Sair

Receba a opção digitada pelo usuário
Direcione para o módulo correto conforme a opção escolhida:

Opção 1 → exibir "Abrindo cadastro..."
Opção 2 → exibir "Abrindo consulta..."
Opção 3 → exibir "Gerando relatório..."
Opção 4 → exibir "Até logo!"
Qualquer outra opção → exibir "Opção inválida. Escolha entre 1 e 4."


Use obrigatoriamente a estrutura match/case para tratar as opções

"""

print("""
=== SISTEMA ===
1 - Cadastrar
2 - Consultar
3 - Relatório
4 - Sair""")

opcao = int(input("Digite a opção deseja: "))

match opcao:
    case 1:
        print("Abrindo Cadastro...")
    case 2:
        print("Abrindo Consulta...")
    case _:
        print("Opção inválida")
        