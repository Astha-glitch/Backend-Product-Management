# 📦 FastAPI Product CRUD API

A simple and clean **FastAPI + SQLAlchemy** CRUD API for managing products.  
The API allows you to **create, read, update, and delete products**, where the **client supplies the product ID**.

---

## 🚀 Features

- FastAPI backend
- SQLAlchemy ORM
- Postgres (or any DB you configure)(Install Postgres)
- Full CRUD operations
- Client-supplied product ID (no auto-increment)
- Easy testing via **Swagger** or **Postman**
- Clean structure and proper error handling

---

## 📁 Project Structure

```
project/
│── main.py
│── database.py
│── database_models.py
│── schemas.py
│── requirements.txt
└── README.md
```

---

## 🔧 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- PostGresSql (default)
- Uvicorn

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2️⃣ Create and activate virtual environment
**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Start FastAPI server
```bash
uvicorn main:app --reload
```

Your API runs at:

```
http://localhost:8000
```

---

## 📘 API Documentation

FastAPI automatically provides interactive docs:

### Swagger UI:
```
http://localhost:8000/docs
```

### ReDoc:
```
http://localhost:8000/redoc
```

---

# 🗄️ API Endpoints (CRUD)

## ✔️ Create Product (POST)
**URL:** `/product`  
**Client supplies the ID.**

**Request Body (JSON):**
```json
{
  "id": 101,
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": 49999,
  "quantity": 5
}
```

---

## ✔️ Get All Products (GET)
**URL:** `/products`

---

## ✔️ Get Product by ID (GET)
**URL:** `/product/{id}`  
Example:
```
/product/101
```

---

## ✔️ Update Product (PUT)
**URL:** `/product/{id}`  

**Request Body:**
```json
{
  "id": 101,
  "name": "Laptop Pro",
  "description": "Updated description",
  "price": 45999,
  "quantity": 3
}
```

---

## ✔️ Delete Product (DELETE)
**URL:** `/product/{id}`  
Example:
```
/product/101
```

---

# 🧪 Testing With Postman

### Always Set Header:
```
Content-Type: application/json
```

### POST Example:
- Method: POST  
- URL: `http://localhost:8000/product`  
- Body (raw → JSON):
```json
{
  "id": 1,
  "name": "Tablet",
  "description": "Android tablet",
  "price": 14999,
  "quantity": 10
}
```

If the ID already exists, response:
```json
{
  "detail": "Product with id 1 already exists"
}
```

---

# 🛠️ SQLAlchemy Product Model (Example)

```python
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
```

---

# 🧑‍💻 Pydantic Schema (Example)

```python
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
```

---

# 🤝 Contributing

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request  

---

# ⭐ Support

If you found this project useful, please ⭐ star this repository!

