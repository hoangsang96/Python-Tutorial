stuff = {'name' : 'Zane', 'age' : 21, 'height' : 6*12+2}
print("Name : ", stuff['name'])
print("Age : ", stuff['age'])
print('height : ', stuff['height'])

stuff['city'] = "San Francisco"
print('City : ', stuff['city'])

for key, value in stuff.items():
	print("Key : ", key, " , value : " , value)
