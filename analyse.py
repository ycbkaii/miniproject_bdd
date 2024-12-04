import pandas as pd
import matplotlib.pyplot as plt


# On importe la data
data = pd.read_csv("IMDB_Movies_Dataset.csv")
print(data)


# On séléctionne les variables qui nous interessent
data = data[['Title', 'Average Rating', 'Director', 'Release Date', 'Country of Origin', 'Budget', 'Runtime', 'Metascore']]

print(data)





# On met en place une Pie Chart pour visualiser les données, le nombre des films des réalisateurs qui ont un average rating sur leurs films > 9 
labels = [data['Director']]
sizes = [data['Average Rating']]


# Création du diagramme en secteurs
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Répartition des catégories')
plt.show()


