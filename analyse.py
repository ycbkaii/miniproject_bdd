import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


# On importe la data
data = pd.read_csv("IMDB_Movies_Dataset.csv")


# On séléctionne les variables qui nous interessent
data = data[['Title', 'Average Rating', 'Director', 'Release Date', 'Country of Origin', 'Budget', 'Runtime', 'Metascore',"Writer"]]

#region BAR CHART


# On met en place un BARCHART pour visualiser les données, le nombre des films des réalisateurs qui ont un average rating sur un de leurs films > 9 
labels = data.loc[data['Average Rating'] >= 9.0]["Director"].to_list()
countTitle = data.groupby("Director").count().reset_index()[["Title","Director"]].reset_index()
sizes = []
for i in range(len(labels)) :
    sizes.append(countTitle.loc[countTitle["Director"] == labels[i] ]["Title"].to_list()[0])

for j in range(len(labels)) :
    labels[j] = labels[j].replace(" ","\n")
# Création du diagramme en secteurs
plt.figure(figsize=(8, 8))
bar  = plt.bar(labels,sizes,width=0.5)

plt.title('Répartition des réalisateur')
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
# plt.show()

#endregion

#region BARGRAPH
# On fait un BARGRAPH mentionnant la somme du budget de chaque auteurs sur chacuns de leurs  films et qui ont au moins un film qui est supérieur à 9 en average rating

dataBarGraph = data[['Director', 'Budget', 'Average Rating']]

# Les réalisateurs des films avec au moins un film >=9
directorsSelected = dataBarGraph.loc[data['Average Rating'] >= 9.0]["Director"].to_list()








# Fonction pour convertir le budget en dollars
def convertNumber(row) :
    input_string = row
    if (str(input_string) == "nan" ) :
        return 0
    # Table des taux de change (symboles -> taux en USD)
    exchange_rates = {
        '$' : 1.00,
        '€': 1.10,    # Euro
        '£': 1.25,    # Livre sterling
        'C$': 0.75,   # Dollar canadien
        'CHF': 1.10,  # Franc suisse
        '¥': 0.007,   # Yen japonais
        '元': 0.14,   # Yuan chinois
        '₹': 0.012,   # Roupie indienne
        'A$': 0.65,   # Dollar australien
        'MX$': 0.05,  # Peso mexicain
        'R$': 0.20,   # Réal brésilien
        '₽': 0.01,    # Rouble russe
        'R': 0.05,    # Rand sud-africain
        '₩': 0.00075, # Won sud-coréen
        '₱': 0.018,   # Peso philippin
        'RM': 0.21,    # Ringgit malaisien
        'DEM' : 0.562,
        'ROL' : 0.000022
    }
    
    
    
    # Fonction pour vérifier si une chaîne contient une devise
    def contains_currency(string):
        currency_regex = re.compile(r'(' + '|'.join(re.escape(key) for key in exchange_rates.keys()) + r')')
        match = currency_regex.search(string)
        return match.group(0) if match else None
    
    contientDevise = contains_currency(input_string)
    if contientDevise == None :
        return 0
    
    # On convertit en dollars
    devise = exchange_rates[contientDevise]
    
    
    
    
    # Utilise une expression régulière pour capturer les chiffres, y compris les séparateurs de milliers
    match = re.search(r'[\d,]+', input_string)
    if match:
        # Remplace les virgules pour convertir en un nombre entier
        number = int(match.group(0).replace(',', ''))
        return number * devise
    else:
        return 0  # Retourne None si aucun nombre n'est trouvé

# La somme du budget de chacuns des réalisateurs
dataBarGraph.loc[:, "Budget"] = dataBarGraph["Budget"].apply(convertNumber)

sommeBudget = dataBarGraph.groupby("Director").sum().reset_index()

sizesDirector = []
labelsDirector = []

for elem in directorsSelected :
   budgetDirector = sommeBudget.loc[sommeBudget["Director"] == elem]
   budget = budgetDirector["Budget"].to_list()[0]
   label = budgetDirector["Director"].to_list()[0]
   if int(budget) > 0 :
    sizesDirector.append(budget)
    labelsDirector.append(label)
       

# Création du diagramme en secteurs
plt.figure(figsize=(8, 8))
plt.bar(labelsDirector,sizesDirector)
plt.title('Répartition des réalisateur')
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
plt.show()

#endregion

#region DECISIONNEL

sommeBudgetTrier = sommeBudget.sort_values(by="Budget", ascending=False).loc[sommeBudget["Director"] == "Christopher Nolan"])
print(sommeBudgetTrier)