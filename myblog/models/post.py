from datetime import datetime
from myblog import db

class Post(db.Model):
    __tablename__ = "posts" #nombre tabla
    id = db.Column(db.Integer, primary_key = True) #Columnas...
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(400))
    body = db.Column(db.Text) ##Texto porque se encriptará
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, author, title, body):
        self.author = author
        self.title = title
        self.body = body
        
        #fecha y usuario no se pasa porque se crean automaticamente

    def __repr__(self):
        return f'post: {self.title}'