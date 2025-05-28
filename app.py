from flask import Flask
from database import db
from control import control_atividade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atividade.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(control_atividade.routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=8880, debug=True)