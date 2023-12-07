/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 

import difflib

# Importe o módulo os para lidar com caminhos de arquivos

import os

# Obtenha o caminho do diretório atual
caminho_atual = os.path.dirname(__file__)

# Nome do arquivo que você quer ler
codigodoarquivomainpython = "main.py"

# Caminho completo do arquivo
caminho_completo = os.path.join(caminho_atual, nome_arquivo)

# Duas strings de códigos para comparação
codigo1 = codigodoarquivomainpython

codigo2 = '''
def soma(a, b):
    return a + b
'''

# Converte as strings em listas de linhas
linhas_codigo1 = codigo1.splitlines()
linhas_codigo2 = codigo2.splitlines()

# Cria um objeto Differ
d = difflib.Differ()

# Compara as listas de linhas
diff = list(d.compare(linhas_codigo1, linhas_codigo2))

# Exibe as diferenças
for linha in diff:
    print(linha)