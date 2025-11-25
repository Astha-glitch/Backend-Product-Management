from fastapi import FastAPI,Depends,HTTPException,status
from database import SessionLocal,engine
from models import Product
from sqlalchemy.orm import Session
import database_models



app=FastAPI()
database_models.Base.metadata.create_all(engine)

@app.get("/")
def greet():
    return "Welcome to my page"
greet()

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=8, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=7, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=6, name="Table", description="A wooden table", price=199.99, quantity=20),
]
def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()

def init_db():
    db=SessionLocal()
    count=db.query(database_models.Product).count()
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        
        db.commit()
init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product

# ------------------
# Create (POST)
# ------------------
@app.post("/product", status_code=status.HTTP_201_CREATED)
def add_product(product: Product, db: Session = Depends(get_db)):
    # 1. Check if client-supplied id already exists
    existing = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == product.id)
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Product with id {product.id} already exists"
        )

    # 2. Create new product object with same id from request body
    new_product = database_models.Product(**product.model_dump())

    # 3. Save to DB
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # 4. Return response
    return {
        "message": "Product added successfully",
        "product": new_product
    }

# ------------------
# Update (PUT) - full update
# ------------------
@app.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    # copy fields (adjust keys to your model)
    db_product.name = product.name  # type: ignore
    db_product.description = product.description  # type: ignore
    db_product.price = product.price  # type: ignore
    db_product.quantity = product.quantity  # type: ignore

    db.commit()
    db.refresh(db_product)
    return {"message": "Product updated successfully", "product": db_product}

# ------------------
# Delete (DELETE)
# ------------------
@app.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted successfully"}