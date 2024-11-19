from flask import Flask, render_template 
#, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vburieapvbrjere'
conexao ="mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3_g2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Autor, Artigo
db.init_app(app)
migrate = Migrate(app, db)
from modulos.autores.autores import bp_autor
app.register_blueprint(bp_autor, url_prefix='/autores')

from modulos.artigos.artigos import bp_artigo
app.register_blueprint(bp_artigo, url_prefix='/artigos')

@app.route('/')
def index():
    return render_template("ola.html")