import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_mail import Mail
from src.models.user import db
from src.routes.contact import contact_bp
from src.routes.user import user_bp

# Caminho absoluto para o config.py, ajuste conforme sua estrutura
CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.py")

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), "static"))

# Carregar as configurações do config.py
app.config.from_pyfile(CONFIG_PATH)

# Configurar CORS com origens permitidas
CORS(
    app, 
    resources={r"/api/*": {"origins": ["https://j-c-fstk-dev.github.io"]}},
    supports_credentials=True
)

# Inicializar extensões
db.init_app(app)
mail = Mail(app)

# Criação das tabelas ao subir o app (Flask 3+ não tem mais before_first_request)
with app.app_context():
    db.create_all()

# Registrar blueprints
app.register_blueprint(contact_bp, url_prefix="/api")
app.register_blueprint(user_bp, url_prefix="/api")

# Servir arquivos estáticos (frontend)
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404
    full_path = os.path.join(static_folder_path, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, "index.html")
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, "index.html")
        else:
            return "index.html not found", 404

if __name__ == "__main__":
    app.run(
        host=app.config.get("FLASK_HOST", "0.0.0.0"),
        port=app.config.get("FLASK_PORT", 5000),
        debug=app.config.get("FLASK_DEBUG", False)
    )
