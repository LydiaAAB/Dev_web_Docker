from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    rna_id = db.Column(db.String(30), nullable=True) 
    rna_id_ex = db.Column(db.String(30), nullable=True)
    gestion = db.Column(db.String(20), nullable=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/assos')
def assos():
<<<<<<< HEAD
    datas = Data.query.limit(20).all()
=======
    datas = Data.query.limit(30).all()
>>>>>>> origin/main
    return render_template('assos.html', datas=datas)

@app.route('/delete/<int:data_id>')
def delete(data_id):
    data = Data.query.get(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('assos'))

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
<<<<<<< HEAD
        rna_id = request.form['rna_id']
        rna_id_ex = request.form['rna_id_ex']
        gestion = request.form['gestion']
        new_data = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('assos'))
    return render_template('ajouter.html')

@app.route('/modifier/<int:data_id>', methods=['GET', 'POST'])
def modifier(data_id):
    data = Data.query.get(data_id)

    if request.method == 'POST':
        data.rna_id = request.form['rna_id']
        data.rna_id_ex = request.form['rna_id_ex']
        data.gestion = request.form['gestion']
        db.session.commit()
        return redirect(url_for('assos'))
    return render_template('modifier.html', data=data)

=======
        # Récupérer les données du formulaire
        rna_id = request.form['rna_id']
        rna_id_ex = request.form['rna_id_ex']
        gestion = request.form['gestion']

        # Créer une nouvelle instance de la classe Data avec les données du formulaire
        new_data = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)

        # Ajouter la nouvelle instance à la base de données
        db.session.add(new_data)
        db.session.commit()

        # Rediriger l'utilisateur vers la page assos
        return redirect(url_for('assos'))

    # Si la méthode est GET, afficher la page de formulaire
    return render_template('ajouter.html')

>>>>>>> origin/main

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run()
>>>>>>> origin/main
