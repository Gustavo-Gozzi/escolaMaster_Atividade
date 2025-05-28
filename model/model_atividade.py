from database import db

class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.Integer, nullable=False)
    dt_entrega = db.Column(db.Integer, nullable=False)