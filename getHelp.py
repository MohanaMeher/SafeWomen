import requests, json 
  
api_key = 'AIzaSyBfuq4-ElrwPsz8LGwSJ68BPQ32n1uvE7c'
  
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
query = ('police in koramangal') 
  
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 

x = r.json() 
y = x['results'] 

for i in range(len(y)): 
    print(y[i]['name']) 