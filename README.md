# Desafio de Implementação de Banco de Dados Relacional e NoSQL

Este repositório contém a solução para um desafio que envolve a implementação de um banco de dados relacional utilizando SQLAlchemy (Parte 1) e um banco de dados NoSQL utilizando PyMongo (Parte 2).

## Parte 1: Implementação com SQLAlchemy

Nesta parte do desafio, o objetivo é criar uma aplicação de integração com SQLite com base em um esquema relacional disponibilizado. As classes Cliente e Conta são definidas para representar as tabelas do banco de dados relacional dentro da aplicação. Em seguida, são inseridos dados mínimos para manipulação das informações e executados métodos de recuperação de dados via SQLAlchemy.

Para executar a solução da Parte 1, basta executar o código fornecido no arquivo `parte1.py`. Certifique-se de ter as dependências do SQLAlchemy instaladas.

## Parte 2: Implementando um Banco de Dados NoSQL com PyMongo

Na segunda parte do desafio, o objetivo é implementar um banco de dados NoSQL com MongoDB para fornecer uma visão agregada do modelo relacional. São realizadas operações para conectar ao MongoDB Atlas, criar um banco de dados, definir uma coleção para criar documentos de clientes e inserir documentos com a estrutura mencionada. Além disso, são escritas instruções de recuperação de informações com base nos pares de chave e valor.

Para executar a solução da Parte 2, basta executar o código fornecido no arquivo `parte2.py`. Certifique-se de ter as dependências do PyMongo instaladas e substitua os placeholders `<username>`, `<password>`, `<cluster>` e `<dbname>` pelos detalhes corretos da sua conexão com o MongoDB Atlas.

## Pré-requisitos

- Python 3.x
- SQLAlchemy
- PyMongo
- Conexão com um banco de dados MongoDB Atlas (para a Parte 2)

## Executando o Código

1. Clone este repositório:
````
git clone https://github.com/Nayumt99/desafio-python-dio-sql
````

2. Navegue até o diretório do projeto:

````

cd desafio-python-dio-sql

````

3. Execute o código da Parte 1:
````

python sqlacademy.py
````

4. Execute o código da Parte 2:

````

python pymongo.py
````


