os scripts estão no branch "scripts"
the scripts are in the branch "scripts"
organization and testing phase. fase de organização e teste
# project1
design of a security system to make an application safe and self-repairing

Como vai funcionar? Esse sistema tratasse de um código que contem diversos script's para realizar diversas tarefas, tornando o aplicativo praticamente invulnerável contra ataques de vírus e mod's hackers

funções que o código realiza:

Correção de alteração não autorizada no código do arquivo.

Verificação da integridade do código do arquivo.

Criptografia de dados pré-selecionados.

Guardar uma cópia criptografada do código do arquivo.

Fazer alerta de segurança ao usuário e desenvolvedor.

Eu sei como fazer cada uma dessas coisas e posteriormente estarei colocando o código aqui neste repositório.

How will it work? This system is a code that contains several scripts to perform various tasks, making the application practically invulnerable against virus attacks and hacker mods.


functions that the code performs:

Correction of an unauthorized change in the file code.

Checking the integrity of the file code.

Encryption of pre-selected data.

Save an encrypted copy of the file code.

Make security alerts to the user and developer.


I know how to do each of these things and I'll be posting the code here in this repository at a later date.


# publicar
- [ ] script para guarda backup do codigo
- [ ] script para repara o codigo apartir do backup
- [ ] proteção contra debug
- [ ] script para criptografar informações senssiveis
- [ ] script para transmitir informações senssiveis 
- [ ] script para guardar informações sensiveis
- [ ] script para reparar o programa 
- [ ] manual de uso
- [ ] adss
- [ ] script de alerta remoto
- [ ] script de varedura
- [ ] script para verificar pgp
- [ ] script para rastrear erros
- [ ] script para alerta
- [ ] script de travamento
- [ ] script para servidor 
- [ ] rsa 1kbit p2p
- [ ] log
- [ ] proteção de memoria ram
- [ ] integração com kernel
- [ ] anti-keyloger
- [ ] relatorio de desempenho
- [ ] modulo blueprint
- [ ] integração do backup com as tarefas de restauração
- [ ] varedura de pasta
- [ ] antivirus em nuvem
- [ ] antichit

# publish
- [ ] script to save code backup
- [ ] script to repair code from backup
- [ ] debug protection
- [ ] script to encrypt sensitive information
- [ ] script to transmit sensitive information 
- [ ] script to store sensitive information
- [ ] script to repair the program 
- [ ] user manual
- [ ] adss
- [ ] remote alert script
- [ ] scan script
- [ ] script to check pgp
- [ ] error tracking script
- [ ] alert script
- [ ] crash script
- [ ] server script 
- [ ] rsa 1kbit p2p
- [ ] log
- [ ] ram memory protection
- [ ] kernel integration
- [ ] anti-keyloger
- [ ] performance report
- [ ] blueprint module
- [ ] backup integration with restore tasks
- [ ] folder scanning
- [ ] cloud antivirus
- [ ] antichit

explicação da implementação:

Os scripts mencionados têm como objetivo implementar um sistema de segurança integrado para proteger o código principal (main.py) de alterações não autorizadas e cheats. Vou explicar cada um deles de forma pedagógica, considerando que você é leigo no assunto.

1. Script de verificação:
Esse script tem a função de verificar o conteúdo do código principal ( exemplo "main.py" ) comparando-o com a variável "codigodoarquivomainpython". Ele busca qualquer diferença entre o código atual e o conteúdo original armazenado na variável, identificando possíveis alterações não autorizadas.

2. Script cache:
O script cache utiliza uma variável e ou arquivo log  para armazenamento de logs, que contém informações importantes para o funcionamento do programa, essas informações podem ser criptografadas para aumentar a privacidade do usuário. Ao invés de manter essas informações na memória RAM, elas são salvas em disco. Isso otimiza o desempenho e permite recuperar os dados em caso de falhas ou reinicialização do sistema.

3. Script restauração:
O script de restauração tem a função de copiar o valor armazenado na variável "codigodoarquivomainpython" e colá-lo no arquivo main.py. Esse procedimento garante que o código principal seja sempre consistente com o conteúdo original, evitando modificações indevidas.

4. Script criptografia:
Esse script verifica as variáveis que devem ser criptografadas, utilizando como base a variável "criptografeesses". A criptografia é uma técnica de segurança que transforma os dados legíveis em uma forma ilegível, dificultando o acesso não autorizado às informações sensíveis.

5. Script anti-keylogger:
Esse script possui uma particularidade interessante, pois ele digita dentro de si mesmo. Ele age como uma medida de segurança contra keyloggers, que são programas maliciosos que registram todas as teclas digitadas pelo usuário. Ao digitar dentro do próprio script, o anti-keylogger impede a captura dessas informações.

6. Script de integração JavaScript e HTML:
Esse script permite a integração do código Python com elementos JavaScript e HTML. Essa combinação de tecnologias possibilita a criação de interfaces mais dinâmicas e interativas para o usuário, melhorando a experiência e também adicionando camadas adicionais de segurança.

7. Script de verificação no arquivo main.py:
Por último, esse script realiza a verificação da existência e integridade dos demais scripts mencionados (restauração, reconhecimento, criptografia, cache e anti-keylogger). Ele garante que todos esses scripts estejam presentes e funcionando corretamente no código principal (main.py), formando assim um sistema de segurança integrado.

Todos esses scripts, juntamente com o código principal ( exemplo "main.py" ), trabalham em conjunto para garantir a existência, integridade e segurança do programa. Eles atuam na prevenção de alterações não autorizadas e cheats, bem como na proteção de informações sensíveis.

os valores das variáveis do script de verificação e restauração devem ser alterados para conter dentro de si o código que você queira proteger, mas não se esqueça de colocar scripts dentro do código protegido para verificar a existência e integridade dos script desse sistema de segurança.

exemplos:






explanation of implementation:

The scripts mentioned aim to implement an integrated security system to protect the main code (main.py) from unauthorized changes and cheats. I'm going to explain each of them in a pedagogical way, considering that you are a layperson on the subject.

1. Verification script:
This script has the function of checking the content of the main code ( example "main.py" ) by comparing it with the variable "codigodoarquivomainpython". It looks for any difference between the current code and the original content stored in the variable, identifying possible unauthorized changes.

2. Cache script:
The cache script uses a variable and or log file to store logs, which contain important information for the operation of the program, this information can be encrypted to increase user privacy. Instead of keeping this information in RAM, it is saved on disk. This optimizes performance and allows data to be recovered in the event of system crashes or reboots.

3. Restore script:
The restore script has the function of copying the value stored in the "mainpythonfilecode" variable and pasting it into the main.py file. This procedure ensures that the main code is always consistent with the original content, avoiding undue modifications.

4. Encryption script:
This script checks the variables that should be encrypted, using the "cryptografeesses" variable as a base. Encryption is a security technique that transforms readable data into an unreadable form, making it difficult to gain unauthorized access to sensitive information.

5. Anti-keylogger script:
This script has an interesting feature in that it types within itself. It acts as a security measure against keyloggers, which are malicious programs that record all the keystrokes made by the user. By typing inside the script itself, the anti-keylogger prevents this information from being captured.

6. JavaScript and HTML integration script:
This script allows Python code to be integrated with JavaScript and HTML elements. This combination of technologies makes it possible to create more dynamic and interactive interfaces for the user, improving the experience and also adding additional layers of security.

7. Verification script in the main.py file:
Finally, this script checks for the existence and integrity of the other scripts mentioned (restore, reconnaissance, encryption, cache and anti-keylogger). It ensures that all these scripts are present and working correctly in the main code (main.py), thus forming an integrated security system.

All these scripts, together with the main code ("main.py" example), work together to guarantee the existence, integrity and security of the program. They act to prevent unauthorized changes and cheats, as well as protecting sensitive information.

the values of the check and restore script variables should be changed to contain within them the code you want to protect, but don't forget to place scripts within the protected code to check the existence and integrity of the scripts in this security system.

examples:
