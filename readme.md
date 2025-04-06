# 🌐 Django REST API – Clients, Projects, Users

A full-featured Django REST API with JWT Authentication for managing Clients and Projects. Each project belongs to a client and can be assigned to multiple users. Includes Swagger documentation, browsable API, and admin panel access.

---

## 🛠 Tech Stack

- Python 3.12
- Django 4.x
- Django REST Framework
- Simple JWT for authentication
- SQLite (for development)

---

## ⚙️ Project Setup (Linux & Windows)

### ✅ Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### ✅ Create Virtual Environment

#### 🔵 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔵 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### ✅ Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ Apply Migrations

```bash
python manage.py migrate
```

### ✅ Create Superuser

```bash
python manage.py createsuperuser
```

### ✅ Run the Server

```bash
python manage.py runserver
```

Visit the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 JWT Authentication

### 📝 Register User

```http
POST /auth/register/

Body:
{
  "username": "john",
  "password": "mypassword"
}
```

### 🔑 Get JWT Token

```http
POST /auth/token/

Body:
{
  "username": "john",
  "password": "mypassword"
}
```

### 🔁 Refresh Token

```http
POST /auth/token/refresh/

Body:
{
  "refresh": "<your_refresh_token>"
}
```

Use the access token in headers for all protected routes:

```
Authorization: Bearer <your_access_token>
```

---

## 📁 API Routes

### 🔹 Clients

- **List Clients**
  ```
  GET /clients/
  ```

- **Create Client**
  ```
  POST /clients/
  Headers:
    Authorization: Bearer <access_token>

  Body:
  {
    "client_name": "Company A"
  }
  ```

- **Retrieve Client by ID**
  ```
  GET /clients/<id>/
  ```

- **Update Client**
  ```
  PUT /clients/<id>/
  Body:
  {
    "client_name": "Updated Company"
  }
  ```

- **Delete Client**
  ```
  DELETE /clients/<id>/
  ```

---

### 🔹 Projects

- **Create Project for a Client**
  ```
  POST /clients/<client_id>/projects/
  Headers:
    Authorization: Bearer <access_token>

  Body:
  {
    "name": "Project X",
    "users": [1, 2]
  }
  ```

- **Get Projects Assigned to Logged-in User**
  ```
  GET /projects/
  Headers:
    Authorization: Bearer <access_token>
  ```

---

---

## ✅ Done!


Built using Django REST Framework.
