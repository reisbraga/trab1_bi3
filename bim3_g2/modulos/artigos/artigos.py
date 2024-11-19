from flask import Blueprint, render_template, request, redirect, flash
from models import Artigo, Autor
from database import db

bp_artigo = Blueprint('artigos', __name__, template_folder="templates")

@bp_artigo.route('/')
def index():
    dados = Artigo.query.all()
    return render_template('artigos.html', artigo = dados)

@bp_artigo.route('/add')
def add():
    a = Autor.query.all()
    return render_template('artigos_add.html', autor = a)

@bp_artigo.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    ano_publicacao = request.form.get('ano_publicacao')
    id_autor = request.form.get('id_autor')
    
    if  titulo and ano_publicacao and id_autor:
        bp_artigo = Artigo(titulo, ano_publicacao, id_autor)
        db.session.add(bp_artigo)
        db.session.commit()
        flash('Artigo salvo com sucesso!!!')
        return redirect('/artigos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/artigos/add')

@bp_artigo.route("/remove/<int:id_artigo>")
def remove(id_artigo):
    dados = Artigo.query.get(id_artigo)
    if id_artigo > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Artigo removido com sucesso!')
        return redirect("/artigos")
    else:
        flash("Caminho incorreto!")
        return redirect("/artigos")

@bp_artigo.route("/edita/<int:id_artigo>")
def edita(id_artigo):
    artigo = Artigo.query.get(id_artigo)
    autor = Autor.query.all()
    return render_template("artigos_edita.html", dados=artigo, autor=autor)

@bp_artigo.route("/editasave", methods=['POST'])
def editasave():
    id_artigo = request.form.get('id_artigo')
    titulo = request.form.get('titulo')
    ano_lancamento = request.form.get('ano_lancamento')
    id_autor = request.form.get('id_autor')
    if  id_artigo and titulo and ano_lancamento and id_autor:
        artigos = Artigo.query.get(id_artigo)
        artigos.titulo = titulo
        artigos.ano_lancamento = ano_lancamento
        artigos.id_autor = id_autor

        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/artigos')
    else:
        flash('Dados incompletos.')
        return redirect("/artigos")