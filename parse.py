import json
myfile = open('data.json','r')
data=myfile.read()


jsonData = json.loads(data)
print jsonData
