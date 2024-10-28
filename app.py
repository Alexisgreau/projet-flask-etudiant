from flask import Flask, render_template, request, redirect, url_for

#Contrôle sur les ID/ clef unique
#Arrondie des moyennes
#Confirmation des supression
#Contôle sur les caractères pour la saisies des id ou nom 
#N'afficher que 10 étudiants par page / Rajouter la recherche selon 

app = Flask(__name__)

# Liste pour stocker les étudiants
etudiants = []

# Classe Etudiant
class Etudiant:
    def __init__(self, nom, age, identifiant):
        self.nom = nom
        self.age = age
        self.identifiant = identifiant
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return round(sum(self.notes) / len(self.notes),2)

# Fonction pour vérifier si l'identifiant est unique
def est_identifiant_unique(identifiant):
    for etudiant in etudiants:
        if etudiant.identifiant == identifiant:
            return False
    return True

# Route principale pour afficher la liste des étudiants
@app.route('/')
def afficher_etudiants():
    # Récupère le numéro de page depuis l'URL (défaut : 1)
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Nombre d'étudiants par page

    # Calcul des indices pour récupérer les étudiants de la page actuelle
    start = (page - 1) * per_page
    end = start + per_page
    etudiants_affiches = etudiants[start:end]

    # Calcul du nombre total de pages
    total_pages = (len(etudiants) + per_page - 1) // per_page

    return render_template('index.html', etudiants=etudiants_affiches, page=page, total_pages=total_pages)

# Route pour ajouter un étudiant
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_etudiant():
    error_message = None
    if request.method == 'POST':
        nom = request.form['nom']
        age = int(request.form['age'])
        identifiant = request.form['identifiant']

        # Vérification de l'unicité de l'identifiant
        if est_identifiant_unique(identifiant):
            nouvel_etudiant = Etudiant(nom, age, identifiant)
            etudiants.append(nouvel_etudiant)
            return redirect(url_for('afficher_etudiants'))
        else:
            # Définir un message d'erreur si l'identifiant existe déjà
            error_message = "Erreur : L'identifiant existe déjà !"

    return render_template('ajouter_etudiant.html', error_message=error_message)

# Route pour afficher les détails d'un étudiant et lui ajouter une note
@app.route('/etudiant/<int:id>', methods=['GET', 'POST'])
def afficher_etudiant(id):
    etudiant = etudiants[id]
    if request.method == 'POST':
        note = float(request.form['note'])
        etudiant.ajouter_note(note)
        return redirect(url_for('afficher_etudiant', id=id))
    moyenne = etudiant.calculer_moyenne()
    return render_template('details_etudiant.html', etudiant=etudiant, moyenne=moyenne, id=id)

# Route pour supprimer un étudiant
@app.route('/supprimer/<int:id>')
def supprimer_etudiant(id):
    del etudiants[id]
    return redirect(url_for('afficher_etudiants'))

# Route pour supprimer une note spécifique d'un étudiant
@app.route('/supprimer_note/<int:id>/<int:index>')
def supprimer_note(id, index):
    etudiant = etudiants[id]
    if 0 <= index < len(etudiant.notes):
        del etudiant.notes[index]
    return redirect(url_for('afficher_etudiant', id=id))

# Route pour modifier les informations d'un étudiant
@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier_etudiant(id):
    etudiant = etudiants[id]
    if request.method == 'POST':
        # Récupérer les nouvelles valeurs depuis le formulaire
        etudiant.nom = request.form['nom']
        etudiant.age = int(request.form['age'])
        return redirect(url_for('afficher_etudiant', id=id))
    return render_template('modifier_etudiant.html', etudiant=etudiant, id=id)

if __name__ == '__main__':
    app.run(debug=True)
