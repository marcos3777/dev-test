# Desafio Técnico - Sistema de Autenticação

## 📋 Descrição

Você foi contratado para implementar um sistema de autenticação completo com login e cadastro de usuários. O projeto já possui uma estrutura base configurada, mas você precisará completar as funcionalidades principais.

## 🎯 Objetivos

### Frontend (Angular)
1. **Melhorar o design das telas** de login e cadastro (HTML e CSS)
2. **Implementar as chamadas de API** no `ApiService` para:
   - Login de usuário
   - Cadastro de usuário

### Backend (Python/Flask)
1. **Implementar a rota de login** (`/api/login`)
2. **Implementar a rota de cadastro** (`/api/register`)
3. **Implementar os métodos auxiliares** no `DatabaseRepository`:
   - `get_user_by_email()`
   - `create_user()`

## 🏗️ Estrutura do Projeto

```
dev-test/
├── frontend/
│   └── login-app/          # Aplicação Angular
│       ├── src/
│       │   └── app/
│       │       ├── components/
│       │       │   ├── login/
│       │       │   ├── register/
│       │       │   └── dashboard/
│       │       └── services/
│       │           └── api.service.ts  # TODO: Implementar chamadas
│       └── package.json
│
├── backend/               # API Python/Flask
│   ├── app.py            # TODO: Implementar rotas
│   ├── database_repository.py  # TODO: Implementar métodos
│   └── requirements.txt
│
└── README.md
```

## 🚀 Como Executar

### Backend
```bash
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python app.py
```
O servidor estará disponível em `http://localhost:5000`

### Frontend
```bash
cd frontend/login-app

# Instalar dependências
npm install

# Executar aplicação
npm start
```
A aplicação estará disponível em `http://localhost:4200`

## 📝 Tarefas a Implementar

### ✅ Tarefa 1: Design das Telas (Frontend)

**Arquivos para editar:**
- `frontend/login-app/src/app/components/login/login.component.html`
- `frontend/login-app/src/app/components/login/login.component.scss`
- `frontend/login-app/src/app/components/register/register.component.html`
- `frontend/login-app/src/app/components/register/register.component.scss`

**Requisitos:**
- Melhorar a aparência visual das telas
- Adicionar estilos CSS apropriados
- Manter a funcionalidade existente
- Garantir responsividade básica

### ✅ Tarefa 2: Implementar Chamadas de API (Frontend)

**Arquivo para editar:**
- `frontend/login-app/src/app/services/api.service.ts`

**Métodos a implementar:**
1. `login(email: string, password: string)`
   - Fazer POST para `/api/login`
   - Retornar Observable com a resposta

2. `register(email: string, password: string)`
   - Fazer POST para `/api/register`
   - Retornar Observable com a resposta

### ✅ Tarefa 3: Implementar Rota de Login (Backend)

**Arquivo para editar:**
- `backend/app.py`

**Rota:** `POST /api/login`

**Requisitos:**
1. Receber `email` e `password` no body
2. Validar campos obrigatórios
3. Buscar usuário por email
4. Verificar senha com `check_password_hash()`
5. Retornar sucesso com dados do usuário ou erro

**Exemplo de resposta sucesso:**
```json
{
  "success": true,
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  },
  "token": "token_simulado"
}
```

### ✅ Tarefa 4: Implementar Rota de Cadastro (Backend)

**Arquivo para editar:**
- `backend/app.py`

**Rota:** `POST /api/register`

**Requisitos:**
1. Receber `email` e `password` no body
2. Validar campos obrigatórios
3. Validar formato do email (regex básico)
4. Validar senha (mínimo 6 caracteres)
5. Verificar se email já existe
6. Criar hash da senha com `generate_password_hash()`
7. Salvar usuário no repositório
8. Retornar sucesso ou erro

**Exemplo de resposta sucesso:**
```json
{
  "success": true,
  "message": "Usuário cadastrado com sucesso",
  "user": {
    "id": "uuid",
    "email": "user@example.com"
  }
}
```

### ✅ Tarefa 5: Implementar Métodos do Repositório (Backend)

**Arquivo para editar:**
- `backend/database_repository.py`

**Métodos a implementar:**

1. `get_user_by_email(email: str) -> Optional[dict]`
   - Buscar e retornar usuário pelo email
   - Retornar None se não encontrado

2. `create_user(email: str, password_hash: str) -> dict`
   - Gerar UUID único para o usuário
   - Armazenar email em lowercase
   - Adicionar timestamp de criação
   - Salvar no dicionário `self.users`
   - Retornar dados do usuário (sem password_hash)

## 🔍 Exemplos de Implementação

### Exemplo já implementado - Verificar Email

A rota `/api/check-email` e o método `email_exists()` já estão implementados como referência:

```python
# Rota em app.py
@app.route('/api/check-email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email')
    exists = db.email_exists(email)
    return jsonify({'exists': exists}), 200

# Método em database_repository.py
def email_exists(self, email: str) -> bool:
    return email.lower() in self.users
```

Use este exemplo como base para implementar as demais funcionalidades.

## 📊 Critérios de Avaliação

1. **Funcionalidade**: O sistema funciona conforme esperado?
2. **Código Limpo**: O código está organizado e legível?
3. **Validações**: Os dados estão sendo validados corretamente?
4. **Tratamento de Erros**: Os erros estão sendo tratados adequadamente?
5. **Design**: As telas estão visualmente agradáveis?
6. **Segurança**: As senhas estão sendo hasheadas corretamente?

## 💡 Dicas

- Use o método `generate_password_hash()` para criar hash de senhas
- Use o método `check_password_hash()` para verificar senhas
- O CORS já está configurado no backend
- O HttpClient já está configurado no Angular
- Teste primeiro a rota `/api/health` para verificar se o servidor está funcionando
- Use o console do navegador para debug no frontend
- Use `print()` para debug no backend

## ⚠️ Observações Importantes

- **NÃO** é necessário implementar JWT ou autenticação real
- **NÃO** é necessário conectar com banco de dados real
- **NÃO** é necessário implementar logout completo (apenas redirecionamento)
- O "banco de dados" é simulado em memória usando um dicionário Python
- Foque na implementação das funcionalidades solicitadas

## 🎯 Entrega

1. Complete todas as tarefas marcadas com TODO
2. Teste o fluxo completo:
   - Cadastrar novo usuário
   - Fazer login com o usuário cadastrado
   - Verificar redirecionamento para dashboard
3. Garanta que não há erros no console
4. Faça commit das suas alterações

## 🤝 Boa Sorte!

Este desafio simula um cenário real de desenvolvimento onde você precisa completar funcionalidades em um projeto existente. Mostre suas habilidades de:
- Compreensão de código existente
- Implementação seguindo padrões estabelecidos
- Resolução de problemas
- Atenção aos detalhes

Qualquer dúvida, consulte os exemplos já implementados no código!