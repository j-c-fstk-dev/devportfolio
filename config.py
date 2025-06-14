import os

# Configurações do Flask
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))  # 5000 é padrão para produção
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"

# Configuração do Banco de Dados
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///portfolio.db")

# CORS
CORS_ORIGINS_STR = os.getenv("CORS_ORIGINS", "*")
CORS_ORIGINS = CORS_ORIGINS_STR.split(",") if CORS_ORIGINS_STR else ["*"]

# Configurações de Email
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True").lower() == "true"
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

# Segurança
SECRET_KEY = os.getenv("SECRET_KEY", "uma-chave-secreta-padrao-para-desenvolvimento")
MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024))

# Rate Limiting (para implementação futura)
RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", 10))
RATE_LIMIT_PER_HOUR = int(os.getenv("RATE_LIMIT_PER_HOUR", 100))
