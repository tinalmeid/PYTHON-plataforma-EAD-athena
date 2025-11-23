# 📊 PyAcademy: Escola EAD em Python Utilizando Django

![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-plataforma-EAD-athena&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-plataforma-EAD-athena&metric=coverage)
![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_PYTHON-plataforma-EAD-athena&metric=duplicated_lines_density)
![Build Status](https://github.com/tinalmeid/PYTHON-plataforma-EAD-athena/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

### Desenvolvimento

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testes-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Django](https://img.shields.io/badge/Framework-Django-092E20?style=flat&logo=django&logoColor=white)
![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white")
![Github Copilot](https://img.shields.io/badge/AI-Copilot-000000?style=flat&logo=githubcopilot&logoColor=white)

### Gestão & DevOps

![Jira](https://img.shields.io/badge/Gestão-Jira-0052CC?style=flat&logo=jira&logoColor=white)
![Azure](https://img.shields.io/badge/DevOps-Azure-0078D7?style=flat&logo=azuredevops&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![SonarCloud](https://img.shields.io/badge/Quality-SonarCloud-F3702A?style=flat&logo=sonarcloud&logoColor=white)
![Clean Code](https://img.shields.io/badge/Prática-Clean_Code-green?style=flat&logo=geocaching&logoColor=white)
![Code Style](https://img.shields.io/badge/Code_Style-PEP8-brightgreen?style=flat)

### Produtividade & Aprendizado

![WakaTime](https://img.shields.io/badge/Produtividade-Wakatime-000000?style=flat&logo=wakatime&logoColor=white)
![Udemy](https://img.shields.io/badge/Plataforma-Udemy-EC5252?style=flat&logo=udemy&logoColor=white)

## 🎯 Sobre o Projeto

Este repositório hospeda o desenvolvimento da **Plataforma EAD Athena** (Simple MOOC), um sistema completo de Gestão de Aprendizagem (LMS - Learning Management System).

O projeto consiste na **modernização arquitetural** de um sistema legado, atualizando a stack para **Django 5.1+** e **Python 3.12+**. O foco vai além das funcionalidades básicas: aplicamos Engenharia de Software robusta, incluindo Custom User Models, arquitetura modular de Apps, testes automatizados (Pytest-Django) e pipelines de CI/CD para garantir manutenibilidade e segurança.

## 📚 Curso de Referência

Udemy: [Python na Web com Django](https://www.udemy.com/course/draft/799014/learn/lecture/4791622#overview)

## 🚀 Como Rodar (Quick Start)

### Pre-requisitos

- Python 3.12 ou superior
- Git

### Instalação

1. 📥**Clone o repositório:**

   ```bash
   git clone [https://github.com/tinalmeid/PYTHON-plataforma-EAD-athena.git](https://github.com/tinalmeid/PYTHON-plataforma-EAD-athena.git)

   cd PYTHON-plataforma-EAD-athena
   ```

2. 🐍**Crie o ambiente virtual:**

   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. 📦**Instale as dependências:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. 🗄️**Configure o Banco de Dados:**

   ```
   # Cria as tabelas iniciais (incluindo o usuário customizado)
   python manage.py migrate
   ```

5. ▶️**Rode o Servidor Local:**

   ```bash
   python manage.py runserver
   # Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   ```

6. 🔬**Rode os Testes:**

   ```bash
   pytest
   ```

## 🧪 Padrões de Qualidade (QA Engineering)

Para garantir a excelência do código, este projeto utiliza um Quality Gate rigoroso:

1. Linting (Pylint): O código deve seguir a PEP8.

2. Testes (Pytest): Cobertura mínima exigida pelo SonarCloud.

3. Clean Code: Funções pequenas, nomes descritivos e princípios SOLID.

4. Code Review: Nenhum código entra na main sem passar pela pipeline de CI.

## 📝 Development Guidelines

Para manter a qualidade e a rastreabilidade do projeto, seguimos estritamente:

1.  **🌿 Branching Strategy:**

    - Toda branch deve começar com a chave do Jira: `ENG-XXX-nome-da-tarefa`.
    - Ex: `ENG-577-setup-ambiente`.

2.  **💾 Padrão de Commit (Conventional Commits):**

    - Formato: `ENG-XXX tipo: Descrição breve`.
    - Tipos permitidos:
      - `feat`: Nova funcionalidade.
      - `fix`: Correção de bug.
      - `docs`: Documentação.
      - `test`: Testes.
      - `refactor`: Melhoria de código sem alterar funcionalidade.
      - `chore`: Configurações e manutenção.
    - Ex: `ENG-586 chore: Configura pipeline inicial`.

3.  **🧪 Testes & TDD:**

    - Toda nova funcionalidade em `src/` deve ter um teste correspondente em `tests/`.
    - Rode `pytest` localmente antes de subir o código.

4.  **🛡️ Quality Gate:**

    - Para aceite de Pull Requests será necessário aprovação do checklist de QA (Sonar + W3C).

    - Código sem Docstrings (documentação de função) será reprovado no Code Review.
    - Mantenha o **SonarCloud** feliz: Zero "Bugs", Zero "Vulnerabilities" e Cobertura aceitável.

5.  **🧹 Clean Code:**
    - Variáveis em inglês e descritivas (nada de `x`, `y`, `aux`).
    - Respeite o **PEP8** (o `pylint` vai reclamar se não fizer!).

## 🏗️ Estrutura do Projeto

```
PYTHON-plataforma-EAD-athena/
├── .github/
│   └── workflows/          # 🤖 Pipelines de CI/CD
├── simplemooc/             # ⚙️ Configurações Globais (Settings, URLs)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # 🏠 App: Página Inicial e Institucional
│   ├── migrations/
│   ├── templates/          # HTMLs específicos do Core
│   ├── tests/
│   └── views.py
├── accounts/               # 👤 App: Gestão de Usuários e Autenticação
│   ├── migrations/
│   ├── models.py           # Custom User Model (AbstractBaseUser)
│   └── tests/
├── requirements.txt        # 📦 Dependências do Projeto
├── sonar-project.properties # 📡 Configuração do SonarCloud
├── manage.py               # 🛠️ CLI de Gerenciamento Django
├── .gitignore
└── README.md
```

## 🗺️ Roadmap & Entregas (Jira)

Monitoramento de tarefas de desenvolvimento com base no fluxo de trabalho de Engenharia.

| ID Jira     | Módulo / Tarefa                               | Branch                      | Status          |
| :---------- | :-------------------------------------------- | :-------------------------- | :-------------- |
| **ENG-591** | 🏗️ Setup: Ambiente, Django 5.x e Custom User  | `ENG-591-setup-core`        | 🔄 Em Andamento |
| **ENG-592** | 🎨 Frontend: Integração de Templates e Assets | `ENG-592-frontend-base`     | 📝 A Fazer      |
| **ENG-593** | 📚 Backend: App Courses e Models              | `ENG-593-courses-models`    | 📝 A Fazer      |
| **ENG-594** | 🖼️ Frontend: Listagem e Detalhes do Curso     | `ENG-594-courses-views`     | 📝 A Fazer      |
| **ENG-595** | 📧 Feature: Formulário de Contato             | `ENG-595-contact-form`      | 📝 A Fazer      |
| **ENG-596** | 🔐 Auth: Login, Logout e Cadastro             | `ENG-596-auth-system`       | 📝 A Fazer      |
| **ENG-597** | 👤 User: Dashboard e Edição de Perfil         | `ENG-597-user-dashboard`    | 📝 A Fazer      |
| **ENG-598** | 🔑 Security: Reset de Senha                   | `ENG-598-password-reset`    | 📝 A Fazer      |
| **ENG-599** | 🎟️ Core: Motor de Inscrições                  | `ENG-599-enrollment-engine` | 📝 A Fazer      |
| **ENG-600** | 🎓 UX: Dashboard do Aluno e Decorators        | `ENG-600-student-area`      | 📝 A Fazer      |
| **ENG-601** | 📢 Feature: Mural de Avisos e E-mails         | `ENG-601-announcements`     | 📝 A Fazer      |
| **ENG-602** | 📺 Content: Aulas e Materiais                 | `ENG-602-lessons-materials` | 📝 A Fazer      |
| **ENG-603** | 💬 Forum: Tópicos e Respostas                 | `ENG-603-forum-structure`   | 📝 A Fazer      |
| **ENG-604** | ✅ Feature: Resposta Correta e Ajax           | `ENG-604-forum-ajax`        | 📝 A Fazer      |
| **ENG-605** | 🧪 QA: Testes Automatizados                   | `ENG-605-tests-coverage`    | 📝 A Fazer      |
| **ENG-606** | 🚀 DevOps: Preparação para Deploy             | `ENG-606-production-ready`  | 📝 A Fazer      |

> **Legenda:** ✅ Concluído | 🔄 Em Andamento | 📝 A Fazer

## 📄 Licença

Este projeto faz parte de um curso de aprendizagem. Sinta-se à vontade para utilizá-lo para fins educacionais.

👩🏽‍💻 Desenvolvido por **Cristina de Almeida** como parte do plano de desenvolvimento técnico.
