"""
Módulo de gerenciamento de banco de dados
Centraliza todas as operações com SQLite
"""

import sqlite3
from config import Config

class Database:
    """Classe para gerenciar conexões e operações com o banco de dados"""
    
    def __init__(self, database_name=Config.DATABASE):
        self.database_name = database_name
    
    def get_connection(self):
        """Retorna uma conexão com o banco de dados"""
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def close_connection(self, conn):
        """Fecha a conexão com o banco de dados"""
        if conn:
            conn.close()
    
    def init_db(self):
        """Inicializa o banco de dados com as tabelas necessárias"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Tabela de usuários
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL,
                    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Tabela de pacientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    tutor TEXT NOT NULL,
                    animal TEXT NOT NULL,
                    especie TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
                )
            """)
            
            # Criar índices para melhor performance
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_pacientes_usuario 
                ON pacientes(usuario_id)
            """)
            
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_usuarios_usuario 
                ON usuarios(usuario)
            """)
            
            conn.commit()
            print("✓ Banco de dados inicializado com sucesso!")
            
        except sqlite3.Error as e:
            print(f"✗ Erro ao inicializar banco de dados: {e}")
            conn.rollback()
        finally:
            self.close_connection(conn)
    
    def usuario_existe(self, usuario):
        """Verifica se um usuário já existe"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (usuario,))
            resultado = cursor.fetchone()
            return resultado is not None
        finally:
            self.close_connection(conn)
    
    def criar_usuario(self, usuario, senha_hash):
        """Cria um novo usuário no banco de dados"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
                (usuario, senha_hash)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            self.close_connection(conn)
    
    def obter_usuario(self, usuario):
        """Obtém os dados de um usuário"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
            return cursor.fetchone()
        finally:
            self.close_connection(conn)
    
    def criar_paciente(self, usuario_id, tutor, animal, especie, idade):
        """Cria um novo paciente"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                """INSERT INTO pacientes (usuario_id, tutor, animal, especie, idade) 
                   VALUES (?, ?, ?, ?, ?)""",
                (usuario_id, tutor, animal, especie, idade)
            )
            conn.commit()
            return True
        except sqlite3.Error:
            return False
        finally:
            self.close_connection(conn)
    
    def obter_pacientes(self, usuario_id):
        """Obtém todos os pacientes de um usuário"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "SELECT * FROM pacientes WHERE usuario_id = ? ORDER BY data_cadastro DESC",
                (usuario_id,)
            )
            return cursor.fetchall()
        finally:
            self.close_connection(conn)
    
    def deletar_paciente(self, paciente_id, usuario_id):
        """Deleta um paciente verificando propriedade"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Verifica se o paciente pertence ao usuário
            cursor.execute(
                "SELECT usuario_id FROM pacientes WHERE id = ?",
                (paciente_id,)
            )
            paciente = cursor.fetchone()
            
            if paciente and paciente['usuario_id'] == usuario_id:
                cursor.execute("DELETE FROM pacientes WHERE id = ?", (paciente_id,))
                conn.commit()
                return True
            return False
        finally:
            self.close_connection(conn)

# Instância global do banco de dados
db = Database()
