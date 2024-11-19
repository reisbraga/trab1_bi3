from database import db

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    instituicao = db.Column(db.String(50))

    def __init__(self, nome, instituicao):
        self.nome = nome
        self.instituicao = instituicao

    def __repr__(self):
        return "<Autor {}>".format(self.nome)
    
class Artigo(db.Model):
    __tablename__ = 'artigo'
    id_artigo = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    ano_publicacao = db.Column(db.Integer)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id'))

    autor = db.relationship('Autor', foreign_keys=id_autor)

    def __init__(self, titulo, ano_publicacao, id_autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.id_autor = id_autor
    
    def __repr__(self):
        return "<Artigo {}>".format(self.titulo)