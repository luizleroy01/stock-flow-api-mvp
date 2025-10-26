from app import db
from datetime import datetime

class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    company_number = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento 1:N com produtos
    products = db.relationship("Product", back_populates="supplier", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Supplier {self.name}>"
