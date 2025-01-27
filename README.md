# Analyse des Films IMDB : Visualisations et Régressions

## Description

Ce projet Python vise à analyser un dataset contenant des informations sur les films IMDB. Il utilise des outils comme Pandas et Matplotlib pour effectuer des visualisations de données et des régressions linéaires. Les principales étapes incluent la création de graphiques, la conversion des budgets en dollars, et l'analyse de la relation entre le budget et la note moyenne des films.

---

## Prérequis

Avant de commencer, assurez-vous que votre environnement dispose des bibliothèques suivantes :

- `pandas`
- `matplotlib`
- `numpy`
- `re`

Pour les installer, exécutez :
```bash
pip install pandas matplotlib numpy
```

---

## Fonctionnalités

### 1. Visualisation des réalisateurs et de leurs films


### 2. Analyse des budgets


### 3. Régression linéaire


---

## Comment exécuter le projet

1. **Préparer les données :**
   - Téléchargez le fichier `IMDB_Movies_Dataset.csv` et placez-le dans le même répertoire que le script.

2. **Lancer le script :**
   - Exécutez le script avec Python :
     ```bash
     python analyse.py
     ```
ON a donc l'affichage des observations

---

## Organisation du code

### Importation des données
- Lecture des données depuis le fichier CSV.
- Sélection des colonnes pertinentes : Titre, Réalisateur, Date de sortie, Budget, Note moyenne, etc.

### Visualisation des réalisateurs
- Diagramme en barres pour le nombre de films par réalisateur avec une note >= 9.

### Conversion des budgets
- Une fonction `convertNumber` convertit les budgets en dollars en fonction des devises présentes dans les données.

### Analyse des budgets
- Visualisation des budgets totaux des réalisateurs sélectionnés.

### Régression linéaire
- Implémentation d'une régression linéaire simple pour analyser la relation entre budget et note moyenne.
- Régressions spécifiques par réalisateur.

---

## Résultats attendus

- **Diagrammes en barres** : Nombre de films et budgets par réalisateur.
- **Graphiques de régression linéaire** : Relation entre budget et note moyenne.
- **Coefficients de régression** : Calculés et affichés dans la console.

---

## Améliorations possibles

- Ajouter des analyses pour d'autres métriques (ex. : durée des films, origine des pays).
- Intégrer un tableau interactif pour filtrer les réalisateurs ou films.
