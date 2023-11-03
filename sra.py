/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 

import gnupg
import rsa

# Create a GPG object
gpg = gnupg.GPG()

# Generate a new RSA key pair
(pubkey, privkey) = rsa.newkeys(2048)

# Encrypt a message using the public key
encrypted_message = gpg.encrypt("This is a secret message", pubkey)

# Decrypt the message using the private key
decrypted_message = gpg.decrypt(encrypted_message, privkey)

# Print the decrypted message
print(decrypted_message)
