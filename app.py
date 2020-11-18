from flask import Flask, render_template, request, send_from_directory
import os
import tempvalues
import tensorflow as tf
import PIL
import numpy as np

applemodel = tf.keras.models.load_model('models/apple.h5')
grapemodel = tf.keras.models.load_model('models/grape.h5')
potatomodel = tf.keras.models.load_model('models/apple.h5')
strawberrymodel = tf.keras.models.load_model('models/apple.h5')
tomatomodel = tf.keras.models.load_model('models/apple.h5')

#classmodel = tf.keras.models.load_model('models/apple2.h5')
#ref = {0:applemodel, 1:grapemodel, 2:potatomodel, 3:strawberrymodel, 4:tomatomodel}
#disease = {0:{0:'Apple Scab', 1: ''}}
#name = {0:apple, 1:grapemodel, 2:potatomodel, 3:strawberrymodel, 4:tomatomodel}
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder
pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'leaf.png')
pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'leaf.png')

@app.route("/")
def index():
    return render_template('index.html', leaf_image=pic1, disease_image=pic2)

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    image = PIL.Image.open(target)
    image = image.resize((256,256))
    image = np.asarray(image)
    leaf_class = np.argmax(classmodel(image))
    disease_model = ref[leaf_class] 
    disease_class = np.argmax(disease_model(image))
    leaf_disease = disease[leaf_class][disease_class]

    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        file.save(destination)

    return render_template("index.html", image_name=filename, identity=name[leaf_class], disease=leaf_disease, leaf_image=pic1, disease_image=pic2)

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

app.run(debug=True)