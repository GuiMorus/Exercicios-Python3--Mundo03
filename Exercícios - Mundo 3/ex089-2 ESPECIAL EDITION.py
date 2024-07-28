# Sistema Boletim de Alunos 3.0 | by Guilherme Moreira
# https://github.com/GuiMorus

# Iniciando variáveis
dados = 'base-dados_alunos.txt'
alunos = []
ativo = True

# --- Verificando e criando base de dados --- #

try:
    # Criando mensagens do 0 para base nova
    with open(dados, 'x') as arquivo:
        arquivo.write("BASE DE DADOS: ALUNOS" + '\n')
        arquivo.write("Informações referente aos alunos com suas notas, média e situação de aprovação" + '\n\n')
        arquivo.write("Nome:\n" + "Primeira Nota:\n" + "Segunda Nota:\n")
        arquivo.write("Terceira Nota:\n" + "Média:\n" + "Situação:\n\n")
        arquivo.write("-\n")

    # Mensagem de sucesso da criação da base de dados
    print("Base de dados iniciada")

except FileExistsError:
    # Mensagem de base de dados carregada com sucesso
    print("Base de dados: Carregada com sucesso")


# --- Funções do sistema --- #

# Verificar float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Carregando cadastros da base para o sistema
def download():
    # Abrindo arquivo em modo leitura
    lendo = False
    contador = 0
    with open(dados, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip().replace("'", "")

            # Lendo os dados de cada aluno
            if lendo:
                match contador:
                    case 1:
                        dnome = str(linha)
                        contador += 1
                    case 2:
                        didade = int(linha)
                        contador += 1
                    case 3:
                        dnota1 = float(linha)
                        contador += 1
                    case 4:
                        dnota2 = float(linha)
                        contador += 1
                    case 5:
                        dnota3 = float(linha)
                        contador += 1
                    case 6:
                        dmedia = float(linha)
                        contador += 1
                    case 7:
                        dstatus = str(linha)

                        # Colocar dados dentro da lista alunos
                        alunos.append([dnome, didade, dnota1, dnota2, dnota3, dmedia, dstatus])
                        contador = 0
                        lendo = False

            # Verificando começo dos dados de cada aluno
            if linha == "-":
                lendo = True
                contador += 1


# Enviar cadastros para a base de dados
def upload():
    # Repetição enviando informações
    for n in range(0, len(alunos)):
        # Abrindo base de dados
        with open(dados, 'a') as arquivo:
            # Percorrendo aos valores dentro da lista
            for info in alunos[n]:
                # Escrevendo valor dentro do arquivo txt
                arquivo.write(str(info) + "\n")

                # Verificando ultimo valor da lista
                if alunos[n].index(info) == 6:
                    arquivo.write("-" + "\n")

    # Limpando lista alunos
    alunos.clear()


# Visualizar alunos cadastrados
def visualizar():
    # Carregar informações da base de dados
    download()

    # Introdução
    print("===[ PLANILHA DOS ESTUDANTES\n")

    # Organizando lista alunos
    alunos.sort()

    # Repetição criando planilha
    print(f"{'Nº':<3} {'NOME':<45} {'MÉDIA':<4}    {'SITUAÇÃO':<}")  # Cabeçalho
    print("-" * 70)
    for n in range(0, len(alunos)):
        pnome = alunos[n][0]
        pmedia = alunos[n][5]
        pstatus = alunos[n][6]

        # Mostrando informações
        if pstatus == 'Aprovado':
            pstatus = f"\033[32m{pstatus}\033[m"
        else:
            pstatus = f"\033[31m{pstatus}\033[m"
        print(f"{n + 1:<3} {pnome:<45} {pmedia:<4}     {pstatus:<}")

    # Laço para ver mais informações de um aluno
    while True:
        print("\nAcessar informações do estudante")
        op = str(input("N°: ").lower().strip())

        # Verificando encerramento do sistema
        if op == 'sair' or op == '0':
            break

        # Verificando se o ID é numérico
        if op.isnumeric():
            op = int(op) - 1

            # Verificando se o ID existe
            if 0 <= op < len(alunos):
                # Mostrando informações detalhadas do aluno
                print("\n" + "_" * 47)
                print(alunos[op][0])
                print(f"{alunos[op][1]} anos")
                print()  # Pular linha
                print(f"{'Primeira Nota: ':<15} {alunos[op][2]:<10}", end="")
                print(f"Média: {alunos[op][5]}")

                print(f"{'Segunda Nota:':<15} {alunos[op][3]:<10}", end="")
                print(f"Situação: {alunos[op][6]}")

                print(f"{'Terceira Nota:':<15} {alunos[op][4]:<4}")
                print("_" * 47)

                # Mensagem de encerramento
                print("\033[33m" + "para encerrar digite: sair", "\033[m")

            else:
                print("\033[31m" + "ESTUDANTE NÃO ENCONTRADO", "\033[m")

        else:
            print("\033[31m" + "Digite o número referente ao aluno", "\033[m")

    # Limpando lista
    alunos.clear()


# Cadastrar novos alunos
def cadastrar():
    # Introdução
    print("===[ CADASTRANDO ESTUDANTES")

    # Laço recolhendo as informações dos alunos
    while True:
        print()  # Pular linha
        nome = str(input("Nome do aluno(a): ").lower().strip().title())

        # Verificando saida
        if nome == 'Sair' or nome == '0':
            break

        idade = str(input("Idade do aluno(a): "))
        nota1 = str(input("1° Nota: ").replace(",", ".").strip())
        nota2 = str(input("2° Nota: ").replace(",", ".").strip())
        nota3 = str(input("3° Nota: ").replace(",", ".").strip())

        print("-" * 30)

        # Verificando se os dados são numéricos
        if nome.title() and idade.isnumeric() and is_float(nota1) and is_float(nota2) and is_float(nota3):

            # Formatando dados
            idade = int(idade)
            nota1 = float(nota1)
            nota2 = float(nota2)
            nota3 = float(nota3)

            # Calculando média e aprovação
            media = (nota1 + nota2 + nota3) / 3
            media = float(f"{media:.2f}")  # Formatando média

            if media >= 6:
                status = 'Aprovado'
            else:
                status = 'Reprovado'

            # Inserindo informações na lista alunos
            alunos.append([nome, idade, nota1, nota2, nota3, media, status])
            print("\033[32m" + "ESTUDANTE CADASTRADO COM SUCESSO!", "\033[m")

            # Inserindo dados na base de dados
            upload()

        else:
            print("\033[31m" + "DADOS INVÁLIDOS, TENTE NOVAMENTE", "\033[m")

        # Mensagem de saida
        print("\033[33m" + "para encerrar digite: sair", "\033[m")


# --- Sistema Principal --- #

while ativo:

    # Introdução
    print("\n")  # Pulando linha
    print("=" * 21, end="")
    print(" | SISTEMA DE BOLETIM |", end="")
    print("=" * 21)

    # Opções do sistema
    print("\033[32m" + "  [ 1 ] Visualizar Alunos", "\033[m", end="  ")
    print("\033[34m" + "[ 2 ] Cadastrar Alunos", "\033[m", end="  ")
    print("\033[31m" + "[ 0 ] SAIR", "\033[m")

    # Verificando opção selecionada
    while True:
        print()  # Pular Linha
        sistema = input("Digite a opção: ").lower().strip()

        if sistema == '1' or sistema == 'visualizar':
            visualizar()
            break

        elif sistema == '2' or sistema == 'cadastrar':
            cadastrar()
            break

        elif sistema == '0' or sistema == 'sair':
            ativo = False

            # Encerramento
            print("\n")  # Pulando linha
            print("=" * 21, end="")
            print(" | ENCERRANDO BOLETIM |", end="")
            print("=" * 21)

            break

        else:
            print("\033[31m" + "OPÇÃO INVÁLIDA, tente novamente", "\033[m")
