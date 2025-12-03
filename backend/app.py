from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from database_repository import DatabaseRepository
import secrets

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Inicializar repositório do "banco de dados"
db = DatabaseRepository()

# Rota de exemplo implementada - verificar se email existe
@app.route('/api/check-email', methods=['POST'])
def check_email():
    """
    Verifica se um email já está cadastrado no sistema.
    Esta rota está completamente implementada como exemplo.
    """
    try:
        data = request.get_json()
        email = data.get('email')

        if not email:
            return jsonify({'error': 'Email é obrigatório'}), 400

        exists = db.email_exists(email)
        return jsonify({'exists': exists}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email e senha são obrigatórios'}), 400

        user = db.get_user_by_email(email)
        if not user:
            return jsonify({'error': 'Credenciais inválidas'}), 401

        if not check_password_hash(user['password'], password):
            return jsonify({'error': 'Credenciais inválidas'}), 401


        return jsonify({
            'success': True,
            'user': {
                'id': user['id'],
                'email': user['email']
            },
            'token': secrets.token_hex(32)
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# TODO: Implementar rota de cadastro
@app.route('/api/register', methods=['POST'])
def register():
    """
    TODO: O candidato deve implementar esta rota.

    Requisitos:
    1. Receber email e password no body da requisição
    2. Validar se os campos foram enviados
    3. Validar formato do email
    4. Validar senha (mínimo 6 caracteres)
    5. Verificar se o email já existe usando db.email_exists()
    6. Criar hash da senha usando generate_password_hash()
    7. Salvar usuário usando db.create_user()
    8. Retornar sucesso ou erro apropriado

    Exemplo de resposta de sucesso:
    {
        "success": true,
        "message": "Usuário cadastrado com sucesso",
        "user": {
            "id": "uuid",
            "email": "user@example.com"
        }
    }
    """
    # TODO: Implementar lógica de cadastro
    return jsonify({'error': 'TODO: Implementar rota de cadastro'}), 501

# Rota de teste
@app.route('/api/health', methods=['GET'])
def health_check():
    """Rota para verificar se o servidor está funcionando"""
    return jsonify({'status': 'ok', 'message': 'Servidor funcionando'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)