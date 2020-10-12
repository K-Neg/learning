import json

with open('jsonData.json') as json_file: 
    data = json.load(json_file) 
  
   
    print(data['objectives'])
      
    print(type(data))



     """ "objectives" : {'name': ["a","b","c"],
                                'value':["1","2","3"]
                }"""