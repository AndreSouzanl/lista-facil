# 🛒 ListaFácil

### Organize suas compras. Simplifique sua rotina.

O **ListaFácil** é uma aplicação web desenvolvida com Python e Django, criada para facilitar o cadastro e a organização de produtos de uma lista de compras mensal.

O projeto está em desenvolvimento e tem como objetivo oferecer uma experiência simples, intuitiva e responsiva, permitindo que cada usuário gerencie sua própria lista de compras.

---

## ✨ Funcionalidades

### ✅ Já implementadas

- 👤 **Cadastro de usuários:** criação de conta com nome de usuário, e-mail e senha.
- 🔐 **Autenticação:** login e logout utilizando os recursos do Django.
- 🛍️ **Cadastro de produtos:** inclusão de nome, descrição, quantidade e unidade de medida.
- 📋 **Listagem de produtos:** visualização dos produtos cadastrados pelo usuário conectado.
- 🔒 **Separação por usuário:** cada usuário visualiza apenas os próprios produtos.
- 💬 **Mensagens de confirmação:** feedback após operações realizadas.
- 📱 **Interface responsiva:** estilos preparados para diferentes tamanhos de tela.

### 🚧 Próximas funcionalidades

- ✏️ Edição de produtos.
- ✅ Finalização de produtos comprados.
- 🗑️ Remoção lógica de produtos, preservando seu registro.
- 🎨 Melhorias na experiência visual da lista de compras.
- 📊 Recursos adicionais para organização das compras mensais.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Django | Framework web |
| SQLite | Banco de dados durante o desenvolvimento |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Git e GitHub | Controle de versão e hospedagem do código |

---

## 📂 Estrutura do projeto

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
│   └── urls.py
│
├── produtos/
│   ├── migrations/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
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

*Observação: a estrutura acima representa os principais arquivos previstos no projeto até esta etapa.*

---

## 🚀 Como executar o projeto localmente

### 1. Pré-requisitos

- Python instalado.
- Git, caso queira clonar o repositório.
- Visual Studio Code ou outro editor de código.

### 2. Acessar a pasta do projeto

No terminal do VS Code, entre na pasta do projeto:

```powershell
cd P:\programação_curso\lista_facil
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar o Django

Caso ainda não esteja instalado no ambiente virtual:

```powershell
python -m pip install django
```

### 5. Aplicar as migrações

```powershell
python manage.py migrate
```

### 6. Verificar a configuração

```powershell
python manage.py check
```

### 7. Iniciar o servidor de desenvolvimento

```powershell
python manage.py runserver
```

A aplicação estará disponível localmente em:

**http://127.0.0.1:8000/**

### Principais páginas

| Página | Endereço |
|---|---|
| Login | `/login/` |
| Cadastro de usuário | `/usuarios/cadastro/` |
| Lista de compras | `/produtos/` |
| Adicionar produto | `/produtos/novo/` |

---

## 🗄️ Modelo de dados

O modelo `Produto` contempla informações como:

- Nome e descrição.
- Quantidade e unidade de medida.
- Data de cadastro e última atualização.
- Status do produto.
- Usuário responsável pela criação, atualização e remoção.

As unidades disponíveis incluem unidade, quilograma, grama, litro, caixa, metro e pacote.

O sistema também prevê os status `ativo`, `editado`, `removido` e `finalizado`, preparando a aplicação para futuras funcionalidades de gerenciamento.

---

## 🎯 Objetivo do projeto

O ListaFácil é um projeto de aprendizado e desenvolvimento contínuo, utilizado para aprofundar conhecimentos em Python, Django, desenvolvimento web, autenticação, modelagem de dados e criação de interfaces responsivas.

A proposta é evoluir gradualmente a aplicação, implementando funcionalidades reais e aplicando boas práticas de desenvolvimento de software.

---

## 🗺️ Roadmap

- [x] Configuração inicial do Django.
- [x] Criação dos aplicativos `usuarios` e `produtos`.
- [x] Configuração do banco de dados.
- [x] Cadastro e autenticação de usuários.
- [x] Cadastro de produtos.
- [x] Listagem de produtos por usuário.
- [x] Estilização inicial e responsividade.
- [x] Botão de logout.
- [ ] Edição de produtos.
- [ ] Finalização de produtos comprados.
- [ ] Remoção lógica de produtos.
- [ ] Melhorias na organização e na experiência da lista.
- [ ] Preparação para publicação em produção.

---

## 👨‍💻 Desenvolvido por Dev Souza

Projeto desenvolvido com dedicação, aprendizado contínuo e foco na construção de soluções úteis para o dia a dia.

**ListaFácil — suas compras mais organizadas.**