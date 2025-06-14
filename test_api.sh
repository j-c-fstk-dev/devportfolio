#!/bin/bash

# Script de exemplo para testar a API do backend
# Execute este script para testar todas as funcionalidades

echo "🚀 Testando Backend do Portfólio Neo - Matrix Developer"
echo "=================================================="

# URL base da API
BASE_URL="http://localhost:5002/api"

echo ""
echo "📝 1. Enviando mensagem de teste..."
RESPONSE=$(curl -s -X POST $BASE_URL/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@teste.com",
    "subject": "Teste da API",
    "message": "Esta é uma mensagem de teste para verificar se a API está funcionando corretamente."
  }')

echo "Resposta: $RESPONSE"

echo ""
echo "📋 2. Listando todas as mensagens..."
curl -s $BASE_URL/contact | python3 -m json.tool

echo ""
echo "✅ Teste concluído!"
echo ""
echo "💡 Para testar manualmente:"
echo "   - Acesse: http://localhost:5002"
echo "   - Preencha o formulário de contato"
echo "   - Verifique as mensagens em: $BASE_URL/contact"

