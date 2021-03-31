from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
   
    def __repr__(self):
        return '<Favoritos %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # do not serialize the password, its a security breach
        }