from .db import db, environment, SCHEMA, add_prefix_for_prod

order_item_association = db.Table(
    "order_items",
    db.Column('order_id', db.Integer, db.ForeignKey(add_prefix_for_prod('orders.id'),ondelete='CASCADE'), primary_key = True),
    db.Column('product_id', db.Integer, db.ForeignKey(add_prefix_for_prod('products.id'), ondelete='CASCADE'), primary_key = True),
    db.Column('quantity', db.Integer)
)
