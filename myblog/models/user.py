from myblog import db

class User(db.Model):
    __tablename__ = "users" #nombre tabla
    id = db.Column(db.Integer, primary_key = True) #Columnas...
    username = db.Column(db.String(50))
    password = db.Column(db.Text) ##Texto porque se encriptará

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'user: {self.username}'