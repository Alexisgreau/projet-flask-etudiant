
# Application de Gestion des Étudiants

## Description de l'application

Cette application de gestion des étudiants, développée en Python avec le framework Flask, permet de gérer facilement les informations des étudiants. Elle propose des fonctionnalités permettant d'ajouter, de modifier, de supprimer et de consulter les informations de chaque étudiant. De plus, il est possible d'ajouter des notes aux étudiants et de calculer leur moyenne. Une fonctionnalité de recherche en temps réel est également incluse, facilitant la recherche par nom, âge ou identifiant.

## Fonctionnalités principales

- **Ajouter un étudiant** : Permet d'ajouter un étudiant en spécifiant son nom, son âge et un identifiant unique.
- **Afficher la liste des étudiants** : Affiche une liste paginée des étudiants, avec 10 étudiants par page.
- **Rechercher un étudiant** : Barre de recherche en temps réel pour rechercher par nom, âge ou identifiant.
- **Détails d'un étudiant** : Affiche les informations détaillées d'un étudiant, y compris les notes.
- **Ajouter une note** : Permet d'ajouter une note à un étudiant spécifique.
- **Calculer la moyenne** : Affiche la moyenne des notes pour chaque étudiant.
- **Modifier un étudiant** : Permet de modifier les informations d'un étudiant (nom et âge).
- **Supprimer un étudiant** : Supprime un étudiant après confirmation.
- **Supprimer une note** : Supprime une note spécifique d'un étudiant.

## Instructions pour l'installation et l'exécution

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Alexisgreau/projet-flask-etudiant.git
   cd projet-flask-etudiant
   ```

2. **Installer les dépendances**
   - Assurez-vous d'avoir Python 3 et `pip` installés.
   - Installez les packages requis avec :
     ```bash
     pip install flask
     ```

3. **Lancer l'application**
   - Exécutez le serveur Flask avec :
     ```bash
     python app.py
     ```
   - L'application sera disponible à l'adresse `http://127.0.0.1:5000`.

## Guide d'utilisation de l'application

1. **Ajouter un étudiant** :
   - Cliquez sur "Ajouter un étudiant" en bas de la page principale.
   - Saisissez le nom, l'âge et un identifiant unique pour l'étudiant.
   - Si l'identifiant est déjà utilisé, un message d'erreur s'affichera.

2. **Afficher les détails d'un étudiant** :
   - Dans la liste des étudiants, cliquez sur "Détails" à côté de l'étudiant que vous souhaitez consulter.
   - Les informations complètes, y compris les notes, seront affichées.

3. **Ajouter une note** :
   - Dans la page de détails d'un étudiant, saisissez une note et cliquez sur "Ajouter une note".
   - La note sera ajoutée et la moyenne recalculée.

4. **Modifier un étudiant** :
   - Dans la liste des étudiants, cliquez sur "Modifier" à côté de l'étudiant que vous souhaitez mettre à jour.
   - Saisissez les nouvelles informations (nom et/ou âge) et sauvegardez.

5. **Supprimer un étudiant** :
   - Dans la liste des étudiants, cliquez sur "Supprimer" à côté de l'étudiant.
   - Une boîte de dialogue de confirmation s'affichera pour valider la suppression.

6. **Recherche en temps réel** :
   - Utilisez la barre de recherche au-dessus de la liste des étudiants pour filtrer les résultats en fonction du nom, de l'âge ou de l'identifiant.
