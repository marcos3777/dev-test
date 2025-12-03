"""
Repositório simulado de banco de dados.
Armazena os dados em memória (dictionary) para simplificar o teste.
"""

import uuid
from datetime import datetime
from typing import Dict, List, Optional

class DatabaseRepository:
    def __init__(self):
        """
        Inicializa o repositório com um dicionário vazio para armazenar usuários.
        Em produção, isso seria substituído por uma conexão real com banco de dados.
        """
        self.users: Dict[str, dict] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        """Adiciona alguns usuários de exemplo para teste"""
        # Senha: "teste123" (já com hash)
        self.users["test@example.com"] = {
            "id": str(uuid.uuid4()),
            "email": "test@example.com",
            "password_hash": "pbkdf2:sha256:600000$JKxY5pZR$9e3c8c1e0b3f8c5f3e6b8c5f9e7b8c5f3e6b8c5f9e7b8c5f3e6b8c5f9e7b8c5f",
            "created_at": datetime.now().isoformat()
        }

    def email_exists(self, email: str) -> bool:
        """
        Verifica se um email já está cadastrado no sistema.

        Args:
            email: O email a ser verificado

        Returns:
            True se o email existe, False caso contrário
        """
        return email.lower() in self.users

    def get_user_by_email(self, email: str) -> Optional[dict]:
        user = self.users.get(email.lower())
        if not user:
            return None
        return {
            'id': user['id'],
            'email': user['email'],
            'password': user['password_hash'],
            'created_at': user['created_at']
        }

    def create_user(self, email: str, password_hash: str) -> dict:
        user_id = str(uuid.uuid4())
        email_lower = email.lower()
        created_at = datetime.now().isoformat()

        self.users[email_lower] = {
            'id': user_id,
            'email': email_lower,
            'password_hash': password_hash,
            'created_at': created_at
        }

        return {
            'id': user_id,
            'email': email_lower,
            'created_at': created_at
        }

    def get_all_users(self) -> List[dict]:
        """
        Retorna todos os usuários cadastrados (para debug).
        Remove o password_hash antes de retornar.
        """
        users_list = []
        for email, user_data in self.users.items():
            user_copy = user_data.copy()
            user_copy.pop('password_hash', None)
            users_list.append(user_copy)
        return users_list

    def clear_all_users(self):
        """Limpa todos os usuários (útil para testes)"""
        self.users.clear()
        self._initialize_sample_data()