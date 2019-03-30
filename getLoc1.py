import googlemaps
gmaps = googlemaps.Client(key='AIzaSyBGCjNPwzhQ00l0mkLVuou0kOzHFuhN_p4')
loc = gmaps.geolocate()
print(loc)