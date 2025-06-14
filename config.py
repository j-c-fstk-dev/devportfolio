# Configurações do Backend Neo Portfolio

# Configurações do Flask
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5002
FLASK_DEBUG = True

# Configurações do Banco de Dados
DATABASE_URL = 'sqlite:///portfolio.db'

# Configurações de CORS
CORS_ORIGINS = ['*']  # Em produção, especifique domínios específicos

# Configurações de Email (para implementação futura)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'seu-email@gmail.com'
EMAIL_PASSWORD = 'sua-senha-de-app'

# Configurações de Segurança
SECRET_KEY = 'sua-chave-secreta-aqui'  # Mude em produção
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Rate Limiting (para implementação futura)
RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_HOUR = 100

