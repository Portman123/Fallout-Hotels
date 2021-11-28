#Disclaimer this code probably won't work if you run it on it's own as it refers to variables defined in another script.
#This code includes the functions used to:
#   1. Import cities.
#   2. Plot the danger zone of nuclear explosions (blast radius).
#   3. Calculate distance between two points on a spherical object in the context of this project.
#   4. Calculate the number of danger zones (nuclear explosions, nuclear power plant fall out) a given point is in.
#   5. For every hotel in the hotels dataset, calculate the number of danger zones it's in.
#        Add this as a new column to the dataset.








#----------------------------------------------------------------------------------------------------------------
#RUN THIS TO INSTALL GEOPY (used for calculating distances between points)
#pip install geopy
import geopy.distance

#Importing cities data
cities = pd.read_csv("https://raw.githubusercontent.com/Portman123/Fallout-Hotels/main/worldcities.csv")
cities = cities.loc[cities['population']>1000000]








#----------------------------------------------------------------------------------------------------------------
# PLOTTING BLAST RADIUS OF CITIES
for lat, lon, city, pop in zip(cities['lat'], cities['lng'], cities['city'], cities['population']):
    #Creating the marker
    folium.Marker(
    #Coordinate of the country
    location=[lat, lon],
    #The popup that show up if click the marker
    popup=folium.Popup(f"""Major city - <b>{city}</b> <br>
                    """, max_width=len(f"Major city - {city}")*10),
    icon=folium.features.CustomIcon("https://i.ibb.co/2sCs96V/Skull-Icon-svg.png", icon_size=(15, 15))
    ).add_to(m)


for lat, lon, pop in zip(cities['lat'], cities['lng'], cities['population']):
  #Fallout radius (based on Castle Bravo)
  folium.Circle([lat, lon], radius=76*1000, color='#ff0000', fill_color='#ff0000', opacity=0.2).add_to(m)
  #Fireball radius (based on Castle Bravo)
  folium.Circle([lat, lon], radius=7.2*1000, color='#000000', fill_color='#000000', opacity=0.3).add_to(m)








#----------------------------------------------------------------------------------------------------------------
#Distance between two points method
#Input: lattitude and longittude of point A
#       lattitude and longittude of point B

def calculateDistance(latA, lngA, latB, lngB):

  coords1 = (latA,lngA)
  coords2 = (latB,lngB)

  return geopy.distance.VincentyDistance(coords1, coords2).miles








#----------------------------------------------------------------------------------------------------------------
# Number of danger zones a given point is in 
#Input: lattitude and longittude of a point on the map


def numDangerZoneOverlaps(lat, lng):

  #This is the worst code I have ever written
  citiesOfInterest = cities.loc[(cities['lat']<=(lat + 50)) & (cities['lat']>= (lat - 50)) & (cities['lng']<=(lng + 50)) & (cities['lng']>= (lng - 50))]
  nuclearOfInterest = nuclear_df.loc[(nuclear_df['latitude']<=(lat + 50)) & (nuclear_df['latitude']>= (lat - 50)) & (nuclear_df['longitude']<=(lng + 50)) & (nuclear_df['longitude']>= (lng - 50))]

  count = 0

  # count how many nuclear explosion radii a given point is in 
  for index, row in citiesOfInterest.iterrows():
    if (calculateDistance(row['lat'], row['lng'], lat, lng) <= 47.2242):
      count += 1
  
  for index, row in nuclearOfInterest.iterrows():
    if (calculateDistance(row['latitude'], row['longitude'], lat, lng) <= row['zone_2']):
      count += 1
  
  return count







#----------------------------------------------------------------------------------------------------------------
# creates list of dangerzone counts to add as column to hotels df
dangerzones = []
for index, row in hotels_df.iterrows():
  try:
     #print(row.head(), '\n\n ', numDangerZoneOverlaps(row['latitude'], row['longitude']), '\n\n ') #debugging
     dangerzones.append(numDangerZoneOverlaps(row['latitude'], row['longitude']))
  except ValueError:
    continue
# add to the dataframe
hotels_df.insert(4, 'danger-zones', dangerzones, True)


