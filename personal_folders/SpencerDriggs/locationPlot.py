import geopy
from geopy.geocoders import Nominatim

# This is where we find all the text addresses (regex), make it a big dictionary?

#Turn those town names into coordinates
geolocator = Nominatim(user_agent="WWPapers")
location = geolocator.geocode("Birmingham, Warwickshire, England")
print(location.latitude, location.longitude)