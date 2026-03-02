# 📚 Documentação Técnica - PetCare

## Arquitetura da Aplicação

```
PetCare (Sistema de Clínica Veterinária)
│
├── Backend (Flask + SQLite3)
│   ├── app.py - Aplicação principal
│   ├── config.py - Configurações
│   ├── database.py - Camada de banco de dados
│   └── requirements.txt - Dependências
│
├── Frontend (HTML5 + CSS3 + Bootstrap)
│   ├── templates/
│   │   ├── login.html - Autenticação
│   │   ├── registro.html - Novo usuário
│   │   ├── index.html - Painel principal
│   │   ├── 404.html - Erro não encontrado
│   │   └── 500.html - Erro servidor
│   │
│   └── static/
│       └── style.css - Estilos customizados
│
└── Banco de Dados (SQLite)
    ├── usuarios - Tabela de usuários
    └── pacientes - Tabela de pacientes
```

## Fluxo de Autenticação

```
Visitante
   ↓
[Página de Login]
   ↓ (credenciais inválidas)
[Flash Message: "Erro"]
   ↓
[Tela de Registro] → [Criar Conta] → [Flash: "Sucesso"]
   ↓
[Login Com Sucesso] → Session com usuario_id
   ↓
[Página Principal (Home)]
```

## Estrutura do Banco de Dados

### Tabela `usuarios`
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Tabela `pacientes`
```sql
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    tutor TEXT NOT NULL,
    animal TEXT NOT NULL,
    especie TEXT NOT NULL,
    idade INTEGER NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
)
```

## Módulos e Funções

### app.py
- `login_required()` - Decorator para proteção de rotas
- `@app.route("/")` - Redireciona para home ou login
- `@app.route("/registro")` - Página de registro
- `@app.route("/login")` - Página de autenticação
- `@app.route("/home")` - Dashboard principal
- `@app.route("/cadastrar")` - Cadastro de paciente
- `@app.route("/deletar/<int:paciente_id>")` - Exclusão de paciente

### database.py
- `Database.get_connection()` - Conexão com SQLite
- `Database.init_db()` - Inicialização das tabelas
- `Database.usuario_existe()` - Verifica usuário duplicado
- `Database.criar_usuario()` - Novo registro
- `Database.obter_usuario()` - Busca usuário
- `Database.criar_paciente()` - Novo paciente
- `Database.obter_pacientes()` - Lista de pacientes
- `Database.deletar_paciente()` - Remove paciente

## Segurança

### Implementações

1. **Hashing de Senhas**
   - Utiliza `werkzeug.security.generate_password_hash()`
   - Algoritmo: pbkdf2:sha256 (padrão)

2. **Proteção de Rotas**
   - Decorator `@login_required` valida sessão
   - Aplicado em todas as rotas protegidas

3. **Isolamento de Dados**
   - Cada usuário vê apenas seus pacientes
   - Validação de permissão em DELETE

4. **Gerenciamento de Sessão**
   - Flask session com SECRET_KEY
   - Atributo `permanent_session = 24h`

5. **CSRF Protection**
   - Implementado via Flask-Session

6. **Validações de Input**
   - `.strip()` para remoção de espaços
   - Validação de tipo de dados
   - Verificação de limites (ex: idade 0-100)

## Performance

### Índices de Banco de Dados
```sql
CREATE INDEX idx_pacientes_usuario ON pacientes(usuario_id)
CREATE INDEX idx_usuarios_usuario ON usuarios(usuario)
```

### Otimizações
- Row factory para retorno eficiente de dados
- Índices em colunas de busca frequente
- Encerramento apropriado de conexões

## Variáveis de Ambiente

```python
SECRET_KEY=sua_chave_secreta_muito_segura
FLASK_ENV=development
FLASK_APP=app.py
DATABASE=clinica_vet.db
```

## Tratamento de Erros

### Implementado
- Erro 404 - Página não encontrada
- Erro 500 - Erro interno do servidor
- Flash messages para feedback ao usuário

## Testes

### Cenários de Teste

1. **Autenticação**
   - Registro com dados válidos
   - Login com credenciais corretas/incorretas
   - Validação de campos obrigatórios

2. **Pacientes**
   - Cadastrá-los com dados completos
   - Listar pacientes por usuário
   - Deletar apenas pacientes do usuário

3. **Segurança**
   - Impedir acesso sem autenticação
   - Isolamento de dados entre usuários
   - Validação de entrada

## Deployment

### Requisitos de Produção
- Python 3.8+
- HTTPS (SESSION_COOKIE_SECURE=True)
- Variáveis de ambiente configuradas
- Servidor WSGI (Gunicorn, uWSGI)

### Exemplo com Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Melhorias Futuras

- [ ] Two-factor authentication (2FA)
- [ ] Backup automático de dados
- [ ] Dashboard com gráficos
- [ ] API REST para integração
- [ ] Sistema de notificações
- [ ] Exportação de relatórios (PDF/CSV)
