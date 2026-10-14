# 🛒 ListaFácil

### Organize suas compras. Simplifique sua rotina.

O **ListaFácil** é uma aplicação web desenvolvida com Python e Django, criada para facilitar o cadastro e a organização de produtos de uma lista de compras mensal.

O projeto está em desenvolvimento e tem como objetivo oferecer uma experiência simples, intuitiva e responsiva, permitindo que cada usuário gerencie sua própria lista de compras.

---

## ✨ Funcionalidades

### ✅ Já implementadas

- 👤 **Cadastro de usuários:** criação de conta com nome de usuário, e-mail e senha.
- 🔐 **Autenticação:** login e logout utilizando os recursos do Django.
- 🔑 **Recuperação de senha:** solicitação de recuperação, geração de link temporário e cadastro de uma nova senha, utilizando os recursos nativos de autenticação do Django.
- 🛍️ **Cadastro de produtos:** inclusão de nome, quantidade e unidade de medida.
- 📋 **Listagem de produtos:** visualização dos produtos cadastrados pelo usuário conectado.
- 🔒 **Separação por usuário:** cada usuário visualiza e gerencia apenas os próprios produtos.
- ✏️ **Edição de produtos:** atualização das informações dos produtos cadastrados.
- ✅ **Controle de compras:** marcação de produtos como comprados ou pendentes.
- 🗑️ **Remoção lógica:** produtos removidos deixam de aparecer na lista, mas permanecem registrados no banco de dados.
- ♻️ **Reativação de produtos:** recuperação de produtos removidos anteriormente, preservando o registro original.
- 🚫 **Validação de duplicidade:** prevenção de cadastros repetidos para o mesmo usuário, com mensagens de orientação.
- 📊 **Resumo da lista:** exibição do total de produtos, comprados e pendentes.
- 💬 **Mensagens de feedback:** confirmação das operações realizadas e avisos ao usuário.
- 📱 **Interface responsiva:** estilos preparados para diferentes tamanhos de tela.
- 🔐 **Proteção de páginas:** acesso às funcionalidades da lista restrito a usuários autenticados.

**Observação sobre a recuperação de senha:** o fluxo foi testado no ambiente local, incluindo a geração do link, a redefinição da senha e o login com a nova senha. Atualmente, o conteúdo do e-mail é exibido no terminal. O envio para uma caixa de entrada real será configurado na etapa de publicação.

### 🛠️ Próximas funcionalidades

- 📄 **Paginação:** dividir a lista de produtos em páginas para facilitar a navegação.
- 🔎 **Filtros de visualização:** permitir visualizar todos os produtos, apenas os pendentes ou apenas os comprados.
- 🧪 **Testes automatizados:** testar autenticação, cadastro, recuperação de senha, edição, remoção, reativação e controle de acesso.
- 🎨 **Melhorias visuais:** aprimorar continuamente a experiência e a usabilidade.
- 🚀 **Publicação:** preparar e disponibilizar a aplicação em ambiente de produção, incluindo o envio real de e-mails e a revisão das configurações de segurança.

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
│   │   ├── cadastro.html
│   │   ├── senha_esqueci.html
│   │   ├── senha_enviada.html
│   │   ├── senha_redefinir.html
│   │   ├── senha_redefinida.html
│   │   ├── email_redefinir_senha.txt
│   │   └── assunto_redefinir_senha.txt
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

**Observação:** a estrutura apresenta os principais arquivos do projeto e pode variar conforme sua evolução. O banco `db.sqlite3` é utilizado no ambiente local de desenvolvimento.

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

### 3. Criar e ativar o ambiente virtual

Caso o ambiente virtual ainda não exista, crie-o:

```powershell
python -m venv venv
```

Ative o ambiente no Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

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
| Solicitação de recuperação de senha | `/usuarios/senha/esqueci/` |
| Confirmação da solicitação de recuperação | `/usuarios/senha/enviada/` |
| Redefinição de senha | `/usuarios/senha/redefinir/<uidb64>/<token>/` |
| Confirmação da nova senha | `/usuarios/senha/redefinida/` |
| Lista de compras | `/produtos/` |
| Adicionar produto | `/produtos/novo/` |

---

## 🗃️ Modelo de dados

O modelo `Produto` contempla:

- Nome do produto.
- Quantidade e unidade de medida.
- Descrição mantida no modelo de dados, mas não exibida no formulário atual.
- Data de cadastro e última atualização.
- Status do produto.
- Usuário responsável pela criação, atualização e remoção.

As unidades de medida disponíveis incluem unidade, quilograma, grama, litro, caixa, metro e pacote.

### Status dos produtos

| Status | Descrição |
|---|---|
| `ativo` | Produto pendente na lista. |
| `editado` | Produto que passou por uma atualização. |
| `finalizado` | Produto marcado como comprado. |
| `removido` | Produto retirado da lista por remoção lógica. |

O modelo possui uma restrição de unicidade que evita registros duplicados com o mesmo nome para um mesmo usuário. A reativação recupera um produto removido, preservando seu registro original.

---

## 🎯 Objetivo do projeto

O ListaFácil é um projeto de aprendizado e desenvolvimento contínuo, utilizado para aprofundar conhecimentos em Python, Django, desenvolvimento web, autenticação, modelagem de dados e criação de interfaces responsivas.

A proposta é evoluir gradualmente a aplicação, implementando funcionalidades reais e aplicando boas práticas de desenvolvimento de software, organização de código, segurança e manutenção.

---

## 🗺️ Roadmap

### Funcionalidades concluídas

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
- [x] Recuperação de senha com geração de link temporário.
- [x] Redefinição de senha e teste de login com a nova senha.

### Próximas etapas

- [ ] Implementar a paginação da lista de produtos.
- [ ] Implementar filtros de visualização.
- [ ] Criar testes automatizados.
- [ ] Aprimorar a interface e a usabilidade.
- [ ] Configurar o envio real de e-mails para recuperação de senha.
- [ ] Revisar a segurança e as configurações da aplicação.
- [ ] Criar o `requirements.txt` com as dependências do projeto.
- [ ] Preparar a aplicação para publicação em produção.

---

## 👨‍💻 Desenvolvido por Dev Souza

Projeto desenvolvido com dedicação, aprendizado contínuo e foco na construção de soluções úteis para o dia a dia.

**ListaFácil — suas compras mais organizadas.**