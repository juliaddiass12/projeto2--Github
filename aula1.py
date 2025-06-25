Filmes=[]

def cor_texto(texto, cor):
    cores = {
        'vermelho': '\033[91m',
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'roxo': '\033[95m',
        'reset': '\033[0m',
        'ciano': '\033[96m',
        'cinza': '\033[90m',
        'branco': '\033[97m',
        'negativo': '\033[1m',
        'sublinhado': '\033[4m',
        'vermelho_escuro': '\033[38;5;124m',} # Vermelho Escuro
    return cores.get(cor, '') + texto + cores['reset']
print(cor_texto('==== Sistema De Filmes e Séries ====', 'vermelho_escuro'))
print('------------------------------------')


def cadastrar_filmes():
    nome= str(input('Digite o nome do filme ou série que deseja cadastrar: '))
    plataforma= str(input('Qual a plataforma que será usada: '))
    genero= str(input('Qual o gênero: '))
    atualizacao = str(input('Já foi assistido ou está assistindo ou não foi assistido: '))
    Filme = {'nome':nome,
              'plataforma':plataforma,
              'genero':genero,
              'atualizacao':atualizacao}
    Filmes.append(Filme)
    print("==😁😁Filme ou Série cadastrada com Sucesso!!!😁😁==")
    print("")


def mostrar_cadastrados():
    if len(Filmes)==0:
        print('nenhuma sessao cadastrada.❌❌❌\n')
        return
    numero=1
    for filme in Filmes:
        status=''
        print(f'[{numero}] nome:{filme['nome']}  gênero:{filme['genero']}   plataforma:{filme['plataforma']}')
        print('')
        numero+=1

def buscar_filmes():
    sessoes=str(input("Busque por gênero ou plataforma:"))
    sessoes_encontrados=[]
    for filme in Filmes:
        if (sessoes in filme['genero']) or (sessoes in filme['plataforma']):
            sessoes_encontrados.append(filme)
    if len(sessoes_encontrados) ==0:
        print('nenhum filme cadastrado❌❌❌ \n')
        return
    for filme in sessoes_encontrados:
        if filme['atualizacao'] == True:
            status = '✅ cadastrada'
        else:
            status = '❌ não cadastrada'
            print(f'nome:{filme['nome']}  gênero:{filme['genero']}   plataforma:{filme['plataforma']} status:{filme['atualizacao']}')
            print("")


def exibir_menu():
    while True:
        print('=== Sistema de Filmes e Séries ===')
        print('1- Cadastrar novo Filme ou Série✍✍✍')
        print('2- Buscar por gêneros e plataforma✨✨ ')
        print('3- Ver todos os Filmes e Séries😎🎇')
        print('4- Sair🤗🤗')

        escolha = str(input('Escolha uma opção: '))
        if escolha == '1':
            cadastrar_filmes()
        elif escolha == '2':
            buscar_filmes()
        elif escolha == '3':
            mostrar_cadastrados()
        elif escolha == '4':
           print(' Saindo do Sistema. Até a próxima')
           break
        else:
            print('Opção Inválida. Tente novamente. \n')


exibir_menu()




