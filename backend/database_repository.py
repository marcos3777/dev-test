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

    # TODO: Implementar método para buscar usuário por email
    def get_user_by_email(self, email: str) -> Optional[dict]:
        """
        TODO: O candidato deve implementar este método.

        Busca um usuário pelo email.

        Args:
            email: O email do usuário

        Returns:
            Dicionário com os dados do usuário se encontrado, None caso contrário

        Exemplo de retorno:
        {
            "id": "uuid",
            "email": "user@example.com",
            "password_hash": "hash_da_senha",
            "created_at": "2024-01-01T00:00:00"
        }
        """
        # TODO: Implementar busca de usuário por email
        pass

    # TODO: Implementar método para criar novo usuário
    def create_user(self, email: str, password_hash: str) -> dict:
        """
        TODO: O candidato deve implementar este método.

        Cria um novo usuário no sistema.

        Args:
            email: Email do usuário
            password_hash: Hash da senha do usuário

        Returns:
            Dicionário com os dados do usuário criado

        Requisitos:
        1. Gerar um ID único para o usuário (use uuid.uuid4())
        2. Armazenar o email em lowercase
        3. Adicionar timestamp de criação
        4. Retornar os dados do usuário criado (sem o password_hash)

        Exemplo de retorno:
        {
            "id": "uuid",
            "email": "user@example.com",
            "created_at": "2024-01-01T00:00:00"
        }
        """
        # TODO: Implementar criação de usuário
        pass

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