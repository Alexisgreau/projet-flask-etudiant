from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np

app = Flask(__name__)

# Initialisation du DataFrame pour stocker les étudiants
etudiants_df = pd.DataFrame(columns=["nom", "age", "identifiant", "notes"])

# Fonction pour ajouter un étudiant dans le DataFrame
def ajouter_etudiant(nom, age, identifiant):
    global etudiants_df
    new_student = pd.DataFrame({
        "nom": [nom],
        "age": [age],
        "identifiant": [identifiant],
        "notes": [[]]
    })
    etudiants_df = pd.concat([etudiants_df, new_student], ignore_index=True)

# Fonction pour vérifier si l'identifiant est unique
def est_identifiant_unique(identifiant):
    return identifiant not in etudiants_df["identifiant"].values

# Fonction pour calculer la moyenne des notes d'un étudiant
def calculer_moyenne(notes):
    if len(notes) == 0:
        return 0
    return round(np.mean(notes), 2)

# Route principale pour afficher la liste des étudiants
@app.route('/')
def afficher_etudiants():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    start = (page - 1) * per_page
    end = start + per_page
    etudiants_affiches = etudiants_df.iloc[start:end].to_dict(orient="records")
    total_pages = (len(etudiants_df) + per_page - 1) // per_page

    return render_template('index.html', etudiants=etudiants_affiches, page=page, total_pages=total_pages)

# Route pour ajouter un étudiant
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_etudiant_route():
    error_message = None
    if request.method == 'POST':
        nom = request.form['nom']
        age = int(request.form['age'])
        identifiant = request.form['identifiant']

        if est_identifiant_unique(identifiant):
            ajouter_etudiant(nom, age, identifiant)
            return redirect(url_for('afficher_etudiants'))
        else:
            error_message = "Erreur : L'identifiant existe déjà ! Veuillez en choisir un autre."

    return render_template('ajouter_etudiant.html', error_message=error_message)

# Route pour afficher les détails d'un étudiant et lui ajouter une note
@app.route('/etudiant/<int:id>', methods=['GET', 'POST'])
def afficher_etudiant(id):
    etudiant = etudiants_df.iloc[id]
    if request.method == 'POST':
        note = float(request.form['note'])
        etudiants_df.at[id, 'notes'].append(note)
        return redirect(url_for('afficher_etudiant', id=id))

    moyenne = calculer_moyenne(etudiant['notes'])
    return render_template('details_etudiant.html', etudiant=etudiant, moyenne=moyenne, id=id)

# Route pour supprimer un étudiant
@app.route('/supprimer/<identifiant>')
def supprimer_etudiant(identifiant):
    global etudiants_df
    # Trouver l'index de l'étudiant avec l'identifiant fourni
    etudiants_df = etudiants_df[etudiants_df["identifiant"] != identifiant].reset_index(drop=True)
    return redirect(url_for('afficher_etudiants'))


# Route pour supprimer une note spécifique d'un étudiant
@app.route('/supprimer_note/<int:id>/<int:index>')
def supprimer_note(id, index):
    notes = etudiants_df.at[id, 'notes']
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for('afficher_etudiant', id=id))

# Route pour modifier les informations d'un étudiant
@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier_etudiant(id):
    if request.method == 'POST':
        etudiants_df.at[id, 'nom'] = request.form['nom']
        etudiants_df.at[id, 'age'] = int(request.form['age'])
        return redirect(url_for('afficher_etudiant', id=id))

    etudiant = etudiants_df.iloc[id]
    return render_template('modifier_etudiant.html', etudiant=etudiant, id=id)

if __name__ == '__main__':
    app.run(debug=True)
