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
        'laranja': '\033[38;5;208m', # Laranja
        'azul_claro': '\033[38;5;111m', # # Azul Claro
        'verde_claro': '\033[38;5;118m', # Verde Claro
        'magenta': '\033[38;5;165m', # Magenta
        'violeta': '\033[38;5;93m', # Violeta
        'marrom':'\033[38;5;130m', # Marrom
        'peach': '\033[38;5;223m', # Peach (Pêssego)
        'petróleo': '\033[38;5;37m', # Petróleo
        'turquesa': '\033[38;5;51m', # Turquesa
        'bege': '\033[38;5;178m', #bege
        'rosa': '\033[38;5;201m', # Rosa
        'dourado': '\033[38;5;220m', # Dourado
        'vermelho_escuro': '\033[38;5;124m', # Vermelho Escuro
        'verde_escuro': '\033[38;5;28m', # Verde Escuro
        'azul_escuro': '\033[38;5;34m', # Azul Escuro
        'azul_turquesa': '\033[38;5;45m', # Azul Turquesa
        'amarelo_escuro': '\033[38;5;136m', # Amarelo Escuro
        'cinza_claro': '\033[38;5;250m', # Cinza Claro
        'cinza_escuro': '\033[38;5;238m', # Cinza Escuro
        'azul_bebe': '\033[38;5;12m', # Azul Bebê
        'verde_bebe': '\033[38;5;46m', # Verde Bebê
        'amarelo_bebe': '\033[38;5;226m', # Amarelo Bebê
        'roxo_escuro': '\033[38;5;93m', # Roxo Escuro
        'laranja_claro': '\033[38;5;214m', # Laranja Claro
        'verde_menta': '\033[38;5;80m', # Verde Menta
        'ciano_claro': '\033[38;5;51m', # Ciano Claro
        'ciano_escuro': '\033[38;5;32m', # Ciano Escuro
        'cobre': '\033[38;5;130m'} # Cobre
     return cores.get(cor,'') + texto + cores['reset']
print(cor_texto('==== Sistema De Filmes e Séries ====','vermelho_escuro'))
print('------------------------------------')


def cadastrar_filmes():
    print(cor_texto('CADASTRAR O FILME/SÉRIE✍️✍️','azul_bebe'))
    nome= str(input('Digite o nome do filme ou série que deseja cadastrar: '))
    plataforma= str(input('Qual a plataforma que será usada: '))
    genero= str(input('Qual o gênero: '))
    atualizacao = str(input('Já foi assistido ou está assistindo ou não foi assistido: '))
    Filme = {'nome':nome,
              'plataforma':plataforma,
              'genero':genero,
              'atualizacao':atualizacao}
    Filmes.append(Filme)
    print(cor_texto("😁😁Filme ou Série cadastrado com Sucesso!!!😁😁",'turquesa'))
    print("")


def mostrar_cadastrados():
    print(cor_texto('VER OS FILME/SÉRIE CADASTRADOS😎', 'azul_bebe'))
    if len(Filmes)==0:
        print(cor_texto('Nenhum filme/série cadastrado.❌❌❌\n','vermelho_escuro'))
        return
    numero=1
    for filme in Filmes:
        status=''
        print(f'[{numero}] nome:{filme['nome']}  gênero:{filme['genero']}   plataforma:{filme['plataforma']} status{filme['atualizacao']}')
        print('')
        numero+=1

def buscar_filmes():
    print(cor_texto('BUSCAR O FILME/SÉRIE👓👓', 'azul_bebe'))
    movies =str(input("Busque por gênero ou plataforma: ")).lower()
    movies_encontrados=[]
    for filme in Filmes:
        if (movies in filme['genero']) or (movies in filme['plataforma']):
            movies_encontrados.append(filme)
    if len(movies_encontrados) ==0:
        print(cor_texto('Nenhum filme/série cadastrado❌❌❌ \n','vermelho_escuro'))
        return
    for filme in movies_encontrados:
        if filme['atualizacao'] == True:
            status = 'cadastrado😁'
        else:
            status = 'não cadastrado😭'
            print(f'nome:{filme['nome']}  gênero:{filme['genero']}   plataforma:{filme['plataforma']} status:{filme['atualizacao']}')
            print("")


def exibir_menu():
    while True:
        print(cor_texto('==== 🎇Menu Inicial🎇 ====', 'violeta'))
        print(cor_texto('1- ✍️Cadastrar novo Filme ou Série✍️','azul_bebe'))
        print(cor_texto('2- 🔎Buscar por gênero ou plataforma🔎 ','azul_bebe'))
        print(cor_texto('3- 😎Ver todos os Filmes e Séries😎','azul_bebe'))
        print(cor_texto('4- Sair👋👋','vermelho'))

        escolha = str(input('Escolha uma opção: '))
        print()
        if escolha == '1':
            cadastrar_filmes()
        elif escolha == '2':
            buscar_filmes()
        elif escolha == '3':
            mostrar_cadastrados()
        elif escolha == '4':
           print(' Saindo do Sistema. Até a próxima!!😘')
           break
        else:
            print('Opção Inválida. Tente novamente. \n')


exibir_menu()