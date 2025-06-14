from flask import Blueprint, jsonify, request
from src.models.user import db
from datetime import datetime

contact_bp = Blueprint('contact', __name__)

class Contact(db.Model):
    """Modelo para armazenar mensagens do formulário de contato"""
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<Contact {self.name} - {self.subject}>'

@contact_bp.route('/contact', methods=['POST'])
def submit_contact():
    """Endpoint para receber mensagens do formulário de contato"""
    try:
        data = request.json
        
        # Validação dos campos obrigatórios
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Campo {field} é obrigatório'}), 400
        
        # Criar nova mensagem de contato
        contact = Contact(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message'],
            created_at=datetime.utcnow()
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Mensagem enviada com sucesso! Entraremos em contato em breve.',
            'id': contact.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500

@contact_bp.route('/contact', methods=['GET'])
def get_contacts():
    """Endpoint para listar todas as mensagens de contato (admin)"""
    try:
        contacts = Contact.query.order_by(Contact.created_at.desc()).all()
        return jsonify([contact.to_dict() for contact in contacts])
    except Exception as e:
        return jsonify({'error': 'Erro ao buscar mensagens'}), 500

@contact_bp.route('/contact/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """Endpoint para buscar uma mensagem específica"""
    try:
        contact = Contact.query.get_or_404(contact_id)
        return jsonify(contact.to_dict())
    except Exception as e:
        return jsonify({'error': 'Mensagem não encontrada'}), 404

@contact_bp.route('/contact/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """Endpoint para deletar uma mensagem"""
    try:
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Mensagem deletada com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro ao deletar mensagem'}), 500

