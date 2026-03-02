# 🐾 PetCare - Sistema de Clínica Veterinária

Um sistema web moderno e responsivo para gerenciar pacientes em clínicas veterinárias, desenvolvido com **Flask** e **SQLite3**.

## 📋 Funcionalidades

✅ **Autenticação de Usuários**
- Registro de novos usuários com criptografia de senha
- Sistema de login seguro
- Gerenciamento de sessão

✅ **Gerenciamento de Pacientes**
- Cadastro de novos pacientes com informações completas
- Visualização de todos os pacientes cadastrados
- Exclusão de pacientes com confirmação
- Listagem organizada por data de cadastro

✅ **Persistência de Dados**
- Banco de dados SQLite integrado
- Dados salvos automaticamente
- Suporte multi-usuário (cada usuário vê seus próprios pacientes)

✅ **Interface Moderna**
- Design responsivo com Bootstrap 5
- Interface intuitiva e amigável
- Navegação fluida
- Validações em tempo real

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python with Flask
- **Banco de Dados:** SQLite3
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Segurança:** Werkzeug (hash de senhas)

## 📦 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🚀 Instalação e Execução

### 1. Clone ou baixe o projeto
```bash
cd c:\Users\Seu Pc\Documents\Anna\sistema_vet
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python app.py
```

### 5. Acesse no navegador
```
http://localhost:5000
```

## 📖 Como Usar

### Primeiro Acesso
1. Clique em **"Crie uma aqui"** na página de login
2. Escolha um usuário e senha
3. Clique em **"Criar Conta"**

### Cadastrar Paciente
1. Preencha os dados do tutor (responsável)
2. Informe o nome do animal
3. Selecione a espécie
4. Digite a idade em anos
5. Clique em **"Cadastrar Paciente"**

### Deletar Paciente
1. Localize o paciente na lista
2. Clique no ícone de lixeira vermelha
3. Confirme a exclusão

## 📁 Estrutura do Projeto

```
sistema_vet/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências do projeto
├── clinica_vet.db        # Banco de dados SQLite (gerado automaticamente)
├── static/
│   └── style.css         # Estilos personalizados
└── templates/
    ├── index.html        # Página principal
    ├── login.html        # Página de login
    └── registro.html     # Página de registro
```

## 🔐 Segurança

- ✅ Senhas criptografadas com hash bcrypt
- ✅ Proteção CSRF com session tokens
- ✅ Validação de permissões por usuário
- ✅ Isolamento de dados entre usuários

## 🎨 Recursos de Design

- Interface moderna com gradientes
- Tema responsivo que se adapta a qualquer tela
- Ícones Bootstrap para melhor UX
- Animações suaves e transições
- Feedbacks visuais para ações do usuário

## 🐛 Troubleshooting

### Erro de porta em uso
Se a porta 5000 já está em uso:
```bash
python app.py --port 5001
```

### Banco de dados corrompido
Delete o arquivo `clinica_vet.db` e execute a aplicação novamente para recriar:
```bash
del clinica_vet.db
python app.py
```

## 📈 Melhorias Futuras

- [ ] Dashboard com estatísticas
- [ ] Agendamento de consultas
- [ ] Histórico médico dos pacientes
- [ ] Exportação de relatórios (PDF)
- [ ] Sistema de notificações
- [ ] Integração com redes sociais
- [ ] App mobile (React Native)

## 🏆 Projeto de Portfólio

Este projeto demonstra:
- Desenvolvimento web full-stack
- Implementação de banco de dados
- Autenticação e segurança
- Design responsivo
- Boas práticas de código
- Versionamento com Git

## 📝 Licença

Este projeto é de código aberto e livre para uso educacional e comercial.

## 👨‍💼 Autor

Desenvolvido como projeto de portfólio.

---

**Made with ❤️ using Flask**
