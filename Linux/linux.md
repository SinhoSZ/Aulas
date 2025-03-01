## Navegação e Manipulação de Arquivos

- **`pwd`** Mostra o diretório atual.
- **`ls`** Lista arquivos e diretórios no diretório atual.
- **`cd nome_da_pasta`** Entra em um diretório.
- **`cd ..`** Volta um nível na hierarqui de diretório.
- **`mkdir nome_da_pasta`** Cria um novo diretório.
- **`rmdir nome_da_pasta`** Remove um diretório vazio.
- **`rm nome_do_arquivo`** Remove um arquivo.
- **`rm -r nome_da_pasta`** Remove um diretório e todo o seu conteúdo.
- **`touch nome_do_arquivo`** Cria um novo arquivo vazio.
- **`cp origem destino`** Copia um arquivo ou diretório.
- **`mv origem destino`** Move ou renomeia arquivos e diretórios.

## Visualização de Arquivos

- **`cat nome_do_arquivo`** Exibe o conteúdo de um arquivo.
- **`less nome_do_arquivo`** Permite visualizar arquivos longos de forma interativa.
- **`head -n 10 nome_do_arquivo`** Exibe as primeiras 10 linhas do arquivo.
- **`tail -n 10 nome_do_arquivo`** Exibe as últimas 10 linhas do arquio.

## Permissões e Usuários

- **`chmod +x nome_do_arquivo`** Dá permissão de execução a um arquivo.
- **`chown usuario:grupo nome_do_arquivo`** Muda o dono de um arquivo.
- **`whoami`** Mostra o nome do usuário atual.
- **`sudo comando`** Executa um comando como superusuário.
- **`passwd`** Altera a senha do usuário atual.

## Processos e Monitoramento

- **`ps aux`** Lista todos os processos em execução.
- **`top`** Exibe processos em tempo real, semelhante ao Gerenciador de Tarefas.
- **`kill PID`** Encerra um processo pelo seu ID (PID).
- **`killall nome_do_programa`** Encerra todos os processos de um programa.

## Rede e Internet

- **`ifcofig`** Mostra informações da rede (subsituído por **`ip a`** em versões mais recentes).
- **`ping google.com`** Testa a conexão com um servidor.
- **`wget URL`** Baixa arquivos da internet.
- **`curl URL`** Baixa ou envia dados para uma URL

## Gerenciamento de Pacotes (Ubuntu - APT)

- **`sudo apt update`** Atualiza a lista de pacotes disponíveis.
- **`sudo apt upgrade`** Atualiza todos os pacotes instalados.
- **`sudo apt install nome_do_pacote`** Instala um pacote.
- **`sudo apt remove nome_do_pacote`** Remove um pacote.