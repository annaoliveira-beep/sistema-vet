"""
Arquivo de configuração da aplicação PetCare
Centraliza todas as configurações do projeto
"""

import os

class Config:
    """Configurações padrão"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_muito_segura_2026'
    DATABASE = 'clinica_vet.db'
    DEBUG = False
    TESTING = False
    
    # Configurações de sessão
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 86400  # 24 horas
    
    # Configurações de segurança
    SESSION_COOKIE_SECURE = False  # Mude para True em produção com HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class DevelopmentConfig(Config):
    """Configurações para desenvolvimento"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configurações para produção"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True

class TestingConfig(Config):
    """Configurações para testes"""
    TESTING = True
    DATABASE = ':memory:'

# Seleção de configuração baseada em ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
