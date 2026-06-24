Ecommerce API (FastAPI + PostgreSQL)
API backend de e-commerce com **FastAPI**, **PostgreSQL**, **SQLAlchemy** e **Docker**, com autenticação JWT e CRUD completo de produtos.

Projeto focado em boas práticas de backend, organização em camadas e simulação de ambiente real de produção.

-Tecnologias utilizadas

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic (migrations)
- Docker & Docker Compose
- Pydantic
- JWT Authentication
- bcrypt (hash de senha)

---

- Funcionalidades

## Autenticação
- Registro de usuário
- Login com JWT
- Senhas criptografadas com bcrypt
- Proteção de rotas

## Usuários
- Criação de usuário
- Estrutura base para expansão (roles, permissões)

## Produtos
- Criar produto
- Listar produtos
- Buscar produto por ID
- Atualizar produto
- Deletar produto (soft delete opcional)

