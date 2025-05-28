from flask import Blueprint, request, jsonify
from model import model_atividade
from database import db
import requests
from datetime import datetime

routes = Blueprint("routes", __name__)


def validar_data(data_str):
    data_fornecida = datetime.strptime(data_str, "%d-%m-%Y")  
    data_hoje = datetime.today()
    return data_fornecida < data_hoje
    
def validar_turma(idTurma):
    turma = requests.get(f"http://localhost:8000/turmas/{idTurma}")
    return turma.status_code == 200

def validar_professor(idProfessor):
    professor = requests.get(f"http://localhost:8000/turmas/{idProfessor}")
    return professor.status_code == 200


@routes.route("/atividade", methods=["POST"])
def postAtividade():
    dados = request.json
    idProfessor = dados.get("professor_id")
    idTurma = dados.get("turma_id")
    materiaT = dados.get("materia")
    dtEntrega = dados.get("dt_entrega")
    print(dtEntrega)
    print(type(dtEntrega))

    if not validar_professor(idProfessor):
        return jsonify("Professor não encontrado."), 400
    
    if not validar_turma(idTurma):
        return jsonify("Turma não encontrada")
    
    if validar_data(dtEntrega):
        return jsonify(f"A data de entrega precisa ser posterior ao dia de hoje. {datetime.today()}"), 400
    
    atividade = model_atividade.Atividade(
        professor_id=idProfessor,
        turma_id = idTurma,
        materia=materiaT,
        dt_entrega=dtEntrega
    )
    try:
        db.session.add(atividade)
        db.session.commit()
        return jsonify("Atividade criada com sucesso!"), 200
    except:
        return jsonify("Ocorreu um erro! A atividade não foi criada"), 400
    

@routes.route("/atividade", methods=["GET"])
def getAtividades():
    atividades = model_atividade.Atividade.query.all()
    lista = []

    for atividade in atividades:
        lista.append({
            "id": atividade.id,
            "professor_id": atividade.professor_id,
            "turma_id":atividade.turma_id,
            "materia": atividade.materia,
            "data_entrega": atividade.dt_entrega
        })  

    return jsonify(lista), 200


@routes.route("/atividade/<int:idAtividade>", methods=["GET"])
def getAtividadeById(idAtividade):
    atividade = model_atividade.Atividade.query.get(idAtividade)
    try:
        atividades = {
            "id": atividade.id,
            "professor_id": atividade.professor_id,
            "turma_id":atividade.turma_id,
            "materia": atividade.materia,
            "data_entrega": atividade.dt_entrega
        }

        return jsonify(atividades), 200
    except:
        return jsonify("Atividade não encontrada."), 400
    

@routes.route("/atividade/<int:idAtividade>", methods=["DELETE"])
def deleteAtividade(idAtividade):
    try:
        atividade = model_atividade.Atividade.query.get(idAtividade)
        db.session.delete(atividade)
        db.session.commit()
        return jsonify("Atividade deletada com sucesso!"), 200
    
    except:
        return jsonify("Turma não encontrada."), 400
