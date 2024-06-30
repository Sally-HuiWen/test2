from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from sqlalchemy import inspect

def table_exists(table_name):
    insp = inspect(db.engine)
    return insp.has_table(table_name, schema=SCHEMA)

# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', first_name='Demo', last_name='User', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', first_name='Marnie', last_name='Grah', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', first_name='Bobbie', last_name='Sox', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production" and table_exists('users'):
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
