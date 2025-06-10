def file_exists(name):
    """
    Verifica se um arquivo existe no sistema.
    Parâmetros: name (str): O nome (ou caminho) do arquivo a ser verificado.
    Retorna:    bool: True se o arquivo existir, False se não existir.
    """
    try:
        with open(name, 'r') as file:
            return True
    except FileNotFoundError:
        return False
    except Exception as error:
        print(f'Erro ao verificar o arquivo: {error}')


def create_file(name):
    """
    Cria um novo arquivo com o nome especificado, se ele ainda não existir.

    Parâmetros:  name (str): O nome (ou caminho) do novo arquivo.

    Retorna:     None
    """
    if not file_exists(name):
        try:
            with open(name, 'w') as file:
                file.write('')
            print(f'Arquivo {name} criado com Sucesso!')
        except Exception as error:
            print(f'Falha ao criar arquivo: {error}')    
    else:
        print(f'O arquivo {name} ja existe')


def copy_file(source, destination):
    """
    Copia o conteúdo de um arquivo de origem para um arquivo de destino.
    Parâmetros:
        source (str): Caminho do arquivo de origem.
        destination (str): Caminho do arquivo de destino.

    Retorna:  None
    """
    if file_exists(source):
        try:
            #Lê conteudo do arquivo de origem
            with open(source, 'r', encoding='utf-8') as src:
                content = src.read()
            
            #Grava o conteúdo no novo arquivo
            with open(destination, 'w', encoding='utf-8') as dst:
                dst.write(content)
            print(f'Arquivo copiado de {source} para {destination} com Sucesso!')
        except Exception as error:
            print(f'Erro ao copiar arquivo: {error}')