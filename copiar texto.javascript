/*
Autor: microsoftwarelabs
numero de contato no zang: https://services.zangi.com/dl/conversation/1094194496
technical support:https://www.vivaolinux.com.br/~cumestive
Os direitos autorais desse código pertencem à organização microsoftweralabs.
The copyright of this Code belongs to the MicrosoftWeralabs organization.
*/ 
/* texto na caixa de texto: */

function copiarTexto() {
/* Selecionamos por ID o nosso input */
var textoCopiado = document.getElementById("texto-usuario");

/* Deixamos o texto selecionado (em azul) */
textoCopiado.select();
textoCopiado.setSelectionRange(0, 99999); /* Para mobile */

/* Copia o texto que está selecionado */
document.execCommand("copy");

alert("Texto copiado: " + textoCopiado.value);
}
