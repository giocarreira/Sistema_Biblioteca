# Sistema de Biblioteca em Python 📚

Este projeto é um sistema de biblioteca interativo desenvolvido em Python, com salvamento de dados em um arquivo JSON local. Ele permite que usuários e administradores realizem operações como cadastro, busca, avaliação e remoção de livros.

## Funcionalidades

**Administrador**:
- Cadastrar livros
- Exibir livros cadastrados
- Remover livros
- Buscar livros por título

**Usuário**:
- Buscar livros
- Adicionar livros à sua biblioteca pessoal
- Avaliar livros
- Visualizar e remover livros da sua biblioteca
- Fazer login

## Regras de uso

- O sistema possui dois tipos de acesso: **Usuário** e **Administrador**.
- Para que o usuário possa adicionar livros à sua biblioteca, **é necessário que o administrador tenha cadastrado livros previamente**.
- Os dados de livros e usuários são armazenados em um arquivo `dados.json`, que é criado automaticamente na primeira execução, no arquivo anexado já está salvo 2 livros e 1 usuário como exemplares.

## Login do Administrador

Para acessar como administrador, utilize:

- **Login**: `admin`
- **Senha**: `1234`

## Execução

Para iniciar o sistema, execute o arquivo `main.py` no terminal:
