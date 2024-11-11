# Sistema de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca desenvolvido como parte da prova de Engenharia de Software I. O sistema visa melhorar a gestão do acervo, empréstimos, devoluções, relatórios e outras atividades essenciais para o funcionamento da biblioteca.

## Integrantes

- **Isaac Davi Mendonça Viana** - 2023000650
- **Laís Padovan** - 2024016313
- **Marcos Eduardo Alves de Souza** - 2023010155
- **Samuel Guedes Nascimento** - 2023012991

## Objetivo

O objetivo deste sistema é fornecer uma solução para a biblioteca, facilitando a gestão do acervo, a consulta de disponibilidade de livros, o controle de empréstimos e devoluções, a geração de relatórios e a aplicação de multas. O sistema foi projetado para ser intuitivo, seguro e eficiente.

## Funcionalidades Principais

1. **Cadastro e Consulta de Livros**: 
   - Inserção, consulta, alteração e remoção de dados dos livros do acervo.
2. **Gerenciamento de Usuários**: 
   - Cadastro e atualização de informações dos usuários da biblioteca.
3. **Empréstimos e Devoluções**:
   - Registro de empréstimos e devoluções de livros, incluindo renovação de prazos e aplicação de multas por atraso.
4. **Geração de Relatórios**:
   - Emissão de relatórios de livros disponíveis e histórico de empréstimos, com opções de exportação.
5. **Segurança e Controle de Acesso**:
   - Autenticação de funcionários com senhas criptografadas e controle de acesso às funcionalidades.

## Estrutura do Projeto

A estrutura do projeto inclui:

- **Questionário para Elicitação de Requisitos**: Entrevistas realizadas com administradores e bibliotecários para entender necessidades e dificuldades.
- **Especificação dos Requisitos**:
  - **Requisitos Funcionais**: Operações como cadastro, consulta e empréstimo de livros.
  - **Requisitos Não Funcionais**: Focam em desempenho, segurança, confiabilidade, usabilidade e portabilidade.
- **Matriz de Rastreabilidade**: Mapeamento dos requisitos para garantir que todos sejam cobertos por casos de uso e funcionalidades.

## Requisitos Funcionais (Exemplos)

1. Manter Cadastro de Livros
2. Manter Cadastro de Usuários
3. Realizar Empréstimo de Livros
4. Consultar Disponibilidade de Livros
5. Gerar Relatório de Livros Disponíveis
6. Gerar Relatório de Empréstimos

## Requisitos Não Funcionais (Exemplos)

1. **Desempenho**: Resposta às consultas em até 2 segundos.
2. **Segurança**: Autenticação por login e senha com criptografia.
3. **Confiabilidade**: Disponibilidade do sistema de 99%.
4. **Usabilidade**: Interfaces intuitivas e acessíveis.
5. **Portabilidade**: Acessível em dispositivos desktop e móveis.

## Protótipos de Telas

1. **Tela Principal**: Interface de boas-vindas com navegação para as funcionalidades.
2. **Relatório Gerado**: Exibição de relatórios detalhados com filtros e opções de exportação.
3. **Consulta de Disponibilidade de Livros**: Tela de pesquisa de livros com filtros por título, autor e categoria.

## Matriz de Rastreabilidade

A matriz de rastreabilidade conecta cada requisito a uma funcionalidade ou caso de uso, garantindo cobertura completa dos requisitos no sistema.

## Estrutura de Arquivos

- `src/`: Contém o código-fonte do projeto.
- `docs/`: Documentação e especificações, incluindo o questionário de requisitos e matriz de rastreabilidade.
- `README.md`: Este arquivo, com informações gerais sobre o projeto.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/sistema-biblioteca.git
   cd sistema-biblioteca
2. Execução do Flask:

   No terminal você executa:
   ```bash
   python app.py
4. Execução da automação do Selenium:

   No terminal você executa:
   ```bash
   python tests/test_crud_selenium.py

## Licença
  Este projeto é apenas para fins educacionais e não está licenciado para uso comercial.
