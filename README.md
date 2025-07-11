# 🔐 FastAPI Auth & Security Microservice

## Features
- JWT authentication
- Secure user registration and login
- Bcrypt password hashing
- Ready to plug in Google OAuth

## Setup

```bash
pip install -r requirements.txt
uvicorn app.. main: app-- reload
```

### Register User
```bash
curl -X POST http://127.0.0.1:8000/register -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "test123"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/token -d "username=test@example.com&password=test123"
```

### Get Current User
```bash
curl -H "Authorization: Bearer <TOKEN>" http://127.0.0.1:8000/users/me
```
