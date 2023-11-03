/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 

<?php

// Generate a random key
$key = openssl_random_pseudo_bytes(32);

// Encrypt the data
$encrypted = openssl_encrypt($data, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);

// Decrypt the data
$decrypted = openssl_decrypt($encrypted, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);

?>
