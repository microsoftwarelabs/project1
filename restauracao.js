/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 

# Node.js necessário 

const fs = require('fs');

// Nome do arquivo a ser modificado
const nomeDoArquivo = 'exemplo.txt';

// Texto a ser colado no arquivo
const texto = 'Este é o novo texto que será adicionado ao arquivo.\n';

// Leitura do conteúdo do arquivo
fs.readFile(nomeDoArquivo, 'utf8', function (err, data) {
    if (err) {
        return console.log(err);
    }
    
    // Adicionando o novo texto ao conteúdo do arquivo
    const novoConteudo = data + texto;

    // Escrita do novo conteúdo no arquivo
    fs.writeFile(nomeDoArquivo, novoConteudo, 'utf8', function (err) {
        if (err) return console.log(err);
        console.log('Texto adicionado com sucesso!');
    });
});