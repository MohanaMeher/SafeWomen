import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
    pprint.pprint(result)  
    
if __name__=="__main__": 
    coordinates =(28.613939, 77.209023) 
    reverseGeocode(coordinates) 