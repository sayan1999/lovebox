from pickle import load, dump

def loaddata(location):
	try:
		with open(location, 'rb') as file:
			data=load(file)
			file.close()
		return data
	except FileNotFoundError:
		print("File not found at ", location)
		return None

def savedata(data, location):

	with open(location, 'wb+') as file:
		dump(data, file)
		file.close()