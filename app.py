from flask import Flask, render_template, request, send_from_directory
import os
import tempvalues
import PIL
import numpy as np
"""
applemodel = tf.keras.models.load_model('models/apple.h5')
grapemodel = tf.keras.models.load_model('models/grape.h5')
potatomodel = tf.keras.models.load_model('models/potato.h5')
strawberrymodel = tf.keras.models.load_model('models/strawberry.h5')
tomatomodel = tf.keras.models.load_model('models/tomato.h5')

#classmodel = tf.keras.models.load_model('models/apple2.h5')
ref = {0:applemodel, 1:grapemodel, 2:potatomodel, 3:strawberrymodel, 4:tomatomodel}
disease = {0:{0:'Apple Scab', 1: 'Black Rot', 2: 'Cedar Apple Rust', 3:'Healthy'}, 1:{0:'Black Rot', 1:'Black Measles', 2:'Healthy', 3:'Leaf Blight'}, 2:{0:'Early Blight', 1:'Healthy', 2:'Late Blight'}, 3:{0:'Healthy',1:'Leaf Scrotch'}, 4:{0:'Bacterial Spot', 1:'Early Blight', 2:'Healthy', 3:'Late Blight', 4:'Leaf Mould', 5:'Septoria Leaf Spot', 6:'Spider Mites', 7:'Target Spot', 8:'Tomato Mosaic Virus', 9:'Tomato Yellow Leaf Curl Virus'}}
name = {0:applemodel, 1:grapemodel, 2:potatomodel, 3:strawberrymodel, 4:tomatomodel}
"""

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder
pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'dleaf.jpg')

@app.route("/")
def index():
    return render_template('index.html', leaf_image=pic1, disease_image=pic1)

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    """
    image = PIL.Image.open(target)
    image = image.resize((256,256))
    image = np.asarray(image)
    leaf_class = np.argmax(classmodel(image))
    disease_model = ref[leaf_class] 
    disease_class = np.argmax(disease_model(image))
    leaf_disease = disease[leaf_class][disease_class]
    """

    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        file.save(destination)

    #return render_template("index.html", image_name=filename, identity=name[leaf_class], disease=leaf_disease, leaf_image=pic1, disease_image=pic2)
    return render_template("index.html", image_name=filename, identity=tempvalues.name, disease=tempvalues.disease, leaf_image=pic1, disease_image=pic1)

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

app.run(debug=True)