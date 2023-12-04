/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 


# Abre o arquivo no modo de leitura e le todas as linhas
with open('seu_arquivo.txt', 'r') as file:
    linhas = file.readlines()

# Adiciona o texto desejado ao final da lista de linhas
texto_a_adicionar = "Este é o novo texto que será adicionado."
linhas.append(texto_a_adicionar + "\n")  # Adiciona uma quebra de linha no final do texto

# Abre o arquivo no modo de escrita e escreve todas as linhas, incluindo o novo texto
with open('seu_arquivo.txt', 'w') as file:
    file.writelines(linhas)