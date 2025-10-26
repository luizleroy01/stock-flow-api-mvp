from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=True)

    manufacture_date = db.Column(db.Date)
    expiration_date = db.Column(db.Date)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamentos
    category = db.relationship("Category", back_populates="products")
    supplier = db.relationship("Supplier", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name} - {self.price}>"
