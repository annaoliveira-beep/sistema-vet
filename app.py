"""
PetCare - Sistema de Clínica Veterinária
Aplicação web para gerenciar pacientes em clínicas veterinárias
"""

from flask import Flask, render_template, request, redirect, session, flash, url_for
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config, config
from database import db
import os

# Inicializar Flask
app = Flask(__name__)
app.config.from_object(config['development'])

# Inicializar banco de dados
db.init_db()

def login_required(f):
    """Decorator para rotas que requerem login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Por favor, faça login primeiro.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ============= ROTAS DE AUTENTICAÇÃO =============

@app.route("/")
def index():
    """Rota raiz que redireciona para home ou login"""
    if "usuario_id" in session:
        return redirect(url_for("home"))
    return redirect(url_for("login"))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    """Página de registro de novos usuários"""
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "").strip()
        
        # Validações
        if not usuario or not senha:
            flash("Usuário e senha são obrigatórios.", "danger")
            return redirect(url_for("registro"))
        
        if len(usuario) < 3:
            flash("O usuário deve ter pelo menos 3 caracteres.", "danger")
            return redirect(url_for("registro"))
        
        if len(senha) < 6:
            flash("A senha deve ter pelo menos 6 caracteres.", "danger")
            return redirect(url_for("registro"))
        
        # Verificar se usuário já existe
        if db.usuario_existe(usuario):
            flash("Este usuário já existe. Escolha outro.", "danger")
            return redirect(url_for("registro"))
        
        # Criar usuário
        senha_hash = generate_password_hash(senha)
        if db.criar_usuario(usuario, senha_hash):
            flash("Registro realizado com sucesso! Faça login.", "success")
            return redirect(url_for("login"))
        else:
            flash("Erro ao criar usuário. Tente novamente.", "danger")
    
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Página de login"""
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "").strip()
        
        if not usuario or not senha:
            flash("Usuário e senha são obrigatórios.", "danger")
            return redirect(url_for("login"))
        
        # Buscar usuário no banco
        user = db.obter_usuario(usuario)
        
        if user and check_password_hash(user["senha"], senha):
            session["usuario_id"] = user["id"]
            session["usuario"] = user["usuario"]
            session.permanent = True
            flash(f"Bem-vindo, {usuario}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos.", "danger")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    """Logout do usuário"""
    usuario = session.get("usuario", "Usuário")
    session.clear()
    flash(f"Até logo, {usuario}!", "info")
    return redirect(url_for("login"))

# ============= ROTAS DO SISTEMA =============

@app.route("/home")
@login_required
def home():
    """Página principal com lista de pacientes"""
    pacientes = db.obter_pacientes(session["usuario_id"])
    return render_template("index.html", pacientes=pacientes)

@app.route("/cadastrar", methods=["POST"])
@login_required
def cadastrar():
    """Cadastra um novo paciente"""
    tutor = request.form.get("tutor", "").strip()
    animal = request.form.get("animal", "").strip()
    especie = request.form.get("especie", "").strip()
    idade = request.form.get("idade", "").strip()

    # Validações
    if not all([tutor, animal, especie, idade]):
        flash("Todos os campos são obrigatórios.", "danger")
        return redirect(url_for("home"))
    
    try:
        idade = int(idade)
        if idade < 0 or idade > 100:
            raise ValueError("Idade deve estar entre 0 e 100")
    except ValueError:
        flash("Idade deve ser um número válido entre 0 e 100.", "danger")
        return redirect(url_for("home"))
    
    # Criar paciente
    if db.criar_paciente(session["usuario_id"], tutor, animal, especie, idade):
        flash(f"✓ Paciente {animal} cadastrado com sucesso!", "success")
    else:
        flash("Erro ao cadastrar paciente. Tente novamente.", "danger")

    return redirect(url_for("home"))

@app.route("/deletar/<int:paciente_id>", methods=["POST"])
@login_required
def deletar(paciente_id):
    """Deleta um paciente"""
    if db.deletar_paciente(paciente_id, session["usuario_id"]):
        flash("✓ Paciente deletado com sucesso!", "success")
    else:
        flash("✗ Erro: Você não tem permissão para deletar este paciente.", "danger")
    
    return redirect(url_for("home"))

# ============= TRATAMENTO DE ERROS =============

@app.errorhandler(404)
def not_found(error):
    """Página 404"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    """Página 500"""
    return render_template("500.html"), 500

# ============= MAIN =============

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
