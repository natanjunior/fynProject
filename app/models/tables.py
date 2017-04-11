from app import db

class Usuario(db.Model):
	__tablename__ = "usuarios"
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(40))
	sobre = db.Column(db.Text)

	def __init__(self, nome, sobre):
		self.nome = nome
		self.sobre = sobre

	def __repr__(self):
		return '<Usuario %r>' % self.nome

class Foto(db.Model):
	__tablename__ = "fotos"
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(40))
	usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	usuario = db.relationship('Usuario',
		backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, url, usuario_id):
		self.url = url
		self.usuario_id = usuario_id

	def __repr__(self):
		return '<URL %r>' % self.url