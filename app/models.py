from app import db #This line imports the database object from the app package, which is defined in the __init__.py file. This allows the models.py file to use the same database instance that was created in the app factory function.

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')