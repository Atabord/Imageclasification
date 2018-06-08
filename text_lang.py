import io
import os, errno
import glob
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

directory = os.path.join(
    os.path.dirname(__file__),
    'imagenes')

imagesList = (file for file in os.listdir(directory) if file.endswith('.' + "jpg") or file.endswith('.' + "jpeg") or file.endswith('.' + "gif"))
# print(list(imagesList))

def createFolder(name):
	folderName = directory + '/' + name
	if not os.path.exists(folderName):
		try:
			os.makedirs(folderName)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise

def moveFile(source, name):
	destination = directory + '/' + name +'/'+ img
	os.rename(source, destination)

for img in imagesList:
	source = directory + '/'+ img
	with io.open(source, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	responseT = client.text_detection(image=image)
	texts = responseT.text_annotations
	if len(texts) > 0:
	    print("La imagen tiene texto")
	    lang = texts[0].locale
	    print('lenguaje: ' + lang)
	else:
	    lang = "undefined"
	    print("la imagen no tiene texto: " + lang)
	
	createFolder(lang)
	moveFile(source, lang)
