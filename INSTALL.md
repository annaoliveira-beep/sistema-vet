# 🚀 Guia de Instalação - PetCare

## Pré-requisitos

- **Python** 3.8 ou superior
- **pip** (gerenciador de pacotes Python)
- **Git** (opcional, para clonar o repositório)

## Verificando Instalações

### Verificar Python
```bash
python --version
```

Esperado: `Python 3.8.x` ou superior

### Verificar pip
```bash
pip --version
```

Esperado: `pip x.x.x from ...`

## Passo a Passo

### 1️⃣ Clonar ou Baixar o Projeto

#### Opção A: Com Git
```bash
git clone <seu-repositorio-url>
cd sistema_vet
```

#### Opção B: Download Manual
- Baixe os arquivos do projeto
- Extraia em uma pasta de sua escolha
- Abra a pasta no terminal

### 2️⃣ Crie um Ambiente Virtual (Recomendado)

O ambiente virtual isolará as dependências do projeto.

#### Windows (PowerShell/CMD)
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

Se bem-sucedido, você verá `(venv)` no início da linha do terminal.

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

Isso instalará:
- Flask 3.0.0
- Werkzeug 3.0.1

### 4️⃣ Execute a Aplicação

```bash
python app.py
```

Você verá uma mensagem similar a:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 5️⃣ Acesse no Navegador

Abra seu navegador e acesse:
```
http://localhost:5000
```

## Resolução de Problemas

### Erro: "python: comando não encontrado"
- **Solução**: Python não está na PATH. Reinstale Python e marque a opção "Add Python to PATH"

### Erro: "ModuleNotFoundError: No module named 'flask'"
- **Solução**: Instale as dependências
```bash
pip install -r requirements.txt
```

### Erro: "Port 5000 already in use"
- **Solução**: Alternar de porta
```bash
python app.py --port 5001
```

### O banco de dados está corrompido
- **Solução**: Delete e recrie
```bash
del clinica_vet.db
python app.py
```

### Erro: "ModuleNotFoundError: No module named 'config'"
- **Solução**: Certifique-se de estar no diretório correto com `sistema_vet`
```bash
cd sistema_vet
python app.py
```

## Desenvolvimento

### Desativar Ambiente Virtual

Quando terminar:
```bash
deactivate
```

### Executar em Produção

Para produção, modifique o ambiente:
```bash
python app.py --mode production
```

Ou defina a variável de ambiente:
```bash
set FLASK_ENV=production
python app.py
```

## Estrutura de Diretórios Esperada

```
sistema_vet/
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── README.md
├── TECHNICAL.md
├── INSTALL.md
├── .gitignore
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── login.html
    ├── registro.html
    ├── 404.html
    └── 500.html
```

## Criando um Usuário Teste

1. Acesse `http://localhost:5000`
2. Clique em "Crie uma aqui"
3. Preencha os dados:
   - **Usuário**: teste
   - **Senha**: 123456
4. Clique em "Criar Conta"
5. Faça login com essas credenciais

## Próximos Passos

✅ Sistema instalado e funcionando!

Agora você pode:
- Adicionar pacientes
- Gerenciar dados
- Customizar o design
- Fazer deploy em produção

## Suporte

Para problemas ou dúvidas, consulte:
- [Documentação Flask](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- Arquivo `TECHNICAL.md` para detalhes técnicos

---

**Desenvolvido com ❤️ usando Flask**
