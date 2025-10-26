from app import db

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relacionamento 1:N com usuários
    users = db.relationship("User", back_populates="role", cascade="all, delete")

    def __repr__(self):
        return f"<Role {self.name}>"
