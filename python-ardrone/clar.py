from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import Video as ClVideo
app = ClarifaiApp(api_key='4457471b3f58454d98334e08cad1e593')

model = app.models.get('general-v1.3')
image = ClImage(file_obj=open('/home/kshea/Pictures/chair.jpg', 'rb'))
print(image)
a=model.predict([image])

b=a["outputs"][0]["data"]["concepts"]
for i in b:
    print(i["name"])

