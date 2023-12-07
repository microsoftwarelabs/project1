from cryptography.fernet import Fernet
import sqlite3

# Chave de criptografia (gerada uma vez e mantida em segredo)
chave = Fernet.generate_key()
cipher_suite = Fernet(chave)

# Valor a ser criptografado
valor_original = 'valor_secreto'

# Criptografar o valor
valor_criptografado = cipher_suite.encrypt(valor_original.encode())

# Conectar ao banco de dados
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Inserir o valor criptografado no banco de dados
cursor.execute("INSERT INTO tabela (campo_criptografado) VALUES (?)", (valor_criptografado,))
conexao.commit()

# Fechar a conexão
conexao.close()