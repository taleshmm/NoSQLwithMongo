# 🗃️ Projeto com MongoDB e Flask 

Este projeto foi criado com o objetivo de explorar o uso de banco de dados **NoSQL (MongoDB)** em conjunto com o microframework **Flask**. Também foram utilizadas bibliotecas como **Cerberus** para validação de dados e **Flask-PyMongo** para integração com o banco.

A estrutura do projeto segue boas práticas de organização de código, e implementa operações básicas de CRUD, além de validações robustas.


## 🧪 Funcionalidades

✅ Integração com MongoDB via Flask-PyMongo
✅ Sistema de delivery com Create, Update e Get
✅ Validação de dados com Cerberus


---

## 🚀 Como executar o projeto

1. **Clonar o repositório**

```bash
git clone https://github.com/taleshmm/NoSQLwithMongo
cd NoSQLwithMongo
```

2. **Criar e ativar um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instalar as dependências**

```bash
pip install -r requirements.txt
```

Sim, **vale muito a pena citar esse passo no README**, especialmente se o projeto depende que o banco `orders` já esteja criado e acessível para funcionar corretamente. Isso ajuda qualquer pessoa (ou até você mesmo no futuro) a configurar o ambiente sem adivinhações.

Você pode adicionar uma seção logo após o passo de criar o `.env`, algo como:

---

4.  **Configurando o MongoDB**

Para que a aplicação funcione corretamente, você precisa de uma instância do MongoDB rodando localmente (ou remotamente).

1. **Crie um banco de dados** com o nome de sua preferência (ex: `myDatabase`).
2. **Crie uma coleção chamada** `ordens` dentro deste banco.
3. **Adicione** o nome do seu banco de dados em:

```connection_handler
self.__database_name = "Nome de sua escolha aqui"
```


> ⚠️ Importante: O nome da coleção precisa ser obrigatoriamente `ordens`. A aplicação espera encontrar essa coleção dentro do banco configurado.


5. **Executar o servidor Flask**

```bash
python run.py
```

---

## 🔐 Segurança

* Validação rigorosa de dados com Cerberus
* Arquitetura organizada para facilitar manutenção e escalabilidade

---

## 📚 Conceitos aprendidos

* Como usar o MongoDB com Flask
* Como validar JSONs com Cerberus
* Como estruturar uma aplicação modular com Flask
* Boas práticas para aplicações com banco de dados NoSQL

