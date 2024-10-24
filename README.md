
# Projet Flask - Gestion d'Étudiants

Ce projet est une application web simple, développée avec Flask, permettant de gérer une liste d'étudiants. Il permet d'ajouter des étudiants, de consulter leurs détails, de modifier leurs informations, d'ajouter des notes et de calculer la moyenne des notes.

## Fonctionnalités

- Ajouter un étudiant (nom, âge, numéro d'identification)
- Consulter les détails d'un étudiant (nom, âge, notes)
- Ajouter des notes à un étudiant
- Calculer la moyenne des notes
- Modifier les informations d'un étudiant
- Supprimer un étudiant ou une note

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- Flask

## Installation

1. Clonez le dépôt :

   git clone https://github.com/Alexisgreau/projet-flask-etudiant.git


2. Accédez au dossier du projet :

   cd projet-flask-etudiant


3. Installez les dépendances :

   pip install flask

## Lancement de l'application

1. Lancez l'application Flask avec la commande suivante :

   python app.py


2. Ouvrez votre navigateur et accédez à l'adresse suivante :

   http://127.0.0.1:5000/


## Structure du projet

- **app.py** : Contient la logique principale de l'application Flask.
- **templates/** : Contient les fichiers HTML pour l'interface utilisateur.
  - index.html : Page d'accueil avec la liste des étudiants.
  - ajouter_etudiant.html : Formulaire pour ajouter un étudiant.
  - details_etudiant.html : Détails d'un étudiant et possibilité d'ajouter des notes.
  - modifier_etudiant.html : Formulaire pour modifier les informations d'un étudiant.

## Contribuer

Les contributions sont les bienvenues ! Pour proposer des modifications, veuillez ouvrir une **pull request**.
