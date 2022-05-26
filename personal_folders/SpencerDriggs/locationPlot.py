import geopy
from geopy.geocoders import Nominatim
import csv


# This is where we find all the text addresses (regex), make it a big dictionary?
town_dict = []
#Turn those town names into coordinates
geolocator = Nominatim(user_agent="WWPapers")

#loop all of this
location = geolocator.geocode("Birmingham, Warwickshire, England")
town_dict.append(["hree", location.latitude, location.longitude])
#name of town, latitude, longitude, journal date
#in tableau, show how many times he references a town

print(location.latitude, location.longitude)

#print each row to a csv file
with open('alltown.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(["townName","Latitude","Longitude"]) 
    write.writerows(town_dict)

#df = pd.DataFrame(data=town_dict, index=[0])
#df = (df.T)
#print (df)
#df.to_excel('dict1.xlsx') 