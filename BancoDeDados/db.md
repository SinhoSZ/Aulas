# Guia de Comandos SQL

## **Criação de Tabelas**
**`CREATE TABLE`**: Cria uma nova tabela.

```sql
CREATE TABLE nome_da_tabela (
    coluna1     tipo_de_dados   restrições
    id          SERIAl          PRIMARY KEY,
    nome        VARCHAR(255)    NOT NULL,
    email       VARCHAR(255)    UNIQUE
);

ALTER TABLE: Modifica a estrutura de uma tabela existente.

ADD COLUMN:         Adiciona uma nova coluna
MODIFY COLUMN:      Modifica o tipo de dados de uma coluna existente
DRP COLUMN:         Remove uma coluna
ADD CONSTRAINT:     Adiciona uma restrição (ex: chave primária, chave estragengeira)
DROP CONSTRAINT:    Remove uma restrição

Exemplo:

ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20);
ALTER TABLE clientes ALTER COLUMN  nome TYPE VARCHA(100);

DROP TABLE: Remove uma tabela

Exemplo:

DROP TABLE nome_da_tabela;

CREATE DATABASE: Cria um novo banco de dados.

Exemplo:

CREATE DATABASE nome_do_novo_banco_de_dados;

DROP DATABASE: Remove um banco de dados.

Exemplo:

DROP DATABASE nome_do_banco_de_dados;

SELECT: Consulta dados de uma tabela.

Exemplo:

SELECT nome, email FROM clientes WHERE id = 1;
SELECT * FROM clientes; -- Seleciona todas as colunas

INSERT: Insere novos dados em uma tabela.

Exemplo:

INSERT INTO nome_da_tabela (coluna1, coluna2, ...) VALUES (valor1, valor2, ...);

INSERT INTO clientes (nome, email) VALUES ('joão da silva' , 'joão@email.com');

UPDATE: Atualiza dados existentes em uma tabela.

Exemplo:

UPDATE nome_da_tabela SET coluna1 = novo_valor, coluna2 = novo_valor WHERE condição;

UPDATE clientes SET email = 'novo_email@email.com' WHERE id =1;

DELETE: Remove dados de uma tabela.

Exemplo:

DELETE FROM nome_da_tabela WHERE condição;

DELETE FROM cliente WHERE id = 1;

## Comandos de controle de transação (TCL): Usados para gerenciar transações.

BEGIN:      Inicia uma transação
COMMIT:     Salva as alterações feitas durante a transação
ROLLBACK:   Desfaz as alterações feitas durante a transação

## CLÁUSULAS IMPORTANTES:

WHERE:      Filtra os resultados de uma consulta.
ORDER BY    Ordena os resultados de uma consulta.
GROUP BY:   Agrupa os resultados de uma consulta.
JOIN:       Combina dados de duas ou mais tabelas.
LIMIT       Limita o número de resultados retornados.
OFFSET:      ignora um certo número de resultados.

Exemplo:

SELECT com WHERE e ORDER BY:

SELECT nome, email FROM clientes WHERE nome LIKE 'J%' ORDER BY nome ASC;

SELECT com JOIN:

SELECT clientes.nome, pedidos.data_pedido FROM clientes INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;