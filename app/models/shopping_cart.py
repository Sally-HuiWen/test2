from .db import db, environment, SCHEMA, add_prefix_for_prod

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    purchase_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))

    #one-to-many products=>user=>shopping_cart
    user = db.relationship(
        'User',
        back_populates = 'shopping_cart',
        
        cascade="delete"
    )
