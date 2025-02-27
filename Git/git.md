# Guia de Comandos Git

Este repositório contém uma lista de comandos GIT essenciais para gerenciar versões e trabalhar com repositórios.

## Comandos Iniciais e Configuração

-**`git init`**:  Inicializa um repositório Git em um diretório.
-**`git config --global user.name "Seu Nome"`** :  Define o nome de usuário global.
-**`git config --global user.email "seuemail@example.com"`** :  Define o email global.
-**`git config --global core.editor "editor"`**:  Define o editor de texto padrão (como: vim, nam, code, etc).

## STATUS E HISTÓRICO

-**`git status`**:Mostra o estado atual do repositório, incluindo arquivos modificados e não rastreados.
-**`git log`**:  Exibe o histórico de commits.
-**`git log --oneline`**:  Exibe o histórico de commits em uma linha por commit.
-**`git diff`**:  Mostra as diferenças entre os arquivos modificados e os arquivos no repositório.
-**`git diff --staged`**:  Mostra as diferenças dos arquivos que foram preparados para o commit.

## TRABALHANDO COM REPOSITÓRIOS REMOTOS

-**`git remote add origin <url>`**:  adiciona um repositório remoto com o nome origin.
-**`git remote -v`**:  Exibe as URLs dos repositórios remotos.
-**`git fetch`**:  Baixa as alterações de um repostório remoto sem aplicá-las.
-**`git pull`**:  Baixa as alterações e faz merge com a branch atual.
-**`git push`**:  Envia as alterações locais para o repositório remoto.
-**`git push origin <branch>`**:  Envia a branch local para o repositório remoto especificado.
-**`git clone <url>`**:  Clona um repositório remoto para o seu dietório local.

## MANIPULANDO BRANCHES

-**`git branch`**:  Exibe as branches locais no repositório.
-**`git branch <nome-da-branch>`**:  Cria uma nova branch
-**`git checkout <nome-da-branch>`**:   muda para a branch especificada.
-**`git checkout -b <nome-da-branch>`**:  Cria e muda para uma nova branch.
-**`git branch -d <nome-da-branch>`**:  Exclui uma branch local.
-**`git merge <nome-da-branch>`**:  Faz merge de outra branch na branch atual.
-**`git rebase <nome-da-branch>`**:  Reaplica commits da branch atual em cima da outra branch (útil para atualizar uma branch com alterações de outra).

## FAZENDO COMMITS

-**`git add <arquivo>`**:  Adiciona um arquivo específico para o próximo commit.
-**`git add .`**:  Adiciona todos os arquivos modificados e novos para o próximo commit.
-**`git commit -m "mensagem do commit"`**:  Faz commit com uma mensagem descritiva.
-**`git commit --amend`**:  Altera o último commit (útil para corrigir erros no commit anterior).

## TRABALHANDO COM ARQUIVOS

-**`git rm <arquivo>`**:  Remove um arquivo do repositório e da área de stage.
-**`git mv <arquivo-antigo> <arquivo-novo>`**:  Move ou renomeia um arquivo.

## REVERTENDO E DESFAZENDO ALTERRAÇÕES

-**`git reset <arquivo>`**:  Remove um arquivo da área de stage (não desfaz as mudanças no arquivo).
-**`git reset --hard`**:  Desfaz todas as alterações locais (atualiza o repositório local para o último commit).
-**`git revert <commit>`**:  Cria um novo commit que reverte as alterações de um cmmit anterior.
-**`git checkout -- <arquivo>`**:  Desfaz as alterações feitas em um arquivo (volta para o estado do último commit).

## TRABALHANDO COM STASHES

-**`git stash`**:  Salva temporariamente mudanças não comitadas para trabalhar em outra coisa.
-**`git stash pop`**:  Aplica o stash mais recente e remove-o da pilha.
-**`git stash list`**:  Lista todos os stashes salvos.
-**`git stash apply`**:  Aplica um stash sem removê-lo

## TRABALHANDO COM TAGS

-**`git tag`**:  Lista todas as tags no repositório.
-**`git tag <nome-da-tag>`**:  Cria uma nova tag.
-**`git tag -a <nome-da-tag> -m "mensagem"`**:  Cria uma tag anotada com uma mensagem.
-**`git push origin <nome-da-tag>`**:  Envia uma tag para o repositório remoto.
-**`git push --tags`**:  Envia todas as tags locais para o repositório remoto.
-**`git tag -d <nome-da-tag>`**:  Exclui uma tag local.

## REESCREVENDO HISTÓRICO ( ATENÇÃO )

-**`git rabase -i <commit-id>`**:  Inicia uma rebase interativa, permitindo editar commits anteriores ( útil para corrigir ou reorganizar commits).
-**`git cherry-pick <commit-id>`**:  Aplica um commit específico de uma branch para a branch atual.

## OUTROS COMANDOS ÚTEIS

-**`git stash save "Mensagem"`**:  salva mudançass em um stash com uma mensagem opcional.
-**`git clean -fd`**:  Remove arquivos não rastreados (como arquivos temporários ou gerados).
-**`git show <commit-id>`**:  Exibe detalhes de um commit específico.
-**`git ls-files`**:  Lista todos os arquivos rastreados no repositório.