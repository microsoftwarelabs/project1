
#Autor: Populim
#Os direitos autorais desse código pertencem à organização Microsoftwarelabs.
#The copyright of this Code belongs to the Microsoftwarelabs organization.


from hashlib import sha256
import time

duracao = 30 # 30 segundos
codigo_secreto = "código secreto"

tempo = time.time()
tempo_hash = (tempo//duracao)*duracao
tempo_restante = duracao - (tempo % duracao)

senha = codigo_secreto + str(tempo_hash)
hash_hex = sha256(senha.encode('utf-8')).hexdigest()
hash_int = int(hash_hex, 16) # convertendo pra int
hash_6_digitos = hash_int % 10**6 # pegando os 6 ultimos digitos

print("código de verificação:",hash_6_digitos)
print("Tempo restante: ", tempo_restante, "segundos")
