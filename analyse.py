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
plt.xlabel("Réalisateurs")
plt.ylabel("Nombre des films des réalisateurs")
# plt.show()

#endregion

#region BARGRAPH
# On fait un BARGRAPH mentionnant la somme du budget de chaque auteurs sur chacuns de leurs  films et qui ont au moins un film qui est supérieur à 9 en average rating

dataBarGraph = data[['Director', 'Budget', 'Average Rating',"Metascore"]]

# Les réalisateurs des films avec au moins un film >=9
directorsSelected = dataBarGraph.loc[data['Average Rating'] >= 9.0]["Director"].to_list()



# Fonction pour convertir le budget en dollars
def convertNumber(row) :
    input_string = row
    if (str(input_string) == "nan" ) :
        return 0
    # Table des taux de change (symboles -> taux en USD)
    exchange_rates = {
        '$': 1.00,        # Dollar américain
        '€': 1.10,        # Euro
        '£': 1.25,        # Livre sterling
        'C$': 0.75,       # Dollar canadien
        'CHF': 1.10,      # Franc suisse
        '¥': 0.007,       # Yen japonais
        '元': 0.14,       # Yuan chinois
        '₹': 0.012,       # Roupie indienne
        'A$': 0.65,       # Dollar australien
        'MX$': 0.05,      # Peso mexicain
        'R$': 0.20,       # Réal brésilien
        '₽': 0.01,        # Rouble russe
        '₩': 0.00075,     # Won sud-coréen
        'FRF': 0.152,     # Franc français
        'DEM': 0.562,     # Mark allemand
        'SEK': 0.09,      # Couronne suédoise
        'DKK': 0.14,      # Couronne danoise
        'HK$': 0.13,      # Dollar de Hong Kong
        'CN¥': 0.14,      # Yuan chinois
        'HUF': 0.0027,    # Forint hongrois
        'NOK': 0.11,      # Couronne norvégienne
        'TRL': 0.000054,  # Lire turque ancienne
        'EGP': 0.032,     # Livre égyptienne
        'PLN': 0.24,      # Zloty polonais
        'IRR': 0.000024,  # Rial iranien
        'ITL': 0.00052,   # Lire italienne
        'LVL': 1.61,      # Lats letton
        'BEF': 0.024,     # Franc belge
        'ESP': 0.006,     # Peseta espagnole
        'BDT': 0.0093,    # Taka bangladais
        'MVR': 0.065,     # Rufiyaa maldivienne
        'NT$': 0.031      # Dollar taïwanais
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
plt.xlabel("Réalisateurs")
plt.ylabel("Le budget total du réalisateur en milliards dollars")
plt.show()

#endregion

#region DECISIONNEL

# On supprime les rows qui ont un budget inconnu ou égale à 0
dataBarGraph = dataBarGraph[dataBarGraph['Budget'] != 0]
dataBarGraph = dataBarGraph.dropna(subset="Budget")
dataBarGraph = dataBarGraph[dataBarGraph['Budget'] >= 50000000]
dataBarGraph = dataBarGraph.dropna(subset="Metascore")

noteGen = dataBarGraph["Average Rating"].to_numpy()
budgetGen = dataBarGraph["Budget"].to_numpy()


# REGRESSION LINÉAIRE
# Données exemple
x = budgetGen  # Variables indépendantes
y = noteGen # Variables dépendantes

# Calcul des coefficients de régression linéaire
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calcul de la pente (beta_1)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
beta_1 = numerator / denominator

# Calcul de l'interception (beta_0)
beta_0 = y_mean - beta_1 * x_mean

print(f"Pente (beta_1): {beta_1}")
print(f"Intercept (beta_0): {beta_0}")


# Prévisions
y_pred = beta_0 + beta_1 * x

# Affichage des résultats
plt.scatter(x, y, color='blue', label='Données réelles')
plt.plot(x, y_pred, color='red', label='Régression linéaire')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Régression Linéaire Simple')
plt.show()



for real in labelsDirector :
    noteDirector = dataBarGraph.loc[dataBarGraph["Director"] == real ]["Average Rating"].to_numpy()
    budgetDirector = dataBarGraph.loc[dataBarGraph["Director"] == real]["Budget"].to_numpy()
    # REGRESSION LINÉAIRE
    # Données exemple
    x = budgetDirector  # Variables indépendantes
    y = noteDirector # Variables dépendantes

    # Calcul des coefficients de régression linéaire
    n = len(x)
    if n > 1 :
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        # Calcul de la pente (beta_1)
        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean) ** 2)
        beta_1 = numerator / denominator

        # Calcul de l'interception (beta_0)
        beta_0 = y_mean - beta_1 * x_mean

        print(f"Pente (beta_1): {beta_1}")
        print(f"Intercept (beta_0): {beta_0}")


        # Prévisions
        y_pred = beta_0 + beta_1 * x

        # Affichage des résultats
        plt.scatter(x, y, color='blue', label='Données réelles')
        plt.plot(x, y_pred, color='red', label='Régression linéaire')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.title('Régression Linéaire Simple ' + str(real))
        plt.show()
