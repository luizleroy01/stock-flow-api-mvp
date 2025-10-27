from app import db
from sqlalchemy import text


def update_stock(product_id,qtd):
    query = text("""
        UPDATE products
        SET stock = stock + :qtd, updated_at = NOW()
        WHERE id = :pid
        RETURNING *;
    """)
    result = db.session.execute(query, {"pid": product_id, "qtd": qtd})
    db.session.commit()
    return result

def get_products_by_filter(filter):
    query = text("""
    SELECT * FROM products
    WHERE name ILIKE '%' || :name || '%'
""")

    result = db.session.execute(query, {"name": filter["name"]})
    rows = result.fetchall()

    # Converte todas as linhas para dicionários
    return [dict(row._mapping) for row in rows]