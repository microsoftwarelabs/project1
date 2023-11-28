/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 


from hashlib import sha256
import time
import random
import string

duracao = 30  # 30 segundos
codigo_secreto = "código secreto"


def generate_hash(password):
    # Convertendo a senha para bytes
    password_bytes = password.encode('utf-8')

    # Gerando o hash SHA256
    sha256_hash = sha256(password_bytes).hexdigest()

    # Convertendo o hash para um número binário
    binary_hash = bin(int(sha256_hash, 16))[2:]

    # Gerando uma sequência aleatória de caracteres
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=6000000000 - len(binary_hash)))

    # Concatenando o hash binário com os caracteres aleatórios
    padded_hash = binary_hash + random_chars

    return padded_hash


# Senha secreta
senha_secreta = "minha_senha_secreta"

# Gerando o hash
hash_6000000000_bits = generate_hash(senha_secreta)

# Imprimindo o hash
print(hash_6000000000_bits)

# Tempo atual
tempo = time.time()
tempo_hash = (tempo // duracao) * duracao
tempo_restante = duracao - (tempo % duracao)

senha = hash_6000000000_bits + str(tempo_hash)
hash_hex = sha256(senha.encode('utf-8')).hexdigest()
hash_int = int(hash_hex, 16)  # convertendo para inteiro
hash_6000_digitos = str(hash_int)[-6000:]  # obtendo os últimos 6000 dígitos

print("Código de verificação:", hash_6000_digitos)
print("Tempo restante:", tempo_restante, "segundos")