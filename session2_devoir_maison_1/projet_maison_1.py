# import des modules usuels
import numpy as np
import pandas as pd

def haversine_np(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    diff_lat = lat2 - lat1
    diff_lon = lon2 - lon1

    a = np.sin(diff_lat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(diff_lon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

# fonction recherche de ville
def ville(geo, lat, lon):
    s =haversine_np(geo['Latitude'], geo['Longitude'], lat, lon)
    # print(lat, lon)
    # print(geo.iloc[s.idxmin()]['Latitude'], geo.iloc[s.idxmin()]['Longitude'])
    # print(s.sort_values())
    print("\n-----------------------------------------------------------------")
    print(f'La plus proche commune est {geo.iloc[s.idxmin()]["Commune"].title()} ({geo.iloc[s.idxmin()]["Code Postal"]}) située à une distance de {s.min():.3f} km')
    print("-----------------------------------------------------------------\n")

def random_coordinates():
    # on applique la fonction à une coordonnée tirée au hasard
    # init du random
    np.random.seed(0)
    a, b = 41.5, 51.1  # latitude min et max de la France métropolitaine
    lat = (b - a) * np.random.random() + a
    a, b = -5.1, 9.5  # longitude min et max de la France métropolitaine
    lon = (b - a) * np.random.random() + a    
    return lat, lon

def main():
    # options d'affichage
    pd.set_option("display.min_rows", 16)

    # chargement des données
    geo = pd.read_csv("correspondance-code-insee-code-postal.csv",
                       sep=';',
                       usecols=range(11))

    ###### REPONSE 1.1
    # on ajoute la colonne "CP Ville"
    geo["CP Ville"] = geo["Code Postal"] + " " + geo["Commune"]

    ###### REPONSE 1.2
    # extraire Latitude et Longitude de "geo_point_2d"
    geo["Latitude"] = geo["geo_point_2d"].apply(lambda x: float(x.split(', ')[0]))
    geo["Longitude"] = geo["geo_point_2d"].apply(lambda x: float(x.split(', ')[1]))

    lat, lon = random_coordinates()
    
    ville(geo, lat, lon)

    

    

if __name__ == '__main__':
  main()