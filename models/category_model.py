from app import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relacionamento 1:N com produtos
    products = db.relationship("Product", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category {self.name}>"
