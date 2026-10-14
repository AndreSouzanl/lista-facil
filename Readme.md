# 🛒 ListaFácil

### Organize suas compras. Simplifique sua rotina.

O **ListaFácil** é uma aplicação web desenvolvida com Python e Django, criada para facilitar o cadastro e a organização de produtos de uma lista de compras mensal.

O projeto está em desenvolvimento e tem como objetivo oferecer uma experiência simples, intuitiva e responsiva, permitindo que cada usuário gerencie sua própria lista de compras.

---

## ✨ Funcionalidades

### ✅ Já implementadas

- 👤 **Cadastro de usuários:** criação de conta com nome de usuário, e-mail e senha.
- 🔐 **Autenticação:** login e logout utilizando os recursos do Django.
- 🛍️ **Cadastro de produtos:** inclusão de nome, quantidade e unidade de medida.
- 📋 **Listagem de produtos:** visualização dos produtos cadastrados pelo usuário conectado.
- 🔒 **Separação por usuário:** cada usuário visualiza e gerencia apenas os próprios produtos.
- ✏️ **Edição de produtos:** atualização das informações dos produtos cadastrados.
- ✅ **Controle de compras:** marcação de produtos como comprados ou pendentes.
- 🗑️ **Remoção lógica:** produtos removidos deixam de aparecer na lista, mas permanecem registrados no banco de dados.
- ♻️ **Reativação de produtos:** recuperação de produtos removidos anteriormente, sem criar registros duplicados.
- 🚫 **Validação de duplicidade:** prevenção de cadastros repetidos para o mesmo usuário, com mensagem de orientação.
- 📊 **Resumo da lista:** exibição do total de produtos, comprados e pendentes.
- 💬 **Mensagens de feedback:** confirmação das operações realizadas e avisos ao usuário.
- 📱 **Interface responsiva:** estilos preparados para diferentes tamanhos de tela.
- 🔐 **Proteção de páginas:** acesso às funcionalidades da lista restrito a usuários autenticados.

### 🚧 Próximas funcionalidades

- 📄 Paginação da lista de produtos.
- 🔎 Filtros para visualizar produtos pendentes, comprados e todos os produtos.
- 🎨 Melhorias contínuas na experiência visual e na usabilidade.
- 🧪 Ampliação dos testes automatizados.
- 🚀 Preparação e publicação da aplicação em ambiente de produção.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Django | Framework web |
| SQLite | Banco de dados durante o desenvolvimento |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |

---

## 📁 Estrutura do projeto

```text
lista_facil/
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── usuarios/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── produtos/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── registration/
│   │   └── login.html
│   ├── usuarios/
│   │   └── cadastro.html
│   └── produtos/
│       ├── lista.html
│       └── formulario.html
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── db.sqlite3
└── README.md
```

*Observação: a estrutura apresenta os principais arquivos do projeto e pode variar conforme a evolução da aplicação. O banco `db.sqlite3` é utilizado no ambiente local de desenvolvimento.*

---

## 🚀 Como executar o projeto localmente

### 1. Pré-requisitos

- Python instalado.
- Visual Studio Code ou outro editor de código.
- Git, caso deseje clonar o repositório.

### 2. Acessar a pasta do projeto

No terminal do VS Code, execute:

```powershell
cd P:\programação_curso\lista_facil
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Caso o ambiente virtual ainda não exista, crie-o com:

```powershell
python -m venv venv
```

Em seguida, ative-o.

### 4. Instalar o Django

```powershell
python -m pip install django
```

### 5. Aplicar as migrações

```powershell
python manage.py migrate
```

### 6. Verificar a configuração do projeto

```powershell
python manage.py check
```

### 7. Iniciar o servidor de desenvolvimento

```powershell
python manage.py runserver
```

A aplicação estará disponível localmente em:

**http://127.0.0.1:8000/**

> O servidor de desenvolvimento do Django é destinado a testes locais, não à publicação em produção.

---

## 🔗 Principais páginas

| Página | Endereço |
|---|---|
| Login | `/login/` |
| Cadastro de usuário | `/usuarios/cadastro/` |
| Lista de compras | `/produtos/` |
| Adicionar produto | `/produtos/novo/` |

---

## 🗃️ Modelo de dados

O modelo `Produto` contempla:

- Nome do produto.
- Quantidade e unidade de medida.
- Descrição mantida no modelo de dados, embora não seja mais exibida no formulário atual.
- Data de cadastro e última atualização.
- Status do produto.
- Usuário responsável pela criação, atualização e remoção.

As unidades de medida disponíveis incluem unidade, quilograma, grama, litro, caixa, metro e pacote.

Os status utilizados são:

| Status | Descrição |
|---|---|
| `ativo` | Produto pendente na lista. |
| `editado` | Produto que passou por uma atualização. |
| `finalizado` | Produto marcado como comprado. |
| `removido` | Produto retirado da lista por remoção lógica. |

O modelo também possui uma restrição de unicidade para evitar que o mesmo usuário cadastre mais de um registro com o mesmo nome. A reativação permite recuperar um produto removido, preservando seu registro original.

---

## 🎯 Objetivo do projeto

O ListaFácil é um projeto de aprendizado e desenvolvimento contínuo, utilizado para aprofundar conhecimentos em Python, Django, desenvolvimento web, autenticação, modelagem de dados e criação de interfaces responsivas.

A proposta é evoluir gradualmente a aplicação, implementando funcionalidades reais e aplicando boas práticas de desenvolvimento de software, organização de código e segurança.

---

## 🗺️ Roadmap

- [x] Configuração inicial do Django.
- [x] Criação dos aplicativos `usuarios` e `produtos`.
- [x] Configuração do banco de dados SQLite.
- [x] Cadastro e autenticação de usuários.
- [x] Cadastro de produtos.
- [x] Listagem de produtos por usuário.
- [x] Estilização inicial e responsividade.
- [x] Botão de logout.
- [x] Edição de produtos.
- [x] Finalização de produtos comprados.
- [x] Remoção lógica de produtos.
- [x] Reativação de produtos removidos.
- [x] Validação de produtos duplicados.
- [x] Resumo de produtos, comprados e pendentes.
- [ ] Implementação da paginação.
- [ ] Implementação de filtros de visualização.
- [ ] Ampliação dos testes automatizados.
- [ ] Preparação para publicação em produção.

---

## 👨‍💻 Desenvolvido por Dev Souza

Projeto desenvolvido com dedicação, aprendizado contínuo e foco na construção de soluções úteis para o dia a dia.

**ListaFácil — suas compras mais organizadas.**
