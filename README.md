# Backend para Portfólio Neo - Matrix Developer

Este é um backend Flask completo criado para o portfólio HTML com tema Matrix. O sistema inclui uma API REST para gerenciar mensagens do formulário de contato.

## 🚀 Funcionalidades

- **API REST completa** para formulário de contato
- **Banco de dados SQLite** para armazenar mensagens
- **Validação de campos** obrigatórios
- **CORS habilitado** para comunicação com frontend
- **Interface web** servindo o HTML original
- **Endpoints administrativos** para gerenciar mensagens

## 📋 Pré-requisitos

- Python 3.11+
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone ou baixe o projeto**
```bash
cd neo-portfolio-backend
```

2. **Ative o ambiente virtual**
```bash
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

1. **Inicie o servidor Flask**
```bash
python src/main.py
```

2. **Acesse o site**
- Frontend: http://localhost:5002
- API: http://localhost:5002/api/

## 🔗 Endpoints da API

### POST /api/contact
Envia uma nova mensagem de contato.

**Corpo da requisição:**
```json
{
  "name": "Nome do usuário",
  "email": "email@exemplo.com", 
  "subject": "Assunto da mensagem",
  "message": "Conteúdo da mensagem"
}
```

**Resposta de sucesso (201):**
```json
{
  "success": true,
  "message": "Mensagem enviada com sucesso! Entraremos em contato em breve.",
  "id": 1
}
```

### GET /api/contact
Lista todas as mensagens de contato (para administração).

**Resposta:**
```json
[
  {
    "id": 1,
    "name": "Nome do usuário",
    "email": "email@exemplo.com",
    "subject": "Assunto",
    "message": "Conteúdo da mensagem",
    "created_at": "2025-06-13T19:32:04.758643"
  }
]
```

### GET /api/contact/{id}
Busca uma mensagem específica por ID.

### DELETE /api/contact/{id}
Remove uma mensagem específica por ID.

## 🗄️ Banco de Dados

O sistema utiliza SQLite com a seguinte estrutura:

**Tabela: contacts**
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR(100), NOT NULL)
- `email` (VARCHAR(120), NOT NULL)
- `subject` (VARCHAR(200), NOT NULL)
- `message` (TEXT, NOT NULL)
- `created_at` (DATETIME, DEFAULT NOW)

## 🎨 Frontend

O HTML original foi integrado e está sendo servido pelo Flask. O formulário de contato foi modificado para:

- Enviar dados via JavaScript (fetch API)
- Exibir mensagens de sucesso/erro
- Limpar campos após envio bem-sucedido
- Validar campos obrigatórios

## 🔧 Estrutura do Projeto

```
neo-portfolio-backend/
├── src/
│   ├── main.py              # Arquivo principal do Flask
│   ├── models/
│   │   └── user.py          # Modelos de banco de dados
│   ├── routes/
│   │   ├── contact.py       # Rotas da API de contato
│   │   └── user.py          # Rotas de usuário
│   └── static/
│       └── index.html       # Frontend HTML
├── venv/                    # Ambiente virtual Python
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## 🧪 Testando a API

**Teste via curl:**
```bash
# Enviar mensagem
curl -X POST http://localhost:5002/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Teste",
    "email": "teste@teste.com",
    "subject": "Teste Backend",
    "message": "Testando o backend"
  }'

# Listar mensagens
curl http://localhost:5002/api/contact
```

## 🚀 Deploy em Produção

Para deploy em produção, considere:

1. **Usar um servidor WSGI** como Gunicorn
2. **Configurar banco de dados** PostgreSQL ou MySQL
3. **Adicionar autenticação** para endpoints administrativos
4. **Configurar HTTPS** e certificados SSL
5. **Implementar rate limiting** para prevenir spam

## 📝 Notas Técnicas

- **CORS habilitado** para permitir requisições do frontend
- **Validação robusta** de dados de entrada
- **Tratamento de erros** com mensagens apropriadas
- **Logs detalhados** para debugging
- **Código limpo** e bem documentado

## 🎯 Próximos Passos

- [ ] Adicionar autenticação de administrador
- [ ] Implementar paginação na listagem
- [ ] Adicionar filtros de busca
- [ ] Configurar envio de emails
- [ ] Implementar rate limiting
- [ ] Adicionar testes automatizados

---

**Desenvolvido com Flask e muito ☕**

