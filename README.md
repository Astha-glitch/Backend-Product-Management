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
-React Frontend

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
frontend/
│
├── public/
│   └── index.html
│
├── src/
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   ├── index.css
│   ├── TaglineSection.js
│   └── TaglineSection.css
│
├── package.json
└── README.md (optional)
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
# 🎨 Frontend (React) – Product Management UI

This is the **frontend UI** for the Product Management application.  
It communicates with the FastAPI backend running at:

```
http://localhost:8000
```

The frontend is built using **React**, **Axios**, and standard CSS (no Tailwind).

---

## 🚀 Features

- View all products  
- Get product by ID  
- Add new products  
- Update existing products  
- Delete products  
- Clean UI  
- Axios-based API communication  
- Fully connected to backend via `proxy` in package.json

---

## 📁 Project Structure

```
frontend/
│
├── public/
│   └── index.html
│
├── src/
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   ├── index.css
│   ├── TaglineSection.js
│   └── TaglineSection.css
│
├── package.json
└── README.md (optional)
```

### 🔍 File Breakdown

#### **public/index.html**
Main HTML template where the React app mounts on the `<div id="root"></div>` element.

---

#### **src/index.js**
Entry point of the React application.  
Renders `<App />` into the root element.

---

#### **src/index.css**
Global styles applied across the application.

---

#### **src/App.js**
Main component that:
- Contains the UI structure
- Calls backend APIs using Axios
- Renders product list / forms

---

#### **src/App.css**
Styles specific to components in `App.js`.

---

#### **src/TaglineSection.js**
A standalone React component that renders a tagline or header section.

---

#### **src/TaglineSection.css**
Styles only for the `TaglineSection` component.

---

# 📦 Install Dependencies

Make sure you're in the `frontend` folder:

```bash
cd frontend
npm install
```

This installs:
- react
- react-dom
- axios
- react-scripts

---

# ▶️ Run the Frontend

```bash
npm start
```

The app will open at:

```
http://localhost:3000
```

Proxy is configured in `package.json`, so API calls automatically forward to:

```
http://localhost:8000
```

---

# 🔌 Backend Connection

The `package.json` includes:

```json
"proxy": "http://localhost:8000"
```

This allows Axios requests like:

```js
axios.get("/products");
```

without writing the full backend URL.

---

# 🤝 Requirements

- Node.js v16+  
- npm v8+  
- Backend running at `localhost:8000`

---

# ⭐ Notes

- `node_modules/` is intentionally ignored (not pushed to GitHub).
- All API calls use Axios.
- UI is simple and minimal for easy understanding.

---

# 🧩 Useful Scripts

```bash
npm start       # Start dev server
npm run build   # Create production build
npm test        # Run tests (if added)
```

---

# 🎉 Conclusion

This frontend works seamlessly with your FastAPI backend to provide a clean and fully functional Product Management interface.



# 🤝 Contributing

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Open a pull request  

---

# ⭐ Support

If you found this project useful, please ⭐ star this repository!

